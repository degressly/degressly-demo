FROM python:3.12-alpine3.20

WORKDIR /app
COPY src/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ .

ENV PORT=8080
ENV PYTHONUNBUFFERED=1

COPY certs/mitmproxy-ca-cert.crt /cert.crt
COPY certs/mitmproxy-ca-cert.crt /usr/local/share/ca-certificates/extra/mitmproxy-ca-cert.crt
RUN update-ca-certificates
RUN cat /cert.crt >> /etc/ssl/certs/ca-certificates.crt
RUN export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

SHELL ["/bin/sh", "-c"]
ENTRYPOINT python main.py $PORT 