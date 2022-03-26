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
2022-03-16 20:32:58 pvcf_qc_fail STDERR + docker run -a stdout -a stderr --memory=4194304000 --cidfile /home/dnanexus/meta/containerId --user 0:0 --hostname job-G8jvYB8JFqgqgjf9620qfvjZ --entrypoint /bin/bash -v /home/dnanexus:/home/dnanexus pvcf_qc_fail:0.1 /home/dnanexus/meta/commandScript
2022-03-16 20:32:58 pvcf_qc_fail STDERR WARNING: Your kernel does not support swap limit capabilities or the cgroup is not mounted. Memory limited without swap.
2022-03-16 20:32:59 pvcf_qc_fail STDERR /home/dnanexus/meta/commandScript: line 9: unexpected EOF while looking for matching `''
2022-03-16 20:32:59 pvcf_qc_fail STDERR /home/dnanexus/meta/commandScript: line 20: syntax error: unexpected end of file
2022-03-16 20:32:59 pvcf_qc_fail STDERR +++ cat /home/dnanexus/meta/containerId
2022-03-16 20:32:59 pvcf_qc_fail STDERR ++ docker wait 7015c0ad15e4830807bd48b844eaf6bafb0427e3af372c14817a3e2790e0d862
2022-03-16 20:32:59 pvcf_qc_fail STDERR + rc=2
2022-03-16 20:32:59 pvcf_qc_fail STDERR ++ cat /home/dnanexus/meta/containerId
2022-03-16 20:32:59 pvcf_qc_fail STDERR + docker rm 7015c0ad15e4830807bd48b844eaf6bafb0427e3af372c14817a3e2790e0d862
2022-03-16 20:33:00 pvcf_qc_fail STDOUT exit $rc7015c0ad15e4830807bd48b844eaf6bafb0427e3af372c14817a3e2790e0d862
2022-03-16 20:33:00 pvcf_qc_fail STDERR + exit 2
2022-03-16 20:33:00 pvcf_qc_fail STDERR [error] failure executing Task action 'run'
2022-03-16 20:33:00 pvcf_qc_fail STDERR java.io.FileNotFoundException: /home/dnanexus/meta/stderr
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at dx.util.FileUtils$.readFileBytes(FileUtils.scala:186)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at dx.util.FileUtils$.readFileContent(FileUtils.scala:207)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at dx.executor.WorkerJobMeta.runJobScriptFunction(JobMeta.scala:985)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at dx.executor.TaskExecutor.apply(TaskExecutor.scala:991)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at dx.executor.BaseCli.dispatchCommand(BaseCli.scala:86)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at dx.executor.BaseCli.main(BaseCli.scala:137)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at dxExecutorWdl.MainApp$.delayedEndpoint$dxExecutorWdl$MainApp$1(Main.scala:27)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at dxExecutorWdl.MainApp$delayedInit$body.apply(Main.scala:26)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at scala.Function0.apply$mcV$sp(Function0.scala:39)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at scala.Function0.apply$mcV$sp$(Function0.scala:39)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at scala.runtime.AbstractFunction0.apply$mcV$sp(AbstractFunction0.scala:17)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at scala.App.$anonfun$main$1(App.scala:76)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at scala.App.$anonfun$main$1$adapted(App.scala:76)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at scala.collection.IterableOnceOps.foreach(IterableOnce.scala:563)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at scala.collection.IterableOnceOps.foreach$(IterableOnce.scala:561)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at scala.collection.AbstractIterable.foreach(Iterable.scala:926)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at scala.App.main(App.scala:76)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at scala.App.main$(App.scala:74)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at dxExecutorWdl.MainApp$.main(Main.scala:26)
2022-03-16 20:33:00 pvcf_qc_fail STDERR 	at dxExecutorWdl.MainApp.main(Main.scala)

~~~
### Generating Job submission script
Step 6. Efficiently fetch the input file names from RAP
~~~bashscript
$ dx find data --folder "/Bulk/Exome sequences_Previous exome releases/Population level exome OQFE variants, pVCF format - interim 200k release" --name "*.vcf.gz" --delim > inputfile.txt

