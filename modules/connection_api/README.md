# Location API

## Install grpcio-tools globally

To install grpcio-tools globally use the next command:

```sh
python -m pip install grpcio-tools
```

## Generate Protobuf modules

To generate protobuf modules base on a proto file use the next command:

```sh
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./location.proto
```

## Run the application

To run the application use the next command:

```sh
docker compose up -d --build
```
