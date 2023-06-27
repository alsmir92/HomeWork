# Создайте набор с нескольких элементов типа int
my_set = {10, 15, 20, 25}
# Добавьте в него ещё один элемент
my_set.add(30)

print(my_set)
# Создайте ещё один набор с несколькими элементами, причём некоторые должны быть такими же как в первом наборе
copied_set = my_set.copy()

copied_set.add(35)
copied_set.add(40)

print(copied_set)
# Найдите общие элементы в двух наборах и поместите их в новый набор
last_set = my_set & copied_set

print(last_set)
# Конвертируйте результирующий набор в список и выведите список в терминал
my_list = list(last_set)

print(my_list)
print(type(my_list))
