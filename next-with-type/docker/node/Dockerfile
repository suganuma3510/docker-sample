FROM node:15.8.0-alpine3.10

ENV PORT 3000

WORKDIR /app
COPY ./app .

EXPOSE ${PORT}

CMD ["yarn", "dev"]
