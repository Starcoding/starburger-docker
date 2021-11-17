FROM python:3.9.5-alpine

WORKDIR /usr/src/star-burger

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/app
RUN addgroup -S app && adduser -S app -G app

ENV HOME=/home/star-burger
ENV APP_HOME=/home/star-burger
RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/staticfiles
WORKDIR $APP_HOME

RUN apk update && apk add git
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add zlib-dev jpeg-dev gcc musl-dev
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . $APP_HOME

RUN chown -R app:app $APP_HOME

USER app
