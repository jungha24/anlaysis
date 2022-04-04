## How to access standard tabular data approved from UK biobank

1. fetch ukb45879.enc
~~~
1. Login to the Application Management System at https://bbams.ndph.ox.ac.uk/ams/
2. Go to the Projects section for your Application **** and click on the Data Tab then the "Go to Showcase download page" button.
3. On the Downloads page of the UKB Showcase, go to the Dataset Tab and click on the entry with ID ****;
4. Enter the MD5 checksum for the data (see below) and click Generate;
5. On the following screen, click Fetch to download the data.
~~~

2. validate the download (ukbmd5)
~~~bashscript
wget  -nd  biobank.ndph.ox.ac.uk/ukb/util/ukbmd5 
chmod 755
./ukbmd5 ukb45879.enc 
~~~
- compare the MD5 code with MD5 code provided from e-mail

3. decrypt the dataset (ukbunpack)
~~~bashscript
wget  -nd  biobank.ndph.ox.ac.uk/ukb/util/ukbunpack
chmod 755
./ukbunpack ukb45879.enc keyvalue

UKBiobank ukb_unpack_lx (c) CTSU. Compiled Mar 14 2018 14:21:31.

Attempting Unpack of "ukb45879.enc"
Password: "1...8"./gfetch 22418 -cX -ak69079r45879.key

Unpacking, 4 chunks
....
Unpack output as "ukb45879.enc_ukb"
Bytes written: 31991590
MD5 computed:  3...a
~~~
- *ukb45879.enc_ukb* is generated.

4. conversion of the dataset (ukbconv)
~~~bashscript
wget  -nd  biobank.ndph.ox.ac.uk/ukb/util/ukbconv
chmod 755 ./ukbconv
./ukbconv ukb45879.enc_ukb txt
./ukbconv ukb45879.enc_ukb docs
~~~
- 'ukb45879.txt', 'ukb45879.log', 'fields.ukb' are generated.
- various options do the following...
  - docs: generates a data dictionary for your dataset. This creates HTML document
  - csv, txt, r, sas or stat: converts the dataset into a csv, txt of a file suitable for one of the statistics packages
  - bulk: creates a bulk file which is used in conjunction wwith ukbfetch to download bulk data.

5. for bulk data, use ukbfetch
~~~bashscript
wget  -nd  biobank.ndph.ox.ac.uk/ukb/util/gfetch
chmod 755 gfetch
for i in {1..22}; do ./gfetch 22418 -c${i} -ak....key; done
./gfetch 22418 -cX -ak...key
./gfetch 22418 -cY -ak...key
./gfetch 22418 -cXY -ak...key
./gfetch 22418 -cMT -ak...key
~~~
- 'ukb22418_c1_b0_v2.bed','ukb22418_c2_b0_v2.bed',...,'ukb22418_cMT_b0_v2.bed' are generated.
- download calls BIM and FAM
~~~bashscript
## for fam
./gfetch 22418 -c1 -ak...key -m       #name of output: ukb22418_c1_b0_v2_s488176.fam
mv ukb22418_c1_b0_v2_s488176.fam ukb22418_b0_v2.fam   #rename the file
## for bim
wget  -nd  biobank.ndph.ox.ac.uk/ukb/ukb/auxdata/ukb_snp_bim.tar
tar -xvf ukb_snp_bim.tar
~~~
- etc (Marker-QC, sample-QC, relatedness files)
~~~bashscript
## for marker QC
wget  -nd  biobank.ndph.ox.ac.uk/ukb/ukb/auxdata/ukb_snp_qc.txt

## for sample QC
# need to request standard field from Category 100313

## for relatedness
./gfetch rel -ak...key
~~~
