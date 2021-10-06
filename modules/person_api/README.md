# Person API Overview

# Pre-requisites

-   Docker: https://docs.docker.com/engine/install/

# Start-up the services

```sh
docker compose up -d --build
```

# Down the services

```sh
docker compose down
```

# Execute commands

```sh
docker compose exec app <command> <arg-1> <arg-2> ... <arg-n>
```

For instance:

```sh
docker compose exec app echo "Hello World!"
```
