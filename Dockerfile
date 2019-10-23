from python:latest

RUN pip install bs4

ADD . /root
WORKDIR /root
