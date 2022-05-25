FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -U pip
RUN pip install -r requirements.txt

EXPOSE 8501