### single cell eQTL pipeline
- starting material: gvcf files of wgs, count matrix from 10x genomics

[1] generate genotype to analysis by refering to GATK best practice
- https://github.com/jungha24/anlaysis/blob/1e8e3eb6a3baa42166eecebd6c79d7cbe5a8a577/GATK/Variant_Calling2Recalibration.md

[2] marker/sample QC
- https://github.com/jungha24/anlaysis/blob/8648ad00f2be9e2c7502528008154f5e4544ecb6/GATK/Filtering_variants.md

[3] clumping snps for reducing multiple correction test burden
- use maf information instead of p value from assoc 
- https://privefl.github.io/bigsnpr/articles/pruning-vs-clumping.html
~~~bashscript
/ssd-data/workspace/support/tool/plink2/plink2 --bfile merged.qc3_3 --set-missing-var-ids @:#:\$r:\$a --new-id-max-allele-len 51 --make-bed --out merged.qc4
/ssd-data/workspace/support/tool/plink-1.9/plink --bfile merged.qc4 --freq --out merged.qc4 #merged.qc4.frq
# run make_clumping_input.r
plink --bfile merged.qc4 --out merged.qc4_clumpr_0.2 --clump merged.qc4.frq.as.p --clump-p1 1 --clump-p2 1 --clump-r2 0.2 #240470
plink --bfile merged.qc4 --out merged.qc4_clumpr_0.5 --clump merged.qc4.frq.as.p --clump-p1 1 --clump-p2 1 --clump-r2 0.5 #484486
plink --bfile merged.qc4 --out merged.qc4_clumpr_0.8 --clump merged.qc4.frq.as.p --clump-p1 1 --clump-p2 1 --clump-r2 0.8 #857314
plink --bfile merged.qc4 --out merged.qc4_clumpr_0.9 --clump merged.qc4.frq.as.p --clump-p1 1 --clump-p2 1 --clump-r2 0.9 #1122358

awk 'NR !=1{print $3}' merged.qc4_clumpr_0.8.clumped > merged.qc4_clumpr_0.8.clumped.snp  
plink --bfile merged.qc4 --extract merged.qc4_clumpr_0.8.clumped.snp --out merged.qc4_0.8 --make-bed
~~~
