FROM python:3.10-slim

WORKDIR /app

COPY consumer.py .

RUN pip install confluent-kafka

CMD ["python", "-u", "consumer.py"]