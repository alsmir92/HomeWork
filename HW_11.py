# Создайте функцию route_info, которой будет передаватсья словарь.
# Если в словаре есть ключ distance и его значение - целое число, верните строку "Distance to your destination is <distance>
# Иначе, если в словаре есть ключи speed и time, верните строку "Distance to your destination is <speed * time>"
# Иначе верните строку "No distance info is available"
# Вызовите функцию несколько раз с разными аргументами


# Функция без elif else
def route_info(route):
    if ('distance' in route) and (type(route['distance']) == int):
        return f"Distance to your destination is {route['distance']}"

    if ('speed' in route) and ('time' in route):
        return f"Distance to your destination {route['speed'] * route['time']}"

    return "No distance info is available"


# Функция с условными инструкциями if elif else
def route_info(route):
    if ('distance' in route) and (type(route['distance']) == int):
        route_info = f"Distance to your destination is {route['distance']}"
    elif ('speed' in route) and ('time' in route):
        route_info = f"Distance to your destination {route['speed'] * route['time']}"
    else:
        route_info = "No distance info is available"
    return route_info


print(route_info({'distance': 220}))
# Distance to your destination is 220
print(route_info({'speed': 200, 'time': 5.5}))
# Distance to your destination 1100.0
print(route_info({'city': 'Georgia'}))
# No distance info is available
