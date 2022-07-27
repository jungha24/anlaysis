# additional QC of pVCF from 200K 

#### starting point
* field 23155 (200k exome PLINK format - concated for all chromosome)
* qc fail list from (additional_QC_step1.md)


## marker QC
- remain QC pass variants from raw plink
### 1. remain DP/AD PASS variants 
~~~bashscript
/ssd-data/workspace/support/tool/plink2/plink2 --bfile ukb23155_cALL_b0_v1 --set-all-var-ids @:#:\$r:\$a --new-id-max-allele-len 112 --make-bed --out ukb23155_cALL_b0_v2
plink --bfile ukb23155_cALL_b0_v2 --extract /home/mchoilab_dell/dell_drobo/project_jhl/20210121_GABBR2_UKB_JH/20220403_analysis/pvcf_qc_fail_all.txt --make-bed --out /home/mchoilab_dell/dell_drobo/project_jhl/20210121_GABBR2_UKB_JH/20220403_analysis/ukb23155_cALL_b0_v3
~~~
### 2. filter marker/individuals
~~~bashscript
# [1] exclude variants out of exome capture region
/ssd-data/workspace/support/tool/plink2/plink2 --bfile ukb23155_cALL_b0_v3 --extract bed1 ../xgen_plus_spikein.GRCh38.edit2.bed --make-bed --out ukb23155_cALL_b0_v4

# [2] leave only SNPs (I applied only SNP specific DP/AB cutoff in additional_QC_step1. So use only SNPs) + biallelic + ind/marker call rate > 95%
/ssd-data/workspace/support/tool/plink2/plink2 --bfile ukb23155_cALL_b0_v4 --snps-only --max-alleles 2 --mind 0.05 --geno 0.05 --make-bed --out ukb23155_b0_v5

# [3] sex discordant
/ssd-data/workspace/support/tool/plink-1.9/plink --bfile ukb23155_b0_v5 --check-sex --out ukb23155_b0_v5
/ssd-data/workspace/support/tool/plink-1.9/plink --bfile ukb23155_b0_v5 --keep-fam ukb23155_b0_v5.sexcheck.ok.txt --make-bed --out ukb23155_b0_v6

# [4] relatedness
/ssd-data/workspace/support/tool/plink2/plink2 --bfile ukb23155_b0_v6 --king-cutoff 0.0884 --out ukb23155_b0_v7
/ssd-data/workspace/support/tool/plink-1.9/plink --bfile ukb23155_b0_v6 --remove-fam ukb23155_b0_v7.king.cutoff.out.id --make-bed --out ukb23155_b0_v7
/ssd-data/workspace/support/tool/plink2/plink2 --bfile ukb23155_b0_v6 --king-cutoff 0.354 --out ukb23155_b0_v8
/ssd-data/workspace/support/tool/plink-1.9/plink --bfile ukb23155_b0_v6 --remove-fam ukb23155_b0_v8.king.cutoff.out.id --make-bed --out ukb23155_b0_v8

# [6] ancestry stratification
#/ssd-data/workspace/support/tool/plink-1.9/plink --bfile ukb23155_b0_v7 --maf 0.01 --hwe 0.00001 --make-bed --out ukb23155_cALL_b0_v7.5
/ssd-data/workspace/support/tool/plink-1.9/plink --bfile ukb23155_b0_v7 --maf 0.01 --keep-allele-order --recode vcf-iid bgz --out ukb23155_cALL_b0_v7.6
bcftools annotate --rename-chrs chr_name_conv.txt ukb23155_cALL_b0_v7.5.vcf.gz -Oz -o ukb23155_cALL_b0_v7.5.reheader.vcf.gz
bcftools isec -p ukb23155_v7.6_1000g -Oz 20220303_kova_kg_GSAarray.vcf.gz ukb23155_cALL_b0_v7.6.reheader.vcf.gz
cd ukb23155_v7.6_1000g
bcftools merge 0002.vcf.gz 0003.vcf.gz -Oz -o ukb23155_v7.6_1000g.vcf.gz
split -l 19005 ukb23155_cALL_b0_v7.fam # split fam to 10 bins
cat xaa 20220303_kova_kg_GSAarray.fam > xaa.2
plink --vcf ukb23155_v7.6_1000g.vcf.gz --keep-fam xaa.2 --recode vcf-iid bgz --out ukb23155_v7.6_1000g.xaa.vcf.gz
plink --vcf ukb23155_v7.6_1000g.xaa.vcf.gz --pca 10 --out ukb23155_v7.6_1000g.xaa

# [5] check concordance between genotype data and exome data
## (1) extract 200k fam samples from 500k genotype data
for i in {1..22}; \
  do /ssd-data/workspace/support/tool/plink-1.9/plink \
  --bfile ukb22418_c${i}_b0_v2 \
  --keep-fam /home/mchoilab_dell/dell_drobo/project_jhl/20210121_GABBR2_UKB_JH/20220403_analysis/ukb23155_b0_v7.fam \
  --make-bed --out /home/mchoilab_dell/dell_drobo/project_jhl/20210121_GABBR2_UKB_JH/20220403_analysis/genotype_data/ukb22418_c${i}_b0_v3; done
