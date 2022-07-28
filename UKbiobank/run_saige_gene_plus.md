- https://saigegit.github.io//SAIGE-doc/
0. install (Docker)
~~~bashscript
docker pull wzhou88/saige:1.1.3
~~~
1. execute in pseudo-TTY
~~~bashscript
docker run -v /home/mchoilab_dell/dell_drobo/project_jhl/20210121_GABBR2_UKB_JH/20220403_analysis:/data -it --user root --name saigegeneplus_jhl wzhou88/saige:1.1.3 /bin/bash
~~~

2. prepare input files
- pruned genotype data 
  * for creating sparse GRM
  * for step0
~~~bashscript
plink --bfile ukb23155_cALL_b0_v4 --indep-pairwise 500 10 0.2 --out ukb23155_cALL_b0_v5
~~~
- markers falling in 2 MAC categories (MAC>=20, 10<=MAC<20)
  * for step1
~~~bashscript
~~~
- phenotype file
  * for step1, 2
  * sample id, covariates (age, sex), phenotypes (delimited by \s)
- variants of interest 
~~~bashscript
plink --bfile ../ukb23155_cALL_b0_v10 --extract range region.txt --make-bed --out ukb23155_cALL_b0_v10_adgrl2
~~~
