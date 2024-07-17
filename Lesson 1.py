# Получаем строку от пользователя
numbers = input()
val_to_delete = int(input())

# Преобразуем строку в список
number_list = [int(num) for num in numbers.split(" ")]

# Удаляем все вхождения числа val_to_delete
result = [i for i in number_list if i != val_to_delete]

# Выводим результат
print(result)