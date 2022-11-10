1. curate phenotype file for SAIGE GENE manually
  - download phenotype of interest
  ~~~bashscript
  #/home/mchoilab_dell/dell_drobo/project_jhl/20210121_GABBR2_UKB_JH
  ./ukbconv ukb45036.enc_ukb r -i20220403_analysis/20221107_rett/quant_field.txt -ophenotype/quant_field_221107
  ./ukbconv ukb45036.enc_ukb r -i20220403_analysis/20221107_rett/binary_field.txt -ophenotype/binary_field_221107
  #'binary_field_221107.r' and 'binary_field_221107.tab' were generated in phenotype folder
  ~~~
2. use PHESANT(https://github.com/astheeggeggs/PHESANT)
  - command
  ~~~bashscript
  Rscript phenomeScan.r --phenofile=<1> --variablelistfile=<2> --datacodingfile=<3> --resDir=<4> --userID=<5>
  ~~~
  - input:
    - <1> : csv file, each row is a participant, first column contains the user id and remaining columns are phenotypes, each variable name is in the format 'x[varid]_[instance]_[array]'
    ~~~bashscript
    ./ukbconv ukb45036.enc_ukb csv -i20220403_analysis/20221107_rett/field_of_interest.txt -ophenotype/field_of_interest_221109
    ~~~
    - <2> : tsv file, contain information about each phenotype 
