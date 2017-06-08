From ubuntu:16.04
MAINTAINER Romel Barrios <lssromel@outlook.com>

EXPOSE 5010

RUN apt-get update && apt-get install -y --no-install-recommends \
	python-dev \ 
	python-pip \
	git \
	build-essential
RUN apt-get install iputils-ping -y
RUN apt-get install net-tools -y
RUN pip install -U pip
RUN pip install setuptools
RUN pip install django djangorestframework requests html
WORKDIR /workspace
RUN mkdir -p /data/db
RUN git clone https://github.com/lssromel/result_app.git
WORKDIR /workspace/result_app
