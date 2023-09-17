FROM debian:latest
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests

ADD authentification.py /authentification/authentification.py
WORKDIR /authentification/
CMD python3 authentification.py