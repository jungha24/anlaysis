### start from vcf with VQSR annotation
##### follow filtering critera by refering to 'https://www.cell.com/cell-reports/pdf/S2211-1247(20)30367-3.pdf' 
* remain: VQSR PASS variants
* exclude: low complexity regions 
* exclude: non-canonical chromosomes
* exclude: indel > 50bp
* exclude: SNV with AB > 0.78 or AB < 0.22 
* exclude: indel with AB > 0.8 or AB < 0.2
* filtering: rm duplicates, biallelic-only, geno 0.05, maf 0.05, hwe p-val 1e-5
* filter samples
[1] left GATK VQSR PASS variants only
~~~bashscript
bcftools view -f PASS snp.recalibrated.vcf.gz > merged.vqsr.vcf
bgzip -c merged.vqsr.vcf > merged.vqsr.vcf.gz
~~~
[2] exclude variants overlapping with low complexity regions
- use https://github.com/lh3/varcmp/blob/master/scripts/LCR-hg38.bed.gz (Heng Li, "Toward better understanding of artifacts in variant calling from high-coverage samples", Bioinformatics(2014)
~~~bashscript
vcftools --gzvcf merged.vqsr.vcf.gz --exclude-bed /ssd-data/workspace/support/annotation/LCR-hs38.bed  --recode --recode-INFO-all --stdout | bgzip > merged.vqsr.lcr.vcf.gz
~~~
[3] exclude variants on non-canonical chromosomes (decoy chromosome and contig)
~~~bashscript
vcftools --gzvcf merged.vqsr.lcr.vcf.gz --chr chr1 --chr chr2 --chr chr3 --chr chr4 --chr chr5 --chr chr6 --chr chr7 --chr chr8 --chr chr9 --chr chr10 --chr chr11 --chr chr12 --chr chr13 --chr chr14 --chr chr15 --chr chr16 --chr chr17 --chr chr18 --chr chr19 --chr chr20 --chr chr21 --chr chr22 --chr chrX --chr chrY --recode --out merged.vqsr.lcr.chr.vcf.gz
~~~
[4] exclude indel variants by size
~~~bashscript
/ssd-data/workspace/support/tool/gatk-4.1.6.0/gatk SelectVariants -V merged.vqsr.lcr.chr.vcf.gz -select-type INDEL --max-indel-size 50 -O merged.vqsr.lcr.chr.indel.size.vcf.gz
~~~
[5] exclude variants by allelic balance (SNV with AB > 0.78 or AB < 0.22, indel with AB > 0.8 or AB < 0.2)
~~~bashscript
#snp
/ssd-data/workspace/support/tool/gatk-4.1.6.0/gatk SelectVariants -V merged.vqsr.lcr.chr.vcf.gz -select-type SNP -O merged.vqsr.lcr.chr.snp.vcf.gz 
java -jar /ssd-data/workspace/support/tool/picard_2.25.0/picard.jar FilterVcf I=merged.vqsr.lcr.chr.snp.vcf.gz O=merged.vqsr.lcr.chr.snp.ab.vcf.gz MIN_AB=0.22
/ssd-data/workspace/support/tool/gatk-4.1.6.0/gatk IndexFeatureFile -I merged.vqsr.lcr.chr.snp.ab.vcf.gz
bcftools view -f PASS merged.vqsr.lcr.chr.snp.ab.vcf.gz > merged.vqsr.lcr.chr.snp.abpass.vcf
bgzip -c merged.vqsr.lcr.chr.snp.abpass.vcf > merged.vqsr.lcr.chr.snp.abpass.vcf.gz
#indel
java -jar /ssd-data/workspace/support/tool/picard_2.25.0/picard.jar FilterVcf I=merged.vqsr.lcr.chr.indel.size.vcf.gz O=merged.vqsr.lcr.chr.indel.size.ab.vcf.gz MIN_AB=0.2
/ssd-data/workspace/support/tool/gatk-4.1.6.0/gatk IndexFeatureFile -I merged.vqsr.lcr.chr.indel.size.ab.vcf.gz
bcftools view -f PASS merged.vqsr.lcr.chr.indel.size.ab.vcf.gz > merged.vqsr.lcr.chr.indel.size.abpass.vcf
bgzip -c merged.vqsr.lcr.chr.indel.size.abpass.vcf > merged.vqsr.lcr.chr.indel.size.abpass.vcf.gz

