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
plink --bfile ../ukb23155_cALL_b0_v10 --indep-pairwise 500 10 0.2 --out ukb23155_cALL_b0_v10_prunned
plink --bfile ../ukb23155_cALL_b0_v10 --extract ukb23155_cALL_b0_v10_prunned.prune.in --make-bed --out ukb23155_cALL_b0_v10_prune
~~~
- phenotype file
  * for step1, 2
  * sample id, covariates (age, sex), phenotypes (delimited by \s)
- variants of interest 
~~~bashscript
plink --bfile ../ukb23155_cALL_b0_v10 --extract range region.txt --make-bed --out ukb23155_cALL_b0_v10_adgrl2
~~~
- group file
- groupfile
  * 2 row for one gene
  * use annotated vcf with vep
~~~ 
geneA var rs1 rs2 rs3
geneA anno missense missense lof
~~~

3. step0. create a sparse GRM
~~~bashscript
createSparseGRM.R --plinkFile=ukb23155_cALL_b0_v10_prune --nThreads=8 --outputPrefix=./output/sparseGRM --numRandomMarkerforSparseKin=2000 --relatednessCutoff=0.125
~~~
- output file:
  * sparseGRM_relatednessCutoff_0.125_2000_randomMarkersUsed.sparseGRM.mtx
  * sparseGRM_relatednessCutoff_0.125_2000_randomMarkersUsed.sparseGRM.mtx.sampleIDs.txt

4. step1. fitting the null logistic/linear mixed model
- (optional) markers falling in 2 MAC categories (MAC>=20, 10<=MAC<20)
  * use as input of *--plinkfFile*
~~~bashscript
plink2 --bfile ../ukb23155_cALL_b0_v10 --freq counts --out ukb23155_cALL_b0_v10_count

cat <(tail -n +2 ukb23155_cALL_b0_v10_count.acount | awk '((2*$6-$5) < 20 && (2*$6-$5) >= 10) || ($5 < 20 && $5 >= 10) {print $2}' | shuf -n 1000) \
<(tail -n +2 ukb23155_cALL_b0_v10_count.acount | awk ' $5 >= 20 && (2*$6-$5)>= 20 {print $2}' | shuf -n 1000) > ukb23155_cALL_b0_v10.forCate_vr.markerid.list

plink2 --bfile ../ukb23155_cALL_b0_v10 --extract ukb23155_cALL_b0_v10.forCate_vr.markerid.list --make-bed --out ukb23155_cALL_b0_v10.forCate_vr
~~~
- chromosomes in bim file must be numeric 
~~~bashscript
plink --bfile ukb2315z5_cALL_b0_v10.forCate_vr --update-chr change_chr.txt --make-bed --out ukb23155_cALL_b0_v10.forCate_vr_23
# only chromosome column changed. variant id column still has 'X'
~~~
- run step1_fitNULLGLMM.R
  * using pre-selected markers falling in 2 MAC categories took less time.  
~~~bashscript
# use markers falling in 2 MAC categories 
step1_fitNULLGLMM.R \
 --sparseGRMFile=output/sparseGRM_relatednessCutoff_0.125_2000_randomMarkersUsed.sparseGRM.mtx \
 --sparseGRMSampleIDFile=output/sparseGRM_relatednessCutoff_0.125_2000_randomMarkersUsed.sparseGRM.mtx.sampleIDs.txt \
 --plinkFile=ukb23155_cALL_b0_v10.forCate_vr_23 \
 --useSparseGRMtoFitNULL=TRUE \
 --phenoFile=phenofile_cat2417.txt \
 --phenoCol=binary_132466 \
 --covarColList=age,sex \
 --sampleIDColinphenoFile=eid \
 --traitType=binary \
 --isCateVarianceRatio=TRUE \
 --outputPrefix=./output/binary_132466_sparseGRM \
 --IsOverwriteVarianceRatioFile=TRUE	

