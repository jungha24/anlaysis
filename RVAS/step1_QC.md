## Pruning individuals and markers from 200K UK Biobank exome data
* Data was provided in plink and pVCF format. 
* No variant- or sample-level filters were pre-applied to the pVCF or PLINK files.

#### [1] filter individuals
* input file: ukb23155_cALL_b0_v1 (plink format)
~~~bashscript
# sex-check
/plink-1.9/plink \
  --bfile ukb23155_cALL_b0_v1 \
  --check-sex \
  --out ukb23155_cALL_b0_v1-merge_sexcheck
#het
/plink-1.9/plink \
  --bfile ukb23155_cALL_b0_v1 \
  --het \
  --out ukb23155_cALL_b0_v1-merg_het
#plink2-king
/plink2/plink2 \
  --bfile ukb23155_cALL_b0_v1 \
  --king-cutoff 0.177 \
  --out ukb23155_cALL_b0_v1-merge_king
## merge sample ids which were not satisfying each filtering cutoff. -> kb23155_cALL_b0_v1-merge_sexcheck_het_king.bad_fid.txt

# filtering by sex/heterogenity/kinship 
/plink-1.9/plink \
  --bfile ukb23155_cALL_b0_v1 \
  --remove-fam ukb23155_cALL_b0_v1-merge_sexcheck_het_king.bad_fid.txt \
  --make-bed \
  --out ukb23155_cALL_b0_v2
~~~

#### [2] filter individuals 2 - peddy
* input file: ukb23155_cALL_b0_v2 (plink format)
* generate temperary plink file for peddy 
* use peddy for population stratification
~~~bashscript
# use common variants
/plink-1.9/plink --bfile ukb23155_cALL_b0_v2 --maf 0.05 --make-bed --out ukb23155_cALL_b0_v3
# use variants under missingness 10%
/plink-1.9/plink --bfile ukb23155_cALL_b0_v3 --geno 0.1 --make-bed --out ukb23155_cALL_b0_v4
# use prunned variants
/plink-1.9/plink --bfile ukb23155_cALL_b0_v4 --indep-pairwise 500 10 0.2 --out ukb23155_cALL_b0_v5
/plink-1.9/plink --bfile ukb23155_cALL_b0_v4 --extract ukb23155_cALL_b0_v5.prune.in --make-bed --out ukb23155_cALL_b0_v5
# convert to vcf (required format of peddy)
/plink-1.9/plink --bfile ukb23155_cALL_b0_v5 --recode vcf --out ukb23155_cALL_b0_v5
bgzip -c ukb23155_cALL_b0_v5.vcf >ukb23155_cALL_b0_v5.vcf.gz
tabix -p vcf ukb23155_cALL_b0_v5.vcf.gz
~~~
