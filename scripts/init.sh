#!/usr/bin/env bash

sudo zypper refresh
sudo zypper --non-interactive install bzip2 etcd apparmor-parser
curl -sfL https://get.k3s.io | sh -s - --write-kubeconfig-mode 644