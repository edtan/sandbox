FROM alpine:3.11

RUN apk add --no-cache python3

ENV PYTHONUNBUFFERED=TRUE

WORKDIR /app
COPY main.py version /app/

ENTRYPOINT ["python3", "/app/main.py"]