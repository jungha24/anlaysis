0. apply quanlifying variants
- add gnomad

~~~bashscript
# extract RTT region
plink --bfile ukb23155_b0_v9 --extract range RTTgene_hg38.bed --recode vcf-iid bgz --keep-allele-order --out ukb23155_b0_v9.rtt.vcf.gz
# rename chromosome name
bcftools annotate --rename-chrs chr_name_conv.txt ukb23155_b0_v9.rtt.vcf.gz -Oz -o ukb23155_b0_v9.rtt.chr.vcf.gz
# liftover to hg19 is required
java -Xmx50g -jar /ssd-data/workspace/support/tool/picard_2.25.0/picard.jar LiftoverVcf \
I=ukb23155_b0_v9.rtt.chr.vcf.gz \
O=ukb23155_b0_v9.rtt.chr.hg19.vcf.gz \
CHAIN=/ssd-data/workspace/support/annotation/liftover/hg38ToHg19.over.chain \
REJECT=ukb23155_b0_v9.rtt.chr.hg19reject.vcf \
R=/ssd-data/workspace/support/annotation/liftover/hg19.fa
# add gnomad
./vep --cache --dir_cache  ../ensembl-vep-cache/homo_sapiens -i /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.vcf --port 3337 --af_gnomad --vcf --o /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.gnomadaf.vcf
	## make tsv
	echo -e "CHROM\tPOS\tID\tREF\tALT\t$(../bcftools-1.13/bcftools +split-vep -l /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.gnomadaf.vcf | cut -f 2 | tr '\n' '\t' | sed 's/\t$//')" > /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.gnomadaf.tsv
	../bcftools-1.13/bcftools +split-vep -f '%CHROM\t%POS\t%ID\t%REF\t%ALT\t%CSQ\n' -d -A tab /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.gnomadaf.vcf >> /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.gnomadaf.tsv

# add AF
export BCFTOOLS_PLUGINS=/Users/choimacpro2/Support/software/bcftools-1.13/plugins
/Users/choimacpro2/Support/software/bcftools-1.13/bcftools +setGT ukb23155_b0_v9.rtt.chr.hg19.gnomad.vcf -Oz -o ukb23155_b0_v9.rtt.chr.hg19.setgt.vcf.gz -- -t . -n 0
/Users/choimacpro2/Support/software/bcftools-1.13/bcftools +fill-tags ukb23155_b0_v9.rtt.chr.hg19.setgt.vcf.gz -Oz -o ukb23155_b0_v9.rtt.chr.hg19.setgt.af.vcf.gz -- -t AF,AN,AC,AC_Hom,AC_Het,MAF,NS
# add revel
./vep --database -i /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.vcf --plugin REVEL,/Users/choimacpro2/Support/software/ensembl-vep-plugins/new_tabbed_revel.tsv.gz --vcf --o /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.revel.vcf --port 3337

	## make tsv
	echo -e "CHROM\tPOS\tID\tREF\tALT\t$(../bcftools-1.13/bcftools +split-vep -l /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.revel.vcf | cut -f 2 | tr '\n' '\t' | sed 's/\t$//')" > /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.revel.tsv
	../bcftools-1.13/bcftools +split-vep -f '%CHROM\t%POS\t%ID\t%REF\t%ALT\t%CSQ\n' -d -A tab /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.revel.vcf >> /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.revel.tsv
	
# add MTR
wget http://biosig.unimelb.edu.au/mtr-viewer/static/mtrflatfile_2.0.txt.gz
gunzip mtrflatfile_2.0.txt.gz
sed '1s/.*/#&/' mtrflatfile_2.0.txt > new_mtrflatfile_2.0.txt
bgzip new_mtrflatfile_2.0.txt
tabix -f -s 1 -b 2 -e 2 new_mtrflatfile_2.0.txt.gz
./vep --database -i /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.vcf --plugin MTR,/Users/choimacpro2/Support/software/ensembl-vep-plugins/new_mtrflatfile_2.0.txt.gz --vcf --o /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.MTR.vcf --port 3337
	## make tsv
	echo -e "CHROM\tPOS\tID\tREF\tALT\t$(../bcftools-1.13/bcftools +split-vep -l /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.MTR.vcf | cut -f 2 | tr '\n' '\t' | sed 's/\t$//')" > /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.MTR.tsv
	../bcftools-1.13/bcftools +split-vep -f '%CHROM\t%POS\t%ID\t%REF\t%ALT\t%CSQ\n' -d -A tab /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.MTR.vcf >> /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.MTR.tsv
	
# annotate snpeff
 java -Xmx30g -jar /Users/choimacpro2/Support/software/snpEff/snpEff.jar hg19 -canon ukb23155_b0_v9.rtt.chr.hg19.setgt.af.vcf | bgzip > ukb23155_b0_v9.rtt.chr.hg19.setgt.af.snpeff.vcf.gz
 
	 ## make tsv
	echo -e "CHROM\tPOS\tID\tREF\tALT\tNS\tAN\tAF\tMAF\tAC\tAC_Het\tAC_Hom\t$(../bcftools-1.13/bcftools +split-vep -l /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.snpeff.vcf | cut -f 2 | tr '\n' '\t' | sed 's/\t$//')" > /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.snpeff.tsv
	../bcftools-1.13/bcftools +split-vep -f '%CHROM\t%POS\t%ID\t%REF\t%ALT\t%INFO/NS\t%INFO/AN\t%INFO/AF\t%INFO/MAF\t%INFO/AC\t%INFO/AC_Het\t%INFO/AC_Hom\t%CSQ\n' -d -A tab /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.snpeff.vcf >> /Volumes/choi_Drobo5D_Alz2/Projects_JH/20220424_ukb/ukb23155_b0_v9.rtt.chr.hg19.setgt.af.snpeff.tsv