## (2) convert plink to vcf
/ssd-data/workspace/support/tool/plink-1.9/plink --bfile ukb23155_b0_v7 --keep-allele-order --recode vcf bgz --out ./genotype_data/ukb23155_b0_v7
for i in {1..22}; do /ssd-data/workspace/support/tool/plink-1.9/plink --bfile ukb22418_c${i}_b0_v3 --keep-allele-order --recode vcf bgz --out ukb22418_c${i}_b0_v3; done
 bcftools concat *_v3.vcf.gz -Oz -o ukb22418_cALL_b0_v3.vcf.gz
## (3)liftover hg19 genotype vcf to hg38 genotype vcf
### use CrossMap
conda create -n crossmap_py2.7 python=2.7 CrossMap
conda activate crossmap_py2.7
# use Ensembl built chain files 
crossmap_py2.7 ❯  wget http://ftp.ensembl.org/pub/assembly_mapping/homo_sapiens/GRCh37_to_GRCh38.chain.gz   
# add chr to GRCh38 chromosome and save as GRCh37_to_GRCh38.edit.chain
crossmap_py2.7 ❯  CrossMap.py vcf GRCh37_to_GRCh38.edit.chain ukb22418_cALL_b0_v3.vcf.gz ../../reference/GRCh38_full_analysis_set_plus_decoy_hla.fa ukb22418_cALL_b0_v3.hg38.vcf
@ 2022-04-13 16:25:54: Read chain_file:  GRCh37_to_GRCh38.edit.chain
@ 2022-04-13 16:25:54: Updating contig field ...
@ 2022-04-13 17:56:33: Total entries: 784256
@ 2022-04-13 17:56:33: Failed to map: 99733
## (4) measure concordance with snpsift (only uncompressed vcf as input)
 java -Xmx100g -jar /ssd-data/workspace/support/tool/snpEff_180608_v4.3t/snpEff/SnpSift.jar concordance -v ukb23155_b0_v9.chr6.aa.vcf genotype_data/ukb22418_cALL_b0_v5.hg38.chr6.aa.vcf  > ./concordance/concordance.chr6.aa.txt &  java -Xmx100g -jar /ssd-data/workspace/support/tool/snpEff_180608_v4.3t/snpEff/SnpSift.jar concordance -v ukb23155_b0_v9.chr6.ab.vcf genotype_data/ukb22418_cALL_b0_v5.hg38.chr6.ab.vcf  > ./concordance/concordance.chr6.ab.txt &  java -Xmx100g -jar /ssd-data/workspace/support/tool/snpEff_180608_v4.3t/snpEff/SnpSift.jar concordance -v ukb23155_b0_v9.chr6.ac.vcf genotype_data/ukb22418_cALL_b0_v5.hg38.chr6.ac.vcf  > ./concordance/concordance.chr6.ac.txt &  java -Xmx100g -jar /ssd-data/workspace/support/tool/snpEff_180608_v4.3t/snpEff/SnpSift.jar concordance -v ukb23155_b0_v9.chr6.ad.vcf genotype_data/ukb22418_cALL_b0_v5.hg38.chr6.ad.vcf  > ./concordance/concordance.chr6.ad.txt &  java -Xmx100g -jar /ssd-data/workspace/support/tool/snpEff_180608_v4.3t/snpEff/SnpSift.jar concordance -v ukb23155_b0_v9.chr6.ae.vcf genotype_data/ukb22418_cALL_b0_v5.hg38.chr6.ae.vcf  > ./concordance/concordance.chr6.ae.txt
~~~
- lifover using picard function -> GC head memory error
~~~bashscript
## (1) make reference dictionary
java -jar /ssd-data/workspace/support/tool/picard_2.25.0/picard.jar CreateSequenceDictionary R=GRCh38_full_analysis_set_plus_decoy_hla.fa O=GRCh38_full_analysis_set_plus_decoy_hla.dict
## (2) download chain in /ssd-data/workspace/support/annotation/liftover
rsync -avzP rsync://hgdownload.cse.ucsc.edu/goldenPath/hg19/liftOver/hg19ToHg38.over.chain.gz .
## (3) run liftover
java -Xmx80g -jar /ssd-data/workspace/support/tool/picard_2.25.0/picard.jar LiftoverVcf \
I=ukb22418_c22_b0_v3.vcf.gz \
O=ukb22418_c22_b0_v3.hg38.vcf.gz \
CHAIN=/ssd-data/workspace/support/annotation/liftover/hg19ToHg38.over.chain \
REJECT=ukb22418_c22_b0_v3.hg38reject.vcf \
R=../../reference/GRCh38_full_analysis_set_plus_decoy_hla.fa  
~~~

## additional marker QC
- filter variants by hwe p value 1e-15
~~~bashscript
/ssd-data/workspace/support/tool/plink-1.9/plink --bfile ukb23155_b0_v9 --hwe 1e-15 --make-bed --out ukb23155_cALL_b0_v10
~~~
