#На выполнение заданий по питону студент предполагает потратить ч часов м минут (получить с клавиатуры). 
#Во сколько самое позднее ему следует начать, чтобы оставить на дорогу 1 час и успеть к 19:00 на занятия?

from datetime import datetime, timedelta

# Получаем данные с клавиатуры
ч = int(input("Введите количество часов, которое студент планирует потратить: "))
м = int(input("Введите количество минут, которое студент планирует потратить: "))

# Рассчитываем общее количество времени для заданий по питону
общее_время = timedelta(hours=ч, minutes=м)

# Вычисляем время, в которое студент должен начать, чтобы успеть на занятия
последнее_время = datetime.strptime("19:00", "%H:%M") - общее_время - timedelta(hours=1)

# Выводим результат
print("Студенту следует начать не позже", последнее_время.time(), "чтобы успеть к 19:00 на занятия.")
