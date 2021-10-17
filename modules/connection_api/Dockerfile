FROM python:3.9-slim-buster as builder
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN python -m pip install --user -r requirements.txt

FROM python:3.9-slim-buster
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local:$PATH
CMD [ "python", "run.py" ]
