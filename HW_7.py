# Создать две переменные и присвоить им одинаковые последовательности типа set. При этом не копируйте одну переменную в другую.
# Вывести в терминал результат сравнения двух созданных объектов.
# Сравнить два объекта используя оператор is.
# Есть ли определённые элементы в наборе, используя оператор in.

my_cars = {10, 'Mercedes', 'BMW', True}
other_cars = {True, 10, 'Lada', 'Moskvich'}

print(my_cars == other_cars)  # False

print(my_cars.__eq__(other_cars))  # False

# False сравнивает именно объекты, а не их значения
print(my_cars is other_cars)

print('Mercedes' in my_cars)  # True

print('Lada' not in my_cars)  # True

print('Lada' not in other_cars)  # False

# print([] in other_cars) TypeError: unhashable type: 'list'
