### starting from *GenotypeGVCFs* which were processed from whole genome sequencing

- GVCFs were generated through *HaplotypeCaller* with -ERC GVCF option

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
- running GenotypeGVCF tooks long, since GenomicsDB has to be loaded in memory 
 -  'https://gatk.broadinstitute.org/hc/en-us/community/posts/360063088471-Speeding-up-GenotypeGVCFS-GATK4'
-  ran following scripts parallely on different multiple windows...
~~~bashscript 
for f in gvcf_workspace_split_a*; do /ssd-data/workspace/support/tool/gatk-4.1.6.0/gatk --java-options "-Xmx100g" GenotypeGVCFs -R ./reference/GCA_000001405.15_GRCh38_no_alt_plus_hs38d1_analysis_set.fna -V gendb://${f} -O split_${f##*_}.vcf.gz; done
~~~
