# additional QC of pVCF from 200K 

## run single dx run with app 

~~~bashscript
# upload target region bed file to RAP
 dx upload /Users/jeongha/Dropbox/JH/2022/ukbiobank/xgen_plus_spikein.GRCh38.bed --destination Rett_20220315:/20220315_input/

# run vcftools with "swiss-army-knife"
dx run swiss-army-knife \
  -iin="/Bulk/Exome sequences_Previous exome releases/Population level exome OQFE variants, pVCF format - interim 200k release/ukb23156_c1_b0_v1.vcf.gz" \
  -iin="/20220315_input/xgen_plus_spikein.GRCh38.bed" \
  -icmd="vcftools --gzvcf *.vcf.gz --exclude-bed *.bed --recode --recode-INFO-all --stdout| bgzip > ukb23156_c1_b0_v2.tcr.vcf.gz" \
  --destination Rett_20220315:/20220315_output \
  -y
  
~~~

## Run the Cloud Workstation App
- to reduce the total number of jobs by processing a batch of N samples in each job
### 1. Configure ssh
Step1.Configure SSH for your account
~~~bashscript
jeongha@jeonghas-MacBook-Pro $ dx ssh_config
Select an SSH key pair to use when connecting to DNAnexus jobs. The public key will be saved to your
DNAnexus account (readable only by you). The private key will remain on this computer.

0) Generate a new SSH key pair using ssh-keygen
1) /Users/jeongha/.ssh/id_rsa.pub
2) Select another SSH key pair...

Pick a numbered choice [0]: 1
Updated public key for user user-jeongcool
Your account has been configured for use with SSH. Use dx run with the --allow-ssh, --ssh,
or --debug-on options to launch jobs and connect to them.

jeongha@jeonghas-MacBook-Pro $ dx select "Rett_20220315"
Selected project Rett_20220315
~~~
### 2. Preparing the Applet
Step 2: launch the cloud_workstation app & packaging tool into a Docker image and uploading to RAP
- as soon as this command line is done, job is started and the cloud_workstation prompt appears
~~~bashsciprt
jeongha@jeonghas-MacBook-Pro $ dx run cloud_workstation --ssh
Detected client IP as '147.47.228.76'. Setting allowed IP ranges to '147.47.228.76'. To change the permitted IP addresses use --allow-ssh.

Select an optional parameter to set by its # (^D or <ENTER> to finish):

 [0] Maximum Session Length (suffixes allowed: s, m, h, d, w, M, y) (max_session_length) [default="1h"]
 [1] Files (fids)
 [2] Snapshot (snapshot)

Optional param #: 0

Input:   Maximum Session Length (suffixes allowed: s, m, h, d, w, M, y) (max_session_length)
Class:   string

Enter string value ('?' for more options)
max_session_length: 3h

Select an optional parameter to set by its # (^D or <ENTER> to finish):

 [0] Maximum Session Length (suffixes allowed: s, m, h, d, w, M, y) (max_session_length) [="3h"]
 [1] Files (fids)
 [2] Snapshot (snapshot)

Optional param #:

Using input JSON:
{
    "max_session_length": "3h"
}

Confirm running the executable with this input [Y/n]: Y
Calling app-G8Bgjj057q3753y08FPPYPvx with output destination project-G8gyxY0JFqgX5ZX33gk0yybx:/

Job ID: job-G8jgq4QJFqgVYbVb5fB75G41
Waiting for job-G8jgq4QJFqgVYbVb5fB75G41 to start........
Resolving job hostname and SSH host key.....................................
Checking connectivity to ec2-3-9-13-87.eu-west-2.compute.amazonaws.com:22...OK
Connecting to ec2-3-9-13-87.eu-west-2.compute.amazonaws.com:22
Connecting to ec2-3-9-13-87.eu-west-2.compute.amazonaws.com:22
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-1066-aws x86_64)
...
Welcome to DNAnexus!

