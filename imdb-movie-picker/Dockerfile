# Dockerfile - Blueprint for building images
# Image - A template for running containers
# Container - Actual running process where we have our packaged project

FROM python:3.11.8-slim

WORKDIR /app

# Fix: Force Python to print to terminal immediately
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir requests beautifulsoup4

COPY main.py .

CMD ["python", "main.py"]