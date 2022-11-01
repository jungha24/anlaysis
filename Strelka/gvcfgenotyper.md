- pull gvcfgenotyper image from biocontainer 
~~~bashscript
# very first time
docker pull quay.io/biocontainers/gvcfgenotyper:2019.02.26--h468198e_2
docker run -v /home/mchoilab_dell/dell_drobo/project_jhl/20210622_covid_sceqtl_JH/GT_processing:/data -v /ssd-data/workspace/:/workspace/ -v /home/mchoilab_dell/dell_drobo/COVID19/COVID19_v2/WGS/:/raw/  -it --user $(id -u):$(id -g) --name strelka_gvcfgenotyper_jhl quay.io/biocontainers/gvcfgenotyper:2019.02.26--h468198e_2 /bin/bash
# 
docker start strelka_gvcfgenotyper_jhl
docker exec -it strelka_gvcfgenotyper_jhl /bin/bash
~~~

- running
- https://github.com/Illumina/gvcfgenotyper
~~~bashscript
# make 'gvcfs.txt' file in docker tty
cd /data/20221101_strelka_gvcf_process
find ../../raw/ -name '*.strelka.genomic.vcf.gz' > gvcfs.txt
# run gvcfgenotyper
gvcfgenotyper -l gvcfs.txt -r chr21 -f ../reference/GCA_000001405.15_GRCh38_no_alt_plus_hs38d1_analysis_set.fna -Oz -o covid19_v2.strelka.variants.chr21.vcf.gz

for i in 22 X; do echo -r chr${i} -f ../reference/GCA_000001405.15_GRCh38_no_alt_plus_hs38d1_analysis_set.fna -l gvcfs.txt -Oz -o covid19_v2.strelka.variants.${i}.vcf.gz; done | xargs -i -P22 bash -c "gvcfgenotyper {}"
mv covid19_v2.strelka.variants.22.vcf.gz covid19_v2.strelka.variants.chr22.vcf.gz
mv covid19_v2.strelka.variants.X.vcf.gz covid19_v2.strelka.variants.chrX.vcf.gz
~~~
- run bash script (run_gvcfgenotype.sh)
~~~bashscript
#!/bin/bash

while IFS ="	" read -r chr start end
do
	echo -r ${chr}:${start}-${end} -f ../reference/GCA_000001405.15_GRCh38_no_alt_plus_hs38d1_analysis_set.fna -l gvcfs.txt -Oz -o covid19_v2.strelka.variants.${chr}_${start}_${end}.vcf.gz
done < interval_aa | xarg -i -P30 bash -c "gvcfgenotyper {}"#!/bin/bash

while IFS ="	" read -r chr start end
do
	echo -r ${chr}:${start}-${end} -f ../reference/GCA_000001405.15_GRCh38_no_alt_plus_hs38d1_analysis_set.fna -l gvcfs.txt -Oz -o covid19_v2.strelka.variants.${chr}_${start}_${end}.vcf.gz
done < interval_aa | xarg -i -P30 bash -c "gvcfgenotyper {}"
~~~
