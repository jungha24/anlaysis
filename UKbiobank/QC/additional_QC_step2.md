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
/ssd-data/workspace/support/tool/plink2/plink2 --bfile ukb23155_cALL_b0_v5 --make-king-table --out ukb23155_cALL_b0_v5
~~~

