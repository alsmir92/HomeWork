# Задача №1
# Функция dict_to_list конвертирует словарь в саисок кортежей
# Функция принимает словарь, возвращает список кортежей. В каждом кортеже пара key, value из словаря
# Если значение ключа целое число, его умножаем 2 перед добавлением в кортеж


def dict_to_list(dict_to_convert):
    list_for_convertion = []
    for k, v in dict_to_convert.items():
        if type(v) == int:
            v *= 2
        list_for_convertion.append((k, v))
    return list_for_convertion


print(dict_to_list({'a': 5, 'b': []}))
# [('a', 10), ('b', [])]

# Задача №2
# Создайте функцию filter_list, которая будет фильтровать список
# У функции должно быть два параметра - саисок и тип значения
# Функция должна вернуть новый список,в  котором останутся только значения того типа, который был передан в вызове функции вторым аргументом
# Функцию можно будет вызвать например так: filter_list([35, True, 'abc', 10], int) b gjkexbnm [35, 10]


def filter_list(list_to_filter, value_type):
    filtered_list = []
    for element in list_to_filter:
        if type(element) == value_type:
            filtered_list.append(element)

        # Not recommended, because bool is subclass of int
        if isinstance(element, value_type):
            filtered_list.append(element)
    return filtered_list


print(filter_list([35, True, 'abc', 10], int))
print(filter_list([35, True, 'abc', 10], str))
print(filter_list([35, True, 'abc', 10], bool))
# [35, 10]
# ['abc']
# [True]


# Решение Задача №2 без цикла, а с использованием встроенной функции filter
def filter_list(list_to_filter, value_type):
    return list(filter(lambda elem: type(elem) is value_type, list_to_filter))


res = filter_list([1, 2, 'abc', True], int)
print(res)
# [1, 2]
