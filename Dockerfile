FROM python:3.6-alpine

MAINTAINER Gosha Chernousov

COPY . /adjoy_chet_maker

RUN pip install -r /adjoy_chet_maker/requirements.txt

WORKDIR /adjoy_chet_maker/

CMD ["python3", "run.py"]