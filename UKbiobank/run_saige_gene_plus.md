0. install (Docker)
~~~bashscript
docker pull wzhou88/saige:1.1.3
~~~
1. execute in pseudo-TTY
~~~bashscript
docker run -v /home/mchoilab_dell/dell_drobo/project_jhl/20210121_GABBR2_UKB_JH/20220403_analysis:/data -it --user root --name saigegeneplus_jhl wzhou88/saige:1.1.3 /bin/bash
~~~

2. create sparse GRM
~~~bashscript
/ssd-data/workspace/support/tool/plink-1.9/plink --bfile ukb23155_cALL_b0_v4 --indep-pairwise 500 10 0.2 --out ukb23155_cALL_b0_v5
~~~
