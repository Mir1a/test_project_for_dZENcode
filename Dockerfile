FROM python:3.8

WORKDIR /usr/src/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libwebp-dev g++ gcc gettext && \
    pip install --upgrade pip wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY ./entrypoint.sh .
COPY . .

RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
