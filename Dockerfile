FROM python:3.6-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /source
COPY ./requirements.txt /source/
RUN apt update
RUN apt install -y gcc libpq-dev python3-dev
RUN pip3 install -r /source/requirements.txt
COPY source /source/

WORKDIR /source

ENV FLASK_APP 'main'
ENV FLASK_RUN_HOST '0.0.0.0'
ENV FLASK_RUN_PORT '5000'

EXPOSE 5000

CMD flask run
