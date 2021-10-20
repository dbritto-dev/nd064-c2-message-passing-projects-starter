#!/usr/bin/env bash

kubectl exec -i $1 --container broker-server -- bash -c "kafka-topics --create --bootstrap-server localhost:29092 --replication-factor 1 --partitions 1 --topic Persons"
kubectl exec -i $1 --container broker-server -- bash -c "kafka-topics --create --bootstrap-server localhost:29092 --replication-factor 1 --partitions 1 --topic Locations"