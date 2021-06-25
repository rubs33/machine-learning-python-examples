FROM python:3

WORKDIR /app

RUN apt-get update && apt-get install -y graphviz

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

