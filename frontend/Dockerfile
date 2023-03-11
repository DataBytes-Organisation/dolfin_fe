FROM python:3.8-slim

RUN pip install --upgrade pip

WORKDIR /code

COPY requirements.txt /

RUN pip 

RUN pip install -r /requirements.txt

COPY ./ ./

ENV ENVIRONMENT_FILE=".env"

EXPOSE 8080

ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "application"]