FROM python:3.12-alpine3.20

WORKDIR /app
COPY src/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ .

ENV PORT=8080
ENV PYTHONUNBUFFERED=1

SHELL ["/bin/sh", "-c"]
ENTRYPOINT python main.py $PORT 