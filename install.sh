#!/bin/bash

# Установка необходимого Python пакета
pip install .

# Выполнение скрипта для установки пароля
python -m my_termux_repo.set_password
