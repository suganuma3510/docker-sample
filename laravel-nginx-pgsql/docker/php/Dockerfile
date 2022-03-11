FROM php:8.0.5-fpm-buster
SHELL ["/bin/bash", "-oeux", "pipefail", "-c"]

ENV COMPOSER_ALLOW_SUPERUSER=1 \
  COMPOSER_HOME=/composer

COPY --from=composer:2.0 /usr/bin/composer /usr/bin/composer

RUN apt-get update && \
  apt-get install -y libonig-dev libpq-dev git zip unzip && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  docker-php-ext-install pdo pdo_pgsql pgsql

COPY ./docker/php/php.ini /usr/local/etc/php/php.ini

WORKDIR /laravel