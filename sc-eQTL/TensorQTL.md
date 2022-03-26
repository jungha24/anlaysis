## tensorqtl
#### input
* bed file for expression phenotype
* covariate file
* genotype file with plink binary foramt

### executive
* use docker 
* generate docker-compose.yml and Dockerfile
~~~bashscript
docker build -t jhl-tensorqtl
docker-compose up -d
docker exec -it jhl-tensorqtl /bin/bash
root@e0e452373402: python3 -m tensorqtl ../GT_processing/20220323_output/merged.m1.maf0.05.clump0.9.v2 ./phenotype_files/220324_COVID_CD4T_M1_v2.bed.gz output_220326/m1.maf0.05.clump0.9.cd4t --covariates covariate_files/m1_covariate.txt --mode cis
~~~
