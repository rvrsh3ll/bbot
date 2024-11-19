FROM python:3.10-slim

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PIP_NO_CACHE_DIR=off

WORKDIR /usr/src/bbot

RUN apt-get update && apt-get install -y openssl gcc git make unzip curl wget vim nano sudo

COPY . .

RUN pip install .

WORKDIR /root

ENTRYPOINT [ "bbot" ]
