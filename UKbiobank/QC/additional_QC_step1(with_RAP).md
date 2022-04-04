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
dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ sudo docker build -t pvcf_qc_fail:0.3 .
dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ sudo docker save pvcf_qc_fail:0.3| gzip -c > pvcf_qc_faill_0.3.tar.gz
dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ dx upload -p pvcf_qc_faill_0.3.tar.gz --path Rett_20220315:/Docker/pvcf_qc_fail/pvcf_qc_fail_0.3.tar.gz
dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ dx upload -p Dockerfile --path Rett_20220315:/Docker/pvcf_qc_fail/Dockerfile_for_0.3


#dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ sudo docker pull quay.io/biocontainers/picard:2.26.10--hdfd78af_0
#dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ sudo docker save quay.io/biocontainers/picard:2.26.10--hdfd78af_0 | gzip -c > quay.io_biocontainers_picard_2.26.10--hdfd78af_0.tar.gz
#dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$ dx upload -p quay.io_biocontainers_picard_2.26.10--hdfd78af_0.tar.gz --path Rett_20220315:/Docker/quay.io_biocontainers_picard_2.26.10--hdfd78af_0.tar.gz
~~~
- to confrim the path
~~~bashscript
dnanexus@job-G8jgq4QJFqgVYbVb5fB75G41:~$  docker run -v /home/dnanexus:/home/dnanexus -it --entrypoint /bin/bash pvcf_qc_fail:0.3
~~~
Step 3. Creating an applet in WDL

