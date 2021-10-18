#!/bin/bash

DOCKER_USER=minorpatch

docker login

docker build -f ./modules/person_api/Dockerfile ./modules/person_api -t $DOCKER_USER/udaconnect-person-api
docker build -f ./modules/location_api/Dockerfile ./modules/location_api -t $DOCKER_USER/udaconnect-location-api
docker build -f ./modules/connection_api/Dockerfile ./modules/connection_api -t $DOCKER_USER/udaconnect-connection-api
docker build -f ./modules/frontend/Dockerfile \
             --build-arg REACT_APP_PERSON_API_URL=http://localhost:30001/persons/ \
             --build-arg REACT_APP_CONNECTION_API_URL=http://localhost:30003/connections/ \
             ./modules/frontend \
             -t $DOCKER_USER/udaconnect-app

docker push $DOCKER_USER/udaconnect-person-api
docker push $DOCKER_USER/udaconnect-location-api
docker push $DOCKER_USER/udaconnect-connection-api
docker push $DOCKER_USER/udaconnect-app