- Adding strelka's gvcf files to GenomicsDB workspace was possible (--genomicsdb-update-workspace-path). 
- But GenotypeGVCF doesn't recognize strelka's gvcf in the workspace. 
- As an alternative, 
  1. make multi-sample vcf with gvcfgenotyper (from Illumina) and do recalibration (from GATK4). - merge with gatk's variants at the very last step.
      -  make multi-sample vcf ()
      -  do recalibration with GATK4
      ~~~bashscript
      # generate index file of vcf
      /ssd-data/workspace/support/tool/gatk-4.1.6.0/gatk IndexFeatureFile -I covid19_v2.strelka.variants.vcf.gz
      ~~~