# use full plink file
step1_fitNULLGLMM.R \
--sparseGRMFile=output/sparseGRM_relatednessCutoff_0.125_2000_randomMarkersUsed.sparseGRM.mtx \
--sparseGRMSampleIDFile=output/sparseGRM_relatednessCutoff_0.125_2000_randomMarkersUsed.sparseGRM.mtx.sampleIDs.txt \
--plinkFile=../ukb23155_cALL_b0_v10 \
--useSparseGRMtoFitNULL=TRUE \
--phenoFile=phenofile_cat2417.txt \
--phenoCol=binary_132466 \
--covarColList=age,sex \
--sampleIDColinphenoFile=eid \
--traitType=binary \
--isCateVarianceRatio=TRUE \
--outputPrefix=./output/binary_132466_sparseGRM_fullplink \
--IsOverwriteVarianceRatioFile=TRUE
~~~
- output file:
  * binary_132466_sparseGRM.rda
  * binary_132466_sparseGRM.varianceRatio.txt

5. step2. performing the region- or gene-based association tests
- error
~~~bashscript
Error in SAIGE.getRegionList_new(marker_group_line, nline_per_gene, annolist,  :
  Please check RegionFile: in region LPHN2: duplicated SNPs exist.
~~~
- input plink file: same result whether plink file with gene of interest or full plink file were used
- input GMMATmodelFile, varianceRatioFile: same result whether files from pre-selected markers or full plink file in step1
~~~bashscript
# group file with missense (w/o MTR)
step2_SPAtests.R \
 --bedFile=ukb23155_cALL_b0_v10_adgrl2.bed \
 --bimFile=ukb23155_cALL_b0_v10_adgrl2.bim \
 --famFile=ukb23155_cALL_b0_v10_adgrl2.fam \
 --SAIGEOutputFile=./output/ukb23155_cALL_b0_v10_adgrl2_groupTest_out.txt \
 --chrom=1 \
 --LOCO=FALSE \
 --AlleleOrder=alt-first \
 --minMAF=0 \
 --minMAC=0.5 \
 --sampleFile=samplelist.txt \
 --GMMATmodelFile=./output/binary_132466_sparseGRM.rda \
 --varianceRatioFile=./output/binary_132466_sparseGRM.varianceRatio.txt \
 --sparseGRMFile=./output/sparseGRM_relatednessCutoff_0.125_2000_randomMarkersUsed.sparseGRM.mtx \
 --sparseGRMSampleIDFile=./output/sparseGRM_relatednessCutoff_0.125_2000_randomMarkersUsed.sparseGRM.mtx.sampleIDs.txt \
 --groupFile=group_20220802.txt \
 --annotation_in_groupTest=lof,missense,synonymous,lof:missense,lof:missense:synonymous \
 --maxMAF_in_groupTest=0.00005,0.0001,0.0005,0.001,0.005,0.001

# group file with missense (w/ MTR)
step2_SPAtests.R \
 --bedFile=ukb23155_cALL_b0_v10_adgrl2.bed \
 --bimFile=ukb23155_cALL_b0_v10_adgrl2.bim \
 --famFile=ukb23155_cALL_b0_v10_adgrl2.fam \
 --SAIGEOutputFile=./output/ukb23155_cALL_b0_v10_adgrl2_groupTest_mtr_out.txt \
 --chrom=1 \
 --LOCO=FALSE \
 --AlleleOrder=alt-first \
 --minMAF=0 \
 --minMAC=0.5 \
 --sampleFile=samplelist.txt \
 --GMMATmodelFile=./output/binary_132466_sparseGRM.rda \
 --varianceRatioFile=./output/binary_132466_sparseGRM.varianceRatio.txt \
 --sparseGRMFile=./output/sparseGRM_relatednessCutoff_0.125_2000_randomMarkersUsed.sparseGRM.mtx \
 --sparseGRMSampleIDFile=./output/sparseGRM_relatednessCutoff_0.125_2000_randomMarkersUsed.sparseGRM.mtx.sampleIDs.txt \
 --groupFile=group_20220802_mtr.txt \
 --annotation_in_groupTest=lof,missensem,synonymous,lof:missensem,lof:missensem:synonymous \
 --maxMAF_in_groupTest=0.00005,0.0001,0.0005,0.001,0.005,0.001
~~~
