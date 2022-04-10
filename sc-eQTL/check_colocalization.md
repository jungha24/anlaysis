### find overlapping covid 19 hgi GWAS hit 
- used kova (korea 2k data) for ld caluclation
~~~bashscript
# extract significant snp list from covid19 HGI (p < 5e-8)
gunzip -c COVID19_HGI_B1_ALL_leave_23andme_20210607.txt.gz | awk '$9 < 0.00000005 {print $5}' - > covid19hgi.r6.b1_all_leave_23andme.sig.list.txt
plink --vcf 20220303_kova_kg_GSAarray.vcf.gz --double-id --make-bed --out 20220303_kova_kg_GSAarray
/ssd-data/workspace/support/tool/plink2/plink2 --bfile 20220303_kova_kg_GSAarray --set-all-var-ids @:#:\$r:\$a --make-bed --out 20220303_kova_kg_GSAarray.v2

~~~
