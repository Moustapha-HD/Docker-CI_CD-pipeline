FROM debian:latest
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests
ADD authorization.py /authorization/authorization.py
WORKDIR /authorization/
CMD python3 authorization.py