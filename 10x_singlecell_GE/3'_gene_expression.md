### 0. cellranger mkfastq (demultiplex)
- raw data given by theragen
~~~
{sample_name}--{index_seq}_S1_L002_I1_001.fastq.gz
{sample_name}--{index_seq}_S1_L002_R1_001.fastq.gz
{sample_name}--{index_seq}_S1_L002_R2_001.fastq.gz
...
{sample_name}--{index_seq}_S4_L002_I1_001.fastq.gz
{sample_name}--{index_seq}_S4_L002_R1_001.fastq.gz
{sample_name}--{index_seq}_S4_L002_R2_001.fastq.gz
~~~

### 1. cellranger count
- aligns fastq files to a reference transcriptome and generates a *.cloupe* (file for Loupe browser)
- required options
  - --id: output prefix
  - --fastq: path to fastq directory
  - --sample: if there are multiple samples
~~~bashscipt
/ssd-data/workspace/support/tool/cellranger-7.0.0/bin/cellranger count --id=run_count_iN_ko39 \
--fastqs=Sample_ko_39_iN \
--sample=ko_39_iN--AAGACGGA,ko_39_iN--CGAGGCTC,ko_39_iN--GTCCTTCT,ko_39_iN--TCTTAAAG \
--transcriptome=/ssd-data/workspace/support/tool/refdata-gex-GRCh38-2020-A \
--localcores=16
~~~
