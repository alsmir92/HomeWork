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
print(pc_details.__add__(components))

# Создать два списка
countries = ['Russia', 'China', 'Germany', 'France']
cities = ['Moscow', 'Pekin', 'Berlin', 'Paris']

world = countries + cities

print(world)
