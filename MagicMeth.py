# создать список с 5ю элементами
pc_details = ['Monitor', "Power Block", 'Memory', 'CPU', 'GPU']

print(pc_details)

# удалите третий элемент
pc_details.pop(2)

print(pc_details)

# длину списка
new_long = []

print(len(pc_details))

# поменяйте порядок элементов
pc_details.reverse()

print(pc_details)

# Ещё один список с 2мя элементами
components = ['Mouse', 'Keyboard']

print(components)

# Расширить 1ый список элементами 2го списка
pc_details.extend(components)

print(pc_details)

# Создать два списка
first_list = ['Russia', 'China', 'Germany', 'France']
second_list = [True, False, {'b': 10}, 2.5]

merged_list = first_list + second_list

print(merged_list)

# Мерж листов с магическим методом
other_merged_list = first_list.__add__(second_list)

print(other_merged_list)

# Другой порядок
other_merged_list = second_list.__add__(first_list)

print(other_merged_list)
print()
