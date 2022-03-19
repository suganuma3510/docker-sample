FROM node:15.8.0-alpine3.10

ENV LANG=C.UTF-8 \
    TZ=Asia/Tokyo

ENV HOST 0.0.0.0
ENV PORT 8080

WORKDIR /app
COPY ./app .

RUN apk update && \
    apk upgrade && \
    yarn install && \
    rm -rf /var/cache/apk/*

EXPOSE ${PORT}

CMD ["yarn", "dev"]
