1. install with Docker
~~~bashscript
# pull docker image
docker pull ghcr.io/soedinglab/mmseqs2
#docker run -v /home/mchoilab_dell/dell_drobo/project_jhl/20220706_KNU_nblibrary:/app -it --user 1002 --name mmseqs2_jhl ghcr.io/soedinglab/mmseqs2:latest /bin/bash
# build docker container
git clone https://github.com/soedinglab/MMseqs2.git
cd MMseqs2


docker build -t mmseqs2 .
# error sign: "WARNING: buildx: failed to read current commit information with git rev-parse --is-inside-work-tre"
# run "git config --global --add safe.directory /home/mchoilab_dell/dell_drobo/project_jhl/docker/MMseqs2"
# then re-run "docker build -t mmseqs2"

vi docker-compose.yml
docker-compose up -d
docker exec -it mmseqs2 /bin/bash
# error sign: "Error response from daemon: Container cd510c14d7ef208c76fc7c86d1689cbd377ef9766c614e9835603499ee66520f is not running"

# docker run -v "$(pwd):/app" ghcr.io/soedinglab/mmseqs2 mmseqs easy-search /app/QUERY.fasta /app/DB.fasta /app/result.m8 /app/tmp
~~~

