
#### purpose: read mutant library of target gene with pacbio HiFi sequencing and check the condition of library

[0] filter reads by expected length
- extract reads whose length is under range of interast 
~~~bashscript
python fasta_length_v2.py
~~~

[1] align filtered fasta to reference with pacbio pbmm2
~~~bashscript
/ssd-data/workspace/support/tool/pacbio/smrtcmds/bin/pbmm2 align MECP2_REF.fasta MECP2.hifi_reads.length.fasta MECP2.hifi_reads.length.bam --log-level INFO
samtools sort -O bam -o MECP2.hifi_reads.length.sorted.bam MECP2.hifi_reads.length.bam
samtools index MECP2.hifi_reads.length.sorted.bam
~~~

[2] analysis observed variants
~~~bashscript
python /Users/jeongha/Dropbox/JH/2021/sat_mut/pacbio/ORFcall_JH_v10.py
~~~

