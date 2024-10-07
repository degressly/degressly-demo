FROM python:3.12-alpine3.20

WORKDIR /app
COPY src/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ .

ENV PORT=8080
ENV PYTHONUNBUFFERED=1

COPY certs/cert.crt /cert.crt
RUN cat /cert.crt >> /etc/ssl/certs/ca-certificates.crt

SHELL ["/bin/sh", "-c"]
ENTRYPOINT python main.py $PORT 