FROM python:latest

EXPOSE 5432

WORKDIR /src
COPY requirements.txt /src
RUN pip install -r requirements.txt
COPY . /src