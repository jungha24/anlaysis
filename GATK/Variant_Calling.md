### starting from *GenotypeGVCFs* which were processed from whole genome sequencing

- GVCFs were generated through *HaplotypeCaller* with -ERC GVCF option
- https://gatk.broadinstitute.org/hc/en-us/articles/360035535932-Germline-short-variant-discovery-SNPs-Indels-
- 
#### 1. Consolidate GVCFs
- *GenotypeGVCFs* only can take (1) a single single-sample GVCFs, (2) a single multi-sample GVCF created by *CombineGVCFs*, and (3) a GenomicDB workspace created by *GenomicsDBImport*.
- use *GenomicDBImport* tool
- takes: one or more single-sample GVCFs
- imports: data over at least one genomics interval
- outputs: a directory containing a GenomicsDB dataset -> this would be used as input for *GenotypeGVCFs*.
- requirements:
  * gvcf files and tabix index files should be in a same folder.
  * mkdir temp
  * there should be no existing genomicsdb workspace directory. do not make it previously
  * sample_map file
  ~~~
  sample1   /path/to/sample1/gvcf/file
  sample2   /path/to/sample2/gvcf/file
  ~~~
  
~~~bashscript
gatk GenomicsDBImport \
  --jave-options "-Xmx100g -Xms100g" GenomicsDBImport \
  --sample-name-map covid_wgs_gvcf.sample_map
  --genomicsdb-workspace-path covid_wgs_gvcf_chr
  --intervals chr1
  --tmp-dir=temp
~~~
 
- since it tooks too long, I split the genome to numerous intervals and run them parallely
- split each line of "wgs_calling_regions.hg38.interval_list" into split.interval_list files.
- run following script in several window simultaneously
~~~bashscript
# cd interval_dic_a
# folder interval_dic_a includes *.interval_list* from aa to az
for f in *_h.interval_list
do
    /ssd-data/workspace/support/tool/gatk-4.1.6.0/gatk \
    --java-options "-Xmx100g" GenomicsDBImport \
    --sample-name-map ../covid_wgs_gvcf.sample_map \
    --genomicsdb-workspace-path ../gvcf_workspace_split_n"${${f##wgs_calling_regions.hg38.interval_list.splitn}%_h.interval_list}" \
    -L ${f} \
    --tmp-dir=../temp \
    --batch-size 500 \
    --reader-threads 10
done
~~~

#### 2. Joint-call cohort
- run GenotypeGVCF for each genomicsdb workspace folder
- running GenotypeGVCF tooks long, since GenomicsDB has to be loaded in memory ('https://gatk.broadinstitute.org/hc/en-us/community/posts/360063088471-Speeding-up-GenotypeGVCFS-GATK4')
-  ran following scripts parallely on different multiple windows...
~~~bashscript 
for f in gvcf_workspace_split_a*; do /ssd-data/workspace/support/tool/gatk-4.1.6.0/gatk --java-options "-Xmx100g" GenotypeGVCFs -R ./reference/GCA_000001405.15_GRCh38_no_alt_plus_hs38d1_analysis_set.fna -V gendb://${f} -O split_${f##*_}.vcf.gz; done
~~~
- merge vcf files
- (picard GatherVcfs) Input files must be supplied in genomic order and must not have events at overlapping positions.
~~~bashscript
java -jar /ssd-data/workspace/support/tool/picard_2.25.0/picard.jar GatherVcfs I=split_aa.vcf.gz I=split_ab.vcf.gz I=split_ac.vcf.gz I=split_ad.vcf.gz I=split_ae.vcf.gz I=split_af.vcf.gz I=split_ag.vcf.gz I=split_ah.vcf.gz I=split_ai.vcf.gz I=split_aj.vcf.gz I=split_ak.vcf.gz I=split_al.vcf.gz I=split_am.vcf.gz I=split_an.vcf.gz I=split_ao.vcf.gz I=split_ap.vcf.gz I=split_aq.vcf.gz I=split_ar.vcf.gz I=split_as.vcf.gz I=split_at.vcf.gz I=split_au.vcf.gz I=split_av.vcf.gz I=split_aw.vcf.gz I=split_ax.vcf.gz I=split_ay.vcf.gz O=split_a.vcf.gz
~~~

#### 3. Filter variants by variant (quality score) recalibration
- filter the raw variant callset is to use variant quality score recalibration (VQSR), which uses machine learning to identify annotation profiles of variants that are likely to be real, and assigns a VQSLOD score to each variant that is much more reliable than the QUAL score calculated by the caller.
- step 1, (**VariantRecalibrator**) the program builds a model based on training variants, then applies that model to the data to assign a well-calibrated probability to each variant call.
- step 2, (**ApplyVQSR**) use this variant quality score to filter the raw call set, thus producing a subset of calls with our desired level of quality, fine-tuned to balance specificity and sensitivity.
- https://gatk.broadinstitute.org/hc/en-us/articles/360035531112--How-to-Filter-variants-either-with-VQSR-or-by-hard-filtering
~~~bashscript
#generate index file of vcf
/ssd-data/workspace/support/tool/gatk-4.1.6.0/gatk IndexFeatureFile -I merge.vcf.gz

