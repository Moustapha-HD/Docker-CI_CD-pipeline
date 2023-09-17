FROM debian:latest
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests
ADD content.py /content/content.py
WORKDIR /content/
CMD python3 content.py