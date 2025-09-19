FROM postgres:17

RUN apt-get update && apt-get install -y locales \
    && echo "ru_RU.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen ru_RU.UTF-8

ENV LANG=ru_RU.UTF-8 \
    LANGUAGE=ru_RU:ru \
    LC_ALL=ru_RU.UTF-8


FROM python:3.12-slim

RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /lab2

COPY lab2/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY lab2/lab2.py .

CMD ["python", "lab2.py"]
