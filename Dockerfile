FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /core
COPY . /core/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
