- Adding strelka's gvcf files to GenomicsDB workspace was possible (--genomicsdb-update-workspace-path). 
- But GenotypeGVCF doesn't recognize strelka's gvcf in the workspace. 
- As an alternative, 
  1. make multi-sample vcf with gvcfgenotyper (from Illumina) and do recalibration (from GATK4). - merge with gatk's variants at the very last step.
      -  make multi-sample vcf (https://github.com/jungha24/anlaysis/blob/0074978b5afbb1834aff7041afa94a434661e8b6/Strelka/gvcfgenotyper.md)
        -  loss FITER column information 
      -  do recalibration with GATK4 
        -  doesn't work
     
