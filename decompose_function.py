"""
В этой задаче вам нужно декомпозировать функцию
которая рассчитывает примерное время в пути от одного пункта (start) до пункта (destination)
с учетом заданной скорости и небольшой поправки по времени.
Нужно реализовать три функции,которые принимают меньшее
количество аргументов,переиспользуя в них логику функции
Скорость можно определить по названию функций,константами заданы положения городов MOSCOW и VLADIVOSTOK,
их нужно использовать в соответствующих функциях.

"""
MOSCOW = 1000
VLADIVOSTOK = 9000

def time_calculation(start, destination, speed, correction=1.2):
    return round((abs(start-destination) / speed) * correction, 2)

# Реализуйте функции ниже, код выше изменять нельзя
from  functools import partial

def time_from_moscow_at_60(destination):
    return time_calculation(start=MOSCOW,destination=destination,speed=60)

def time_to_vladivostok_at_100(start):
    return time_calculation(start=start,destination=VLADIVOSTOK,speed=100)

def time_at_120(start, destination):
    return time_calculation(start=start,destination=destination,speed=120)

def time_from_moscow_to_vladivostok(speed):
    return time_calculation(start=MOSCOW,destination=VLADIVOSTOK,speed=speed)

