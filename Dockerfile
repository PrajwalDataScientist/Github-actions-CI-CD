FROM python:3.9-slim

WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 1234

RUN ["python","app.py"]