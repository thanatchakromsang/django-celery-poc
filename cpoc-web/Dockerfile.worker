FROM python:3.6

RUN pip install Django==2.0\
                djangorestframework==3.8\
                uWSGI==2.0.17\
                Pillow==4.2.0\
                psycopg2==2.7.1\
                requests==2.18.1\
                python-intercom==3.1.0

RUN apt-get update && apt-get install -y netcat

ENV APPLICATION_ROOT /app/

RUN mkdir $APPLICATION_ROOT
COPY . $APPLICATION_ROOT
WORKDIR $APPLICATION_ROOT

RUN pip install -r requirements.txt
