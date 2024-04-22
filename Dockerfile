FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

COPY lib_store /app/lib_store

# Install dependencies
COPY requirements.txt /app/lib_store/requirements.txt
RUN pip install --no-cache-dir -r /app/lib_store/requirements.txt

ENV DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS}

WORKDIR /app/lib_store

EXPOSE 8000
