FROM debian:latest

MAINTAINER Gosha Chernousov

RUN apt-get update && apt-get install -y python3-pip vim\
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

COPY . /adjoy_chet_maker

RUN pip3 install -r /adjoy_chet_maker/requirements.txt

WORKDIR /adjoy_chet_maker

CMD ["python3", "run.py"]