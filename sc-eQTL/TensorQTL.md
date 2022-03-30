## tensorqtl
#### input
* bed file for expression phenotype
* covariate file
* genotype file with plink binary foramt

### executive
* use docker 
* generate docker-compose.yml and Dockerfile
~~~bashscript
$ docker build  -t jhl-tensorqtl
$ docker-compose up -d
$ docker exec -it jhl-tensorqtl /bin/bash
~~~
- cis-QTL mapping: permutations 
  * generates phenotype(expression)-level summary statistics with empirical p-values
  * enables calculation of genome wide FDR
~~~bashscript
root@e0e452373402: python3 -m tensorqtl ../GT_processing/20220323_output/merged.m1.maf0.05.clump0.9.v2 ./phenotype_files/220324_COVID_CD4T_M1_v2.bed.gz output_220326/m1.maf0.05.clump0.9.cd4t --covariates covariate_files/m1_covariate.txt --mode cis
~~~
- cis-QTL mapping: summary statistics for all variant-phenotype pairs
  * requires converting parquet to txt
~~~bashscript
root@e0e452373402: python3 -m tensorqtl ../GT_processing/20220323_output/merged.m1.maf0.05.clump0.9.v2 ./phenotype_files/220324_COVID_CD4T_M1_v2.bed.gz output_220326/m1.maf0.05.clump0.9.cd4t.nominal --covariates covariate_files/m1_covariate.txt --mode cis_nominal
# make and execute python file which converts parquet to text.
root@e0e452373402: for f in *.parquet; do python3 ../parquet2txt.py ${f}; done
~~~