Step 4. Compile the WDL task using dxCompiler to a DNAnexus applet
- install dxCompiler.jar (https://github.com/dnanexus/dxCompiler/releases)
~~~bashscript
 jeongha@jeonghas-MacBook-Pro $ java -jar /Users/jeongha/software/dxCompiler-2.9.1.jar compile /Users/jeongha/Dropbox/JH/2022/ukbiobank/pvcf_qc_parallel.wdl
[warning] Project is unspecified...using currently selected project project-G8gyxY0JFqgX5ZX33gk0yybx
applet-G8jv5k8JFqgXB00Q5Z6KjfBF
~~~
- dxWDLrt AssetBundle and pvcf_qc_fail applet were generated on the Project

Step 5. test for 1 input file
~~~bashscript
dx run pvcf_qc_fail_parallel -h
dx run pvcf_qc_fail_parallel -ipvcf=file-Fz7JVvjJ7G2Gfp6kJ51Ff492 --folder="/pVCF_qc_process/" --tag 200K_exome_analysis --tag original --priority normal -y 
~~~
- connecting to jobs via ssh
~~~bashscript
dx ssh job-G90QpvjJFqgxQ248ByX2GfF6
dnanexus@job-G90V7vQJFqgzZj85K67Xkgb5:~$ ls
dnanexus-executable.json  dx_stdout    job-G90V7vQJFqgzZj85K67Xkgb5          job_scratch_space  outputs
dnanexus-job.json         environment  job-G90V7vQJFqgzZj85K67Xkgb5.code.sh  meta               work
dx_stderr                 inputs       job_input.json                        mnt
dnanexus@job-G90V7vQJFqgzZj85K67Xkgb5:~$ cat dnanexus-executable.json
{"id": "applet-G90V7jjJFqgk5Gg0J4JjzV6G", "project": "container-G90V7x8J6XK68bbQ1XK85PZY", "class": "applet", "sponsored": false, "name": "pvcf_qc_fail_pilot", "types": [], "state": "closed", "hidden": false, "links": ["file-G8J1QqjJP5P4bx8yKvGBQFFQ", "file-G8zFfqjJFqgx6Bvb2FF3Vj7j"], "folder": "/", "tags": ["dxCompiler"], "created": 1648432099000, "modified": 1648432117905, "createdBy": {"user": "user-jeongcool"}, "runSpec": {"interpreter": "bash", "bundledDependsByRegion": {"aws:eu-west-2": [{"name": "dxWDLrt.tar.gz", "id": {"$dnanexus_link": "file-G8J1QqjJP5P4bx8yKvGBQFFQ"}}, {"name": "pvcf_qc_fail_0.2.tar.gz", "id": {"$dnanexus_link": "file-G8zFfqjJFqgx6Bvb2FF3Vj7j"}, "stages": []}]}, "systemRequirements": {"main": {"instanceType": "mem3_ssd1_v2_x8"}}, "executionPolicy": {}, "timeoutPolicy": {"*": {"days": 0, "hours": 5, "minutes": 0}}, "bundledDepends": [{"name": "dxWDLrt.tar.gz", "id": {"$dnanexus_link": "file-G8J1QqjJP5P4bx8yKvGBQFFQ"}}, {"name": "pvcf_qc_fail_0.2.tar.gz", "id": {"$dnanexus_link": "file-G8zFfqjJFqgx6Bvb2FF3Vj7j"}, "stages": []}], "distribution": "Ubuntu", "release": "20.04", "version": "0", "systemRequirementsByRegion": {"aws:eu-west-2": {"main": {"instanceType": "mem3_ssd1_v2_x8"}}}}, "inputSpec": [{"name": "overrides___", "class": "hash", "optional": true, "group": "Reserved for dxCompiler"}, {"name": "overrides______dxfiles", "class": "array:file", "optional": true, "group": "Reserved for dxCompiler"}, {"name": "pvcf", "class": "array:file", "help": "chunked pvcf", "patterns": ["*.vcf.gz"]}], "outputSpec": [{"name": "variant", "class": "array:file", "optional": true}], "title": "pvcf_qc_fail_pilot", "summary": "", "description": "# This app requires access to the following dependencies that are not packaged with the app\n* Hard-coded instance type\n    * `mem3_ssd1_v2_x8`\n* Available instance types determined during WDL compilation will be used to select instance types during workflow execution", "developerNotes": "", "access": {"network": []}, "dxapi": "1.0.0", "ignoreReuse": false}
dnanexus@job-G90V7vQJFqgzZj85K67Xkgb5:~$ cat dnanexus-job.json
{"id": "job-G90V7vQJFqgzZj85K67Xkgb5", "region": "aws:eu-west-2", "name": "pvcf_qc_fail_pilot", "tags": [], "properties": {}, "executable": "applet-G90V7jjJFqgk5Gg0J4JjzV6G", "executableName": "pvcf_qc_fail_pilot", "class": "job", "created": 1648432114392, "modified": 1648432202236, "project": "project-G8gyxY0JFqgX5ZX33gk0yybx", "billTo": "org-ukb_wallet_eaa1cc3b47d", "costLimit": null, "invoiceMetadata": null, "folder": "/", "parentJob": null, "originJob": "job-G90V7vQJFqgzZj85K67Xkgb5", "parentAnalysis": null, "analysis": null, "stage": null, "rootExecution": "job-G90V7vQJFqgzZj85K67Xkgb5", "state": "running", "function": "main", "workspace": "container-G90V7x8J6XK68bbQ1XK85PZY", "launchedBy": "user-jeongcool", "detachedFrom": null, "priority": "normal", "workerReuseDeadlineRunTime": {"state": "reuse-off", "waitTime": -1, "at": -1}, "dependsOn": [], "failureCounts": {}, "stateTransitions": [{"newState": "runnable", "setAt": 1648432117970}, {"newState": "running", "setAt": 1648432202227}], "applet": "applet-G90V7jjJFqgk5Gg0J4JjzV6G", "singleContext": false, "ignoreReuse": false, "httpsApp": {"enabled": false}, "rank": 0, "details": {}, "systemRequirements": {"main": {"instanceType": "mem3_ssd1_v2_x8"}}, "executionPolicy": {"restartOn": {"UnresponsiveWorker": 2, "JMInternalError": 1, "ExecutionError": 1}}, "instanceType": "mem3_ssd1_v2_x8", "finalPriority": "normal", "networkAccess": [], "allowSSH": ["147.47.228.76"], "host": "ec2-13-40-196-232.eu-west-2.compute.amazonaws.com", "sshPort": 22, "debug": {}, "startedRunning": 1648432147000, "delayWorkspaceDestruction": false, "timeout": 18000000}
dnanexus@job-G90V7vQJFqgzZj85K67Xkgb5:~/mnt$ ls
input35710ee3-63a9-4181-9112-14689ff72555
dnanexus@job-G90V7vQJFqgzZj85K67Xkgb5:~/meta$ ls
commandScript  containerId  containerRunScript  dxfuseDownloadManifest.json  stderr  stdout
~~~

### Generating Job submission script
Step 6. Efficiently fetch the input file names from RAP
~~~bashscript
$ dx find data --folder "/Bulk/Exome sequences_Previous exome releases/Population level exome OQFE variants, pVCF format - interim 200k release" --name "*.vcf.gz" --delim > inputfile.txt
$ sort -k 4 -t$'\t' inputfile.txt > inputfile2.txt
~~~

Step 7. Create job submissions where each job processes N samples
~~~bashscript
python create_job_submission.py inputfile.txt 18 > submission_command.txt
~~~

~~~bashscript
$ head -1 submission_command.txt
dx run /pvcf_qc_fail -ipvcf=file-Fz7JgBQJ055qvYF24kKj9Yj5 -ipvcf=file-Fz7JgBQJZQVZxbjf3kbQkbJ6 -ipvcf=file-Fz7JgvQJp3PqbFp9P9vVkfJz -ipvcf=file-Fz7Jj10Jk6yvfp6kJ51Ff596 -ipvcf=file-Fz7JjkQJxq3y8bfX3q9QGq2X -ipvcf=file-Fz7Jjy8JYy0V8FZpP4ppqbKj -ipvcf=file-Fz7Jk40J598Y9z2k5zXxpZpy -ipvcf=file-Fz7Jk48J9jxV8FZpP4ppqbQ0 -ipvcf=file-Fz7Jk7QJ5J7kQGvYP9Kjp7x6 -ipvcf=file-Fz7Jk90JvGGPG7ZFPf4x4X16 -ipvcf=file-Fz7Jp3jJp3PX21zq6b1xzzJP -ipvcf=file-Fz7Jp8QJp1y5Q47X65F4F8B6 -ipvcf=file-Fz7JpxjJBx139z2k5zXxpb4p -ipvcf=file-Fz7JqF8J9jxqj4YF655Vx5Xg -ipvcf=file-Fz7Jx10Jp1yGJ71xBZ1qf9gj -ipvcf=file-Fz7JZJQJb74K3KP0B5Ygkp2f -ipvcf=file-Fz7JZP8J7G2KPY8b954zVx0f -ipvcf=file-Fz7JZV8J055fF0bQ95b57kGV  --folder="/pVCF_qc_process/0" --tag 200K_exome_exome_analysis --tag original --tag batch_n_0 --priority normal -y --brief
$ head -1 submission_command.txt |sh
~~~
- this runs serially not parallelly
- would rather run following command. this makes respectively jobs which perform the execution serially.
~~~bashscript
dx run /pvcf_qc_fail_pilot -ipvcf=file-Fz7JZ10JXVzZxbjf3kbQkZgQ -ipvcf=file-Fz7JfyjJXVzz3Y9GJ2xy4179 -ipvcf=file-Fz7Jfz8J5J7zG7ZFPf4x4VXz -ipvcf=file-Fz7Jg98JJVy0qq0Y9v6kFyKx -ipvcf=file-Fz7JgY0JvGG5p3VBJJB3fgGy -ipvcf=file-Fz7Jgb0JP03644kYJkx9Bx78 -ipvcf=file-Fz7Jgv0JxBk5JF4BF8j7qvXJ -ipvcf=file-Fz7Jj88JgPxPPf5VFJGGj09g -ipvcf=file-Fz7JjQQJ9jxb9KqgKJZjk5QP -ipvcf=file-Fz7JjYQJPqkV1Qy11vFbJ5Gx  --folder="/pVCF_qc_process/5" --tag 200K_exome_exome_analysis --tag original --tag batch_n_5 --priority normal -y --brief && \
dx run /pvcf_qc_fail_pilot -ipvcf=file-Fz7JjkjJXVzbYZbF1y68bkXB -ipvcf=file-Fz7Jk7jJZQVy0y652gXxxvfV -ipvcf=file-Fz7JkJ8JZQVV5gJjGbyfgBxJ -ipvcf=file-Fz7JkZjJ5J7Y9jyp64y7QqgJ -ipvcf=file-Fz7Jpg8JZQVb2Fqz4kPZgVxx -ipvcf=file-Fz7JqZjJvGG5fvfj6515X7jG -ipvcf=file-Fz7Jx60Jk6yfF0bQ95b57xg3 -ipvcf=file-Fz7JZqjJf7VyPY8b954zVx37 -ipvcf=file-Fz7JZx0JvGG0qq0Y9v6kFqyg -ipvcf=file-Fz7JZy0J975X21zq6b1xzyQB  --folder="/pVCF_qc_process/6" --tag 200K_exome_exome_analysis --tag original --tag batch_n_6 --priority normal -y --brief && \
dx run /pvcf_qc_fail_pilot -ipvcf=file-Fz7Jb00JQGKbz22436V6PGgB -ipvcf=file-Fz7Jb70JYGZ5Q47X65F4F61Z -ipvcf=file-Fz7Jb98JjvJ52Fqz4kPZgQFp -ipvcf=file-Fz7JbF0JVBF644kYJkx9Bpx9 -ipvcf=file-Fz7JbFjJgPxFj4YF655Vx4Z6 -ipvcf=file-Fz7Jbg0J9jxZ4FyfJX1jjjgK -ipvcf=file-Fz7JbxQJjvJ3xV1P4Q9z44by -ipvcf=file-Fz7Jbz0JYYBFvYF24kKj9YQz -ipvcf=file-Fz7Jf58J499vfp6kJ51Ff4zV -ipvcf=file-Fz7Jf68JjvJK3KP0B5YgkpFQ  --folder="/pVCF_qc_process/7" --tag 200K_exome_exome_analysis --tag original --tag batch_n_7 --priority normal -y --brief && \
...
~~~
