FROM python:3-alpine

WORKDIR /app

COPY src/. ./src
COPY run.py .
COPY requirements.txt .
COPY production.env ./.env

RUN pip install -r requirements.txt

CMD [ "python", "run.py" ]
