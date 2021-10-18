FROM python:3.9-slim-buster as builder
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install --upgrade pip && python -m pip install --user -r requirements.txt

FROM python:3.9-slim-buster
WORKDIR /app
RUN apt update -y && apt install -y wget
RUN GRPC_HEALTH_PROBE_VERSION=v0.3.1 && \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64 && \
    chmod +x /bin/grpc_health_probe
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local:$PATH
EXPOSE 5000
CMD [ "python", "run.py" ]
