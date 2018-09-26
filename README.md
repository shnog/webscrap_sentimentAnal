# webscrap_sentimentAnal
takes Finviz articles and gives sentiment score

## Docker setup
To run the project using docker first install docker.
Instructions can be found at the bottom of [this page](https://docs.docker.com/install/).

The project can be run either using docker, or using docker-compose.
Docker-compose adds sugar on top of docker and allows for easily spinning up and down multiple containers.

### Docker compose approach
To run the container using docker compose,
```
docker-compose build && docker-compose up -d
```
To stop the container using docker compose
```
docker-compose down
```
### Pure docker approach
 build the container run the command,
```
docker build -t webscrape .
```
Before running the docker container, first stop and delete the previous image.
Use --mount to be have files generated in the container be transferred into the local directory.
```
#stop container if exists
docker stop devtest
docker rm devtest
#rebuild container
docker build -t webscrape .
#run container
docker run -d \
--name devtest \
--mount type=bind,source="${pwd}",target=/code \
webscrape

```
For some reason the docker container only build isn't working properly mounting the local directory as a volume. That's fine since this is just an example of how to build using purely docker.
