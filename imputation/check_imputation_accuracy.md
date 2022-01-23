### objective: check the accuracy of the particular reference panel.
### plan:
1. use COVID WGS vcf files
2. extract common variants and use them as ready to analysis files
3. run imputation about common variant vcf files by using 1000G, Korea1K and KOVA2 reference panel
4. compare the concordance (R^2) between imputated variants and WGS varaints
5. assign the accuracy of our reference panl by comparing accuracy of 1000G of Korea1K

#### 1. extract common variants from WGS vcf files and convert them to oxford format
- since COVID WGS vcf files are too big to merge into one multi-sample vcf files, we extract common variants based on gnomAD AF > 0.05
- this requires us to annotate gnomad AF information to all vcf files
- decided to use hail
- use jupyter notebook

#### 2. upload the results to AWS s3 bucket and run impute2 through cromwell
- 
