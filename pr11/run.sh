#!/bin/bash
# Скрипт для запуска приложения с правильными настройками

cd "$(dirname "$0")"
export TK_SILENCE_DEPRECATION=1
export PYTHONUNBUFFERED=1

# Пробуем использовать Python 3.11 из Homebrew, если доступен
if [ -f "/opt/homebrew/bin/python3.11" ]; then
    /opt/homebrew/bin/python3.11 task.py
elif [ -f "/usr/local/bin/python3.11" ]; then
    /usr/local/bin/python3.11 task.py
else
    # Используем стандартный python3
    python3 task.py
fi