This is the DNAnexus Execution Environment, running job-G8jgq4QJFqgVYbVb5fB75G41.
Job: Cloud Workstation
App: cloud_workstation:main
Instance type: mem1_ssd1_v2_x8
Project: Rett_20220315 (project-G8gyxY0JFqgX5ZX33gk0yybx)
Workspace: container-G8jgq58JK9YzJx8K1jf0V356
Running since: Wed Mar 16 06:03:27 UTC 2022
Running for: 0:01:49
The public address of this instance is ec2-3-9-13-87.eu-west-2.compute.amazonaws.com.
You are running byobu, a terminal session manager.
If you get disconnected from this instance, you can log in again; your work will be saved as long as the job is running.
For more information on byobu, press F1.
The job is running in terminal 1. To switch to it, use the F4 key (fn+F4 on Macs; press F4 again to switch back to this terminal).
Use sudo to run administrative commands.
From this window, you can:
 - Use the DNAnexus API with dx
 - Monitor processes on the worker with htop
 - Install packages with apt-get install or pip3 install
 - Use this instance as a general-purpose Linux workstation
OS version: Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-1066-aws x86_64)
dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ mkdir docker
dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ cd docker
dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ vi Dockerfile
dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ sudo docker build -t pvcf_qc_fail:0.2 .
dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ sudo docker save pvcf_qc_fail:0.2| gzip -c > pvcf_qc_faill_0.2.tar.gz
dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ dx upload -p pvcf_qc_faill_0.2.tar.gz --path Rett_20220315:/Docker/pvcf_qc_fail/pvcf_qc_fail_0.2.tar.gz
dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ dx upload -p Dockerfile --path Rett_20220315:/Docker/pvcf_qc_fail/Dockerfile_for_0.2


dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ sudo docker pull quay.io/biocontainers/picard:2.26.10--hdfd78af_0
dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ sudo docker save quay.io/biocontainers/picard:2.26.10--hdfd78af_0 | gzip -c > quay.io_biocontainers_picard_2.26.10--hdfd78af_0.tar.gz
dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ dx upload -p quay.io_biocontainers_picard_2.26.10--hdfd78af_0.tar.gz --path Rett_20220315:/Docker/quay.io_biocontainers_picard_2.26.10--hdfd78af_0.tar.gz
~~~
- to confrim the path
~~~bashscript
dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$  docker run -v /home/dnanexus:/home/dnanexus -it --entrypoint /bin/bash pvcf_qc_fail:0.2
~~~
Step 3. Creating an applet in WDL

Step 4. Compile the WDL task using dxCompiler to a DNAnexus applet
- install dxCompiler.jar (https://github.com/dnanexus/dxCompiler/releases)
~~~bashscript
 jeongha@jeonghas-MacBook-Pro $ java -jar /Users/jeongha/software/dxCompiler-2.9.1.jar compile /Users/jeongha/Dropbox/JH/2022/ukbiobank/pvcf_qc.wdl
[warning] Project is unspecified...using currently selected project project-G8gyxY0JFqgX5ZX33gk0yybx
applet-G8jv5k8JFqgXB00Q5Z6KjfBF
~~~
- dxWDLrt AssetBundle and pvcf_qc_fail applet were generated on the Project

Step 5. test for 1 input file
~~~bashscript
dx run pvcf_qc_fail -h
dx run pvcf_qc_fail -ipvcf=file-Fz7JVvjJ7G2Gfp6kJ51Ff492 /
~~~
- connecting to jobs via ssh
~~~bashscript
dx ssh job-G90QpvjJFqgxQ248ByX2GfF6
~~~

### Generating Job submission script
Step 6. Efficiently fetch the input file names from RAP
~~~bashscript
$ dx find data --folder "/Bulk/Exome sequences_Previous exome releases/Population level exome OQFE variants, pVCF format - interim 200k release" --name "*.vcf.gz" --delim > inputfile.txt
$ sort -k 4 -t$'\t' inputfile.txt > inputfile2.txt
~~~

Step 7. Create job submissions where each job processes N samples
~~~bashscript
~~~
