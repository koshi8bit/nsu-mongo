# MONGO
Это последняя лаба по Распределенным системам.

## Как работает 
Создано 2 контейнера, один на python, другой с MongoDB.

Контейнер с кодом python подключается к контейнеру MongoDB и делает запрос.

Для каждого контейнера был использован [**docker-builder**](https://github.com/koshi8bit/docker-builder)

Оба контейнера лежат в [Docker Hub](https://hub.docker.com/u/koshi8bit)

## Начальные данные
1. Я поднял на виртуалке debian, и пробросил порты 
   - 8080:8080 для http
   - 2222:22 для ssh
1. Для передачи файлов на debian машину и развертывания контейнера был использован мой docker-builder

## Как запустить
1. Для запуска требуется скачать проект docker-builder с гитхаба 
1. Настроить docker-builder по [инструкции](https://github.com/koshi8bit/docker-builder/blob/master/readme.md) с гитхаба для папок:
   - py
   - mongo
1. Запустить 
   - py/-restart.bat
   - mongo/-restart.bat
1. Подключиться с хостовой машины к контейнеру с python [ТУЦ](http://127.0.0.1:8080)
1. Если видна надпись *I am alive!* - контейнер стартанул
1. Теперь с главной страницы нужно перейти на вкладку *Try MongoDB*
1. На новой вкладке добавятся записи и будут выведены на экран
1. Готово

