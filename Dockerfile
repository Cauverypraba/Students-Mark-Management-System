FROM python:3
LABEL Cauverypraba S <prabasatha221@gmail.com>

ENV PYTHONUNBUFFERED=1

WORKDIR /app

ADD . /app/

RUN pip install --upgrade pip

COPY ./requirements.txt ./app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
