# additional QC of pVCF from 200K 

#### starting point
* field 23155 (200k exome PLINK format - concated for all chromosome)
* qc fail list from (additional_QC_step1.md)


## marker QC
- remain QC pass variants from raw plink
### 1. remove variants 
~~~bashscript
/ssd-data/workspace/support/tool/plink2/plink2 --bfile ukb23155_cALL_b0_v1 --set-all-var-ids @:#:\$r:\$a --new-id-max-allele-len 112 --make-bed --out ukb23155_cALL_b0_v2
plink --bfile ukb23155_cALL_b0_v1 --extract /home/mchoilab_dell/dell_drobo/project_jhl/20210121_GABBR2_UKB_JH/20220403_analysis/pvcf_qc_fail_all.txt --make-bed --out /home/mchoilab_dell/dell_drobo/project_jhl/20210121_GABBR2_UKB_JH/20220403_analysis/ukb23155_cALL_b0_v2
~~~
