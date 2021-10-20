#!/usr/bin/env bash

kubectl exec -i $1 $2 -- bash -c "kafka-topics --create --bootstrap-server $BOOTSTRAP_SERVER --replication-factor 1 --partitions 1 --topic Persons"
kubectl exec -i $1 $2 -- bash -c "kafka-topics --create --bootstrap-server $BOOTSTRAP_SERVER --replication-factor 1 --partitions 1 --topic Locations"