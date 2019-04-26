FROM python:3.7-slim
MAINTAINER Chinseok Lee <me@askcompany.kr>

WORKDIR /dj
ADD . /dj

ENV PYTHONUNBUFFERED  1

RUN python3.7 -m pip install -r reqs/prod_azure.txt

EXPOSE 80

CMD ["/bin/sh", "/dj/entry.sh"]