#Hard-filter a large cohort callset on ExcessHet using "VariantFiltration"
/ssd-data/workspace/support/tool/gatk-4.1.6.0/gatk --java-options "-Xmx100g" VariantFiltration -V merge.vcf.gz --filter-expression "ExcessHet > 54.69" --filter-name ExcessHet -O merge_excesshet.vcf.gz

#Create sites-only vcf with "MakeSitesOnlyVcf"
/ssd-data/workspace/support/tool/gatk-4.1.6.0/gatk MakeSitesOnlyVcf -I merge_excesshet.vcf.gz -O merge_sitesonly.vcf.gz

#calculate VQSLOD tranches for indels using "VariantRecalibrator"
/ssd-data/workspace/support/tool/gatk-4.1.6.0/gatk --java-options "-Xmx100g -Xms24g" VariantRecalibrator \
 -V merge_sitesonly.vcf.gz \
 --trust-all-polymorphic \
 -tranche 100.0 -tranche 99.95 -tranche 99.9 -tranche 99.5 -tranche 99.0 -tranche 97.0 -tranche 96.0 -tranche 95.0 -tranche 94.0 -tranche 93.5 -tranche 93.0 -tranche 92.0 -tranche 91.0 -tranche 90.0 \
 -an FS -an ReadPosRankSum -an MQRankSum -an QD -an SOR -an DP\
 -mode INDEL \
 --max-gaussians 4 \
 -resource:mills,known=false,training=true,truth=true,prior=12 /ssd-data/workspace/support/annotation/gca_broad_ref/Mills_and_1000G_gold_standard.indels.hg38.vcf.gz \
 -resource:axiomPoly,known=false,training=true,truth=false,prior=10 /ssd-data/workspace/support/annotation/gca_broad_ref/Axiom_Exome_Plus.genotypes.all_populations.poly.hg38.vcf.gz \
 -resource:dbsnp,known=true,training=false,truth=false,prior=2 /ssd-data/workspace/support/annotation/gca_broad_ref/Homo_sapiens_assembly38.dbsnp138.vcf \
 -O cohort_indels.recal \
 --tranches-file merge_indels.tranches
 
 #caculate VQSLOD tranches for SNPs using "VariantRecalibrator"
 /ssd-data/workspace/support/tool/gatk-4.1.6.0/gatk --java-options "-Xmx100g -Xms24g" VariantRecalibrator \
  -V merge_sitesonly.vcf.gz \
  --trust-all-polymorphic \
  -tranche 100.0 -tranche 99.95 -tranche 99.9 -tranche 99.8 -tranche 99.6 -tranche 99.5 -tranche 99.4 -tranche 99.3 -tranche 99.0 -tranche 98.0 -tranche 97.0 -tranche 90.0 \
  -an QD -an MQRankSum -an ReadPosRankSum -an FS -an MQ -an SOR -an DP \
  -mode SNP \
  --max-gaussians 6 \
  -resource:hapmap,known=false,training=true,truth=true,prior=15 /ssd-data/workspace/support/annotation/gca_broad_ref/hapmap_3.3.hg38.vcf.gz \
  -resource:omni,known=false,training=true,truth=true,prior=12 /ssd-data/workspace/support/annotation/gca_broad_ref/1000G_omni2.5.hg38.vcf.gz \
  -resource:1000G,known=false,training=true,truth=false,prior=10 /ssd-data/workspace/support/annotation/gca_broad_ref/1000G_phase1.snps.high_confidence.hg38.vcf.gz \
  -resource:dbsnp,known=true,training=false,truth=false,prior=7 /ssd-data/workspace/support/annotation/gca_broad_ref/Homo_sapiens_assembly38.dbsnp138.vcf \
  -O cohort_snps.recal \
  --tranches-file merge_snps.tranches
  
 #filter indels on VQSLOD using "ApplyVQSR"
 /ssd-data/workspace/support/tool/gatk-4.1.6.0/gatk --java-options "-Xmx100g -Xms24g" ApplyVQSR \
  -V merge_excesshet.vcf.gz \
  --recal-file cohort_indels.recal \
  --tranches-file merge_indels.tranches \
  --truth-sensitivity-filter-level 99.7 \
  --create-output-variant-index true \
  -mode INDEL \
  -O indel.recalibrated.vcf.gz
  
 #filter SNPs on VQSLOD using "ApplyVQSR"
 /ssd-data/workspace/support/tool/gatk-4.1.6.0/gatk --java-options "-Xmx100g -Xms24g" ApplyVQSR \
  -V indel.recalibrated.vcf.gz \
  --recal-file cohort_snps.recal \
  --tranches-file merge_snps.tranches \
  --truth-sensitivity-filter-level 99.7 \
  --create-output-variant-index true \
  -mode SNP \
  -O snp.recalibrated.vcf.gz
 ~~~
