Небольшой скрипт для мониторинга свободных слотов в расписании врачей Лечебного Центра.

Скрипт принимает на вход урлы сайта lcenter и выдаёт часы в которые можно записаться к доктору на сегодня.

Установка Common Lisp версии
============================

Нужно установить [Roswell](https://github.com/roswell/roswell), а дальше - либо запускать `./monitor.ros`, либо собрать бинарник: `ros build monitor.ros` и запускать его.

Установка python версии
=======================

```
./bootstrap
```

Запуск
------

```
./monitor.py http://www.lcenter.ru/doctor/vedeneeva-natalya-vladimirovna
```
