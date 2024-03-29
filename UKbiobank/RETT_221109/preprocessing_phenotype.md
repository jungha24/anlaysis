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
    - <1> : csv file, each row is a participant, first column contains the user id and remaining columns are phenotypes, each variable name is in the format 'x[varid]_[instance]_[array]' */home/mchoilab_dell/dell_drobo/project_jhl/20210121_GABBR2_UKB_JH/phenotype/field_of_interest_221109.headeredit.csv*
    ~~~bashscript
    ./ukbconv ukb45036.enc_ukb csv -i20220403_analysis/20221107_rett/field_of_interest.txt -ophenotype/field_of_interest_221111
    # edit header to x[varid]_[instance]_[array]
    head -n 1 field_of_interest_221111.csv > field_of_interest_221111.header.csv
    vi field_of_interest_221111.header.csv
      :%s/eid/userId/g
      :%s/","/","x/g
      :%s/[.]/_/g
      :%s/-/_/g
    tail -n +2 -q field_of_interest_221111.csv > field_of_interest_221111.noheader.csv
    cat field_of_interest_221111.header.csv field_of_interest_221111.noheader.csv > field_of_interest_221111.headeredit.csv 
    ~~~
    - <2> : tsv file, contain information about each phenotype */Users/jeongha/Dropbox/JH/2022/ukbiobank/RTT_221031/phesant_221110/outcome-info_221110.tsv*
    ~~~bashscript
    wget variable-info/outcome_info_final_round3.tsv .
    # curate the format and edit the TRAIT_OF_INTEREST and EXCLUDED in R
    # ignore Cat1_ID, Cat2_ID
    ~~~
    - <3> : csv file, containing information about data codings */Users/jeongha/Dropbox/JH/2022/ukbiobank/RTT_221031/PHESANT-master/variable-info/data-coding-ordinal-info-nov2019-update.txt*
    ~~~bashscript
    wget variable-info/data-coding-ordinal-info-nov2019-update.txt .
    ~~~
    - <4> : directory where u want to the results to be stored
    ~~~bashscript
    mkdir results
    ~~~
    - <5> : the colume name with participant ids in <1> input file. *"userId"* 
    - therefor ...
    ~~~bashscript
    docker exec -it --user $(id -u):$(id -g) jhl_r /bin/bash
    cd /mnt/data/phesant/PHESANT-master/WAS
    raw_pheno_dir="/mnt/pheno/"
    Dir="/mnt/data/phesant/"
    Rscript phenomeScan.r --phenofile="${raw_pheno_dir}field_of_interest_221111.headeredit.csv" --variablelistfile="${Dir}data/outcome-info_221110.tsv" --datacodingfile="${Dir}data/data-coding-ordinal-info-nov2019-update.txt" --resDir="${Dir}results/" --userId="userId"
    ~~~
