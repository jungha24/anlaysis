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
done < interval_aa | xarg -i -P30 bash -c "gvcfgenotyper {}"

while IFS ="	" read -r chr start end
do
	echo -r ${chr}:${start}-${end} -f ../reference/GCA_000001405.15_GRCh38_no_alt_plus_hs38d1_analysis_set.fna -l gvcfs.txt -Oz -o covid19_v2.strelka.variants.${chr}_${start}_${end}.vcf.gz
done < interval_ab | xarg -i -P34 bash -c "gvcfgenotyper {}"
~~~
- gather vcf files
~~~bashscript
java -jar /ssd-data/workspace/support/tool/picard_2.25.0/picard.jar GatherVcfs I=covid19_v2.strelka.variants.chr1_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr1_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr1_100000001_150000000.vcf.gz I=covid19_v2.strelka.variants.chr1_150000001_200000000.vcf.gz I=covid19_v2.strelka.variants.chr1_200000000_250000000.vcf.gz I=covid19_v2.strelka.variants.chr2_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr2_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr2_100000001_150000000.vcf.gz I=covid19_v2.strelka.variants.chr2_150000001_200000000.vcf.gz I=covid19_v2.strelka.variants.chr2_200000000_250000000.vcf.gz I=covid19_v2.strelka.variants.chr3_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr3_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr3_100000001_150000000.vcf.gz I=covid19_v2.strelka.variants.chr3_150000001_200000000.vcf.gz I=covid19_v2.strelka.variants.chr4_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr4_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr4_100000001_150000000.vcf.gz I=covid19_v2.strelka.variants.chr4_150000001_200000000.vcf.gz I=covid19_v2.strelka.variants.chr5_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr5_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr5_100000001_150000000.vcf.gz I=covid19_v2.strelka.variants.chr5_150000001_200000000.vcf.gz I=covid19_v2.strelka.variants.chr6_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr6_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr6_100000001_150000000.vcf.gz I=covid19_v2.strelka.variants.chr6_150000001_200000000.vcf.gz I=covid19_v2.strelka.variants.chr7_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr7_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr7_100000001_150000000.vcf.gz I=covid19_v2.strelka.variants.chr7_150000001_200000000.vcf.gz I=covid19_v2.strelka.variants.chr8_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr8_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr8_100000001_150000000.vcf.gz I=covid19_v2.strelka.variants.chr9_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr9_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr9_100000001_150000000.vcf.gz I=covid19_v2.strelka.variants.chr10_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr10_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr10_100000001_150000000.vcf.gz I=covid19_v2.strelka.variants.chr11_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr11_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr11_100000001_150000000.vcf.gz I=covid19_v2.strelka.variants.chr12_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr12_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr12_100000001_150000000.vcf.gz I=covid19_v2.strelka.variants.chr13_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr13_50000001_150000000.vcf.gz I=covid19_v2.strelka.variants.chr14_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr14_50000001_150000000.vcf.gz I=covid19_v2.strelka.variants.chr15_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr15_50000001_150000000.vcf.gz I=covid19_v2.strelka.variants.chr16_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr16_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr17_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr17_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr18_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr18_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr19_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr19_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr20_1_50000000.vcf.gz I=covid19_v2.strelka.variants.chr20_50000001_100000000.vcf.gz I=covid19_v2.strelka.variants.chr21.vcf.gz I=covid19_v2.strelka.variants.chr22.vcf.gz I=covid19_v2.strelka.variants.chrX.vcf.gz O=covid19_v2.strelka.variants.vcf.gz
~~~
