# Python Project Template



## docker environment 
Use docker environment to avoid annoying conflicts.
First, you must set the project name in `docker/.env` file.
then you can run `docker-compose up -d` command 
to build an docker image with default Dockerfile.
```bash
$ cd docker \
    && docker-compose up -d
```
for details about docker, see official documentations
- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
