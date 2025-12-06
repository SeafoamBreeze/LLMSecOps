#!/bin/bash
kubectl create secret docker-registry regcred --from-file=.dockerconfigjson=/Users/Darryl/.docker/config.json -oyaml --dry-run=client > regcred.yaml