#merge
java -jar /ssd-data/workspace/support/tool/picard_2.25.0/picard.jar MergeVcfs I=merged.vqsr.lcr.chr.snp.abpass.vcf.gz I=merged.vqsr.lcr.chr.indel.size.abpass.vcf.gz O=merged.qc1.vcf.gz
~~~
[6] removes duplicates, remain biallelic-only, geno 0.05, maf 0.05, hwe p-val 1e-5
~~~bashscript
/ssd-data/workspace/support/tool/plink2/plink2 \
  --vcf merged.qc1.vcf.gz \
  --rm-dup exclude-all \ #not sure about the mode "exclude-all"
  --max-alleles 2 --min-alleles 2\
  --geno 0.05 \
  --maf 0.05 \
  --hwe 1e-5 \
  --recode vcf bgz --keep-allele-order --out merged.qc2_2
~~~
[7] filter individuals throung peddy or manually with plink
- using peddy
~~~bashscript
# generage ped file
/ssd-data/workspace/support/tool/plink-1.9/plink --vcf merged.qc2_2.vcf.gz --recode --out merged.qc2_2
## install peddy
#conda activate peddy_py3.7
#conda install -y peddy
conda activate hail_py3.7
peddy -p 4 --plot --prefix merged.qc2_2 merged.qc2_2.vcf.gz merged.qc2_2.ped
~~~
- using plink
~~~bashscript
# sexcheck
/ssd-data/workspace/support/tool/plink-1.9/plink --bfile merged.qc2_2 --check-sex --out merged.qc2_2 #merged.qc2_2.sexcheck
/ssd-data/workspace/support/tool/plink-1.9/plink --bfile merged.qc2_2 --remove-fam remove_checksex.txt --make-bed --out merged.qc3_1
# missing
/ssd-data/workspace/support/tool/plink-1.9/plink --bfile merged.qc3_1 --mind 0.05 --make-bed --out merged.qc3_2
# relatedness
/ssd-data/workspace/support/tool/plink2/plink2 --bfile merged.qc3_2 --king-cutoff 0.177 --out merged.qc3_2 #merged.qc3_2.king.cutoff.out.id, merged.qc3_2.king.cutoff.in.id
/ssd-data/workspace/support/tool/plink2/plink2 --bfile merged.qc3_2 --make-king-table --out merged.qc3_2
/ssd-data/workspace/support/tool/plink-1.9/plink --bfile merged.qc3_2 --remove-fam merged.qc3_2.king.cutoff.out.id --make-bed --out merged.qc3_3
# run pca
/ssd-data/workspace/support/tool/plink-1.9/plink --bfile merged.qc3_3 --pca 10 --out merged.qc3_3 #merged.qc3_3.eigenval, merged.qc3_3.eigenvec
#draw pca with 1000g&kova
/ssd-data/workspace/support/tool/plink2/plink2 --bfile merged.qc3_3 --ref-from-fa ./reference/GCA_000001405.15_GRCh38_no_alt_plus_hs38d1_analysis_set.fna --recode vcf --out merged.qc3_3
bgzip -c  merged.qc3_3.vcf >  merged.qc3_3.vcf.gz
bcftools annotate --rename-chrs chr_name_conv.txt merged.qc3_3.vcf.gz -Oz -o merged.qc3_3.chr.vcf.gz
  #there was no 'chr'. so i added 'chr' to find out overlapping variant from 1000g_kova vcf
bcftools isec -p kova2_1000g_covid -Oz 20220303_kova_kg_GSAarray.vcf.bgz merged.qc3_3.chr.vcf.gz
bcftools merge ./kova2_1000g_covid/0002.vcf.gz ./kova2_1000g_covid/0003.vcf.gz -Oz -o 20220303_kova_kg_GSAarray_merged.qc3_3.chr.vcf.gz
  # 0002.vcf.gz : records from 20220303_kova_kg_GSAarray.vcf.bgz shared by both
  # 003.vcf.gz : records from merged.qc3_3.chr.vcf.gz shared by bot
/ssd-data/workspace/support/tool/plink-1.9/plink --vcf 20220303_kova_kg_GSAarray_merged.qc3_3.chr.vcf.gz --const-fid 0 --make-bed --out 20220303_kova_kg_GSAarray_merged.qc3_3.chr 
  #'_' in sample name makes error, since plink use '_' as deliminator 
  #Error: Multiple instances of '_' in sample ID. If you do not want '_' to be treated as a FID/IID delimiter, use --double-id or --const-fid to choose a different method of converting VCF sample IDs to PLINK IDs, or --id-delim to change the FID/IID delimiter.
/ssd-data/workspace/support/tool/plink-1.9/plink --bfile 20220303_kova_kg_GSAarray_merged.qc3_3.chr --pca 10 --out 20220303_kova_kg_GSAarray_merged.qc3_3.chr
~~~
[8] variant calling (annotation)
~~~bashscript
java -Xmx30g -jar /ssd-data/workspace/support/tool/snpEff_180608_v4.3t/snpEff/snpEff.jar -verbose GRCh38.86 merged.qc3_3.vcf.gz | bgzip -c > merged.qc3_3.snpeff.vcf.gz  
~~~
