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