~~~
2. run saige-gene

~~~bashscript
conda activate saige
#conda create -n saige0.42 -c conda-forge -c bioconda -y r-base=4.0 r-saige=0.42 savvy=1.3.0
# there is no SKAT
### use docker
docker run -v /home/mchoilab_dell/dell_drobo/project_jhl/20210121_GABBR2_UKB_JH:/data -it --user root --name SAIGE-GENEjh2 wzhou88/saige:0.44.6.5 /bin/bash
~~~

~~~bashscript
plink --bfile ukb23155_b0_v9 --maf 0.05 --make-bed --out ukb23155_b0_v9.common
plink --bfile ukb23155_b0_v9 --maf 0.01 --make-bed --out ukb23155_b0_v9.common.01
plink --bfile ukb23155_b0_v9 --extract range RTTgene_hg38.bed --make-bed --out ukb23155_b0_v9.rtt
plink --bfile ukb23155_b0_v9.common --bmerge ukb23155_b0_v9.rtt --make-bed --out ukb23155_b0_v9.common.rtt
plink --bfile ukb23155_b0_v9.common.rtt --bmerge ukb23155_b0_v9.chr22 --make-bed --out ukb23155_b0_v9.common.rtt.chr22
plink --bfile ukb23155_b0_v9.common.rtt.chr22 --not-chr 23 --make-bed --out ukb23155_b0_v9.common.rtt.chr22.auto #error
createSparseGRM.R --plinkFile=ukb23155_b0_v9.common.rtt.chr22.auto --nThreads=8 --outputPrefix=./saige-gene/output/sparseGRM.v9.common.rtt.chr22.auto --numRandomMarkerforSparseKin=2000 --relatednessCutoff=0.125
# no sex chromosome
# require more than 30 genetic variants about various MAC range
# include rare variants to analysis
~~~

~~~bashscript

step1_fitNULLGLMM.R \
        --plinkFile=ukb23155_b0_v9.common.rtt.chr22.auto \
        --phenoFile=saige-gene/input/example.txt \
        --phenoCol=y_binary \
        --covarColList=x1,x2 \
        --sampleIDColinphenoFile=IID \
        --traitType=binary       \
        --outputPrefix=saige-gene/output/v9.common.rtt.chr22.auto.example_binary \
        --sparseGRMFile=saige-gene/output/sparseGRM.v9.common.rtt.chr22.auto_relatednessCutoff_0.125_2000_randomMarkersUsed.sparseGRM.mtx \
        --sparseGRMSampleIDFile=saige-gene/output/sparseGRM.v9.common.rtt.chr22.auto_relatednessCutoff_0.125_2000_randomMarkersUsed.sparseGRM.mtx.sampleIDs.txt \
        --nThreads=10 \
        --LOCO=FALSE    \
        --skipModelFitting=FALSE \
        --IsSparseKin=TRUE      \
        --isCateVarianceRatio=TRUE
~~~

~~~bashscript
vcftools --gzvcf ukb23155_b0_v9.rtt.vcf.gz --snps saige-gene/input/cdkl5.revel.gnomad.rare.d.txt --keep-INFO-all --recode --stdout | bgzip > saige-gene/input/ukb23155_b0_v9.rtt.cdkl5.rare.d.vcf.gz
tabix -p vcf ukb23155_b0_v9.rtt.gabbr2.rare.d.vcf.gz
tabix -C ukb23155_b0_v9.rtt.gabbr2.rare.d.vcf.gz
~~~

~~~bashscript

step2_SPAtests.R --vcfFile=ukb23155_b0_v9.rtt.vcf.gz --vcfFileIndex=ukb23155_b0_v9.rtt.vcf.gz.tbi --vcfField=GT --chrom=9 --minMAF=0 --minMAC=0.5 --maxMAFforGroupTest=0.01 --GMMATmodelFile=saige-gene/output/v9.common.rtt.chr22.auto.example_binary.rda --varianceRatioFile=saige-gene/output/v9.common.rtt.chr22.auto.example_binary.varianceRatio.txt --SAIGEOutputFile=saige-gene/output/v9.common.rtt.chr22.auto.example_binary.SAIGE.gabbr2.txt --numLinesOutput=1 --groupFile=saige-gene/input/gabbr2_groupfile.txt --sparseSigmaFile=saige-gene/output/v9.common.rtt.chr22.auto.example_binary.varianceRatio.txt_relatednessCutoff_0.125_2000_randomMarkersUsed.sparseSigma.mtx  --IsSingleVarinGroupTest=TRUE --IsOutputAFinCaseCtrl=TRUE --IsOutputPvalueNAinGroupTestforBinary=TRUE --IsAccountforCasecontrolImbalanceinGroupTest=TRUE --IsOutputBETASEinBurdenTest=TRUE --LOCO=FALSE
~~~
