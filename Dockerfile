FROM python:3.12-alpine3.20

WORKDIR /app
COPY src/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ .

ENV PORT=8080
ENV PYTHONUNBUFFERED=1
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt


# COPY certs/mitmproxy-ca-cert.crt /cert.crt
# RUN cat /cert.crt >> /etc/ssl/certs/ca-certificates.crt

COPY ./certs/mitmproxy-ca-cert.crt /usr/local/share/ca-certificates/mitmproxy-ca-cert.crt
RUN update-ca-certificates

SHELL ["/bin/sh", "-c"]
ENTRYPOINT python main.py $PORT 