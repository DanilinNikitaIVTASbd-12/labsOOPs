FROM python:3.10.6

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./lab6 /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]