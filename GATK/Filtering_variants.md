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
[7] filter individuals throung peddy
~~~bashscript
# generage ped file
/ssd-data/workspace/support/tool/plink-1.9/plink --vcf merged.qc2_2.vcf.gz --recode --out merged.qc2_2
