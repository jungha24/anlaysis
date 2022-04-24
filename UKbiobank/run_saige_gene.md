0. apply quanlifying variants
- add gnomad

~~~bashscript
plink --bfile ukb23155_b0_v9 --extract range RTTgene_hg38.bed --recode vcf-iid bgz --keep-allele-order --out ukb23155_b0_v9.rtt.vcf.gz
 bcftools annotate --rename-chrs chr_name_conv.txt ukb23155_b0_v9.rtt.vcf.gz -Oz -o ukb23155_b0_v9.rtt.chr.vcf.gz
# liftover to hg19 is required
java -Xmx50g -jar /ssd-data/workspace/support/tool/picard_2.25.0/picard.jar LiftoverVcf \
I=ukb23155_b0_v9.rtt.chr.vcf.gz \
O=ukb23155_b0_v9.rtt.chr.hg19.vcf.gz \
CHAIN=/ssd-data/workspace/support/annotation/liftover/hg38ToHg19.over.chain \
REJECT=ukb23155_b0_v9.rtt.chr.hg19reject.vcf \
R=/ssd-data/workspace/support/annotation/liftover/hg19.fa
~~~
2. run saige-gene

~~~bashscript
conda activate saige
~~~

~~~bashscript
createSparseGRM.R --plinkFile=ukb23155_b0_v9 --nThreads=8 --outputPrefix=./saige-gene/sparseGRM.v9 --numRandomMarkerforSparseKin=2000 --relatednessCutoff=0.125
~~~

~~~bashscript
Rscript step1_fitNULLGLMM.R     \
  --plinkFile=ukb23155_b0_v9 \
  --phenoFile=/pheno_1000samples.txt_withdosages_withBothTraitTypes.txt \
        --phenoCol=y_quantitative \
        --covarColList=x1,x2 \
        --sampleIDColinphenoFile=IID \
        --traitType=quantitative       \
        --invNormalize=TRUE     \
        --outputPrefix=./output/example_quantitative \
	--outputPrefix_varRatio=./output/example_quantitative_cate	\
	--sparseGRMFile=./output/example_binary_cate.varianceRatio.txt.sparseGRM.mtx    \
        --sparseGRMSampleIDFile=./output/example_binary.varianceRatio.txt.sparseGRM.mtx.sample  \
        --nThreads=4 \
        --LOCO=FALSE	\
	--skipModelFitting=FALSE \
        --IsSparseKin=TRUE      \
        --isCateVarianceRatio=TRUE	
~~~
