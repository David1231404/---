#Получить с клавиатуры скорость самолета, названия городов и расстояние (на 12 баллов координаты lat, lon).
#Вычислить время в пути, считая скорость постоянной.

# Получаем данные с клавиатуры
скорость = float(input("Введите скорость самолета (в км/ч): "))
город_отправления = input("Введите название города отправления: ")
город_прибытия = input("Введите название города назначения: ")
расстояние = float(input("Введите расстояние между городами (в км): "))

# Вычисляем время в пути
время_в_пути = расстояние / скорость

# Выводим результат
print("Самолет летит из города", город_отправления, "в город", город_прибытия)
print(f"Время в пути: {время_в_пути:.2f} часов")
