#!/bin/bash

# Установка переменных окружения
export HTTP_PROXY="http://proxy.example.com:8080"
export HTTPS_PROXY="http://proxy.example.com:8080"

# Настройка Git
git config --global http.proxy $HTTP_PROXY

# Добавление SSH-ключа
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

# Проверка подключения
ping -c 3 google.com