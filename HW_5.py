# Создайте функцию merge_lists_to_dict. У функции должно быть два параметра. Функция должна объединять два списка, используя встроенную функцию zip.
# Конвертируйте объект zip в словарь и верните его из функции.
def merge_lists_to_dict(ammo, countries):
    return dict(zip(ammo, countries))


# Вызовите функцию, передав ей два списка в качестве аргументов. Выведите результат вызова функции в терминал.
weapon = merge_lists_to_dict(
    ['AK-47', 'M16', 'SCAR-L'], ['USSR', 'USA', 'Belgium'])
print(weapon)

weapon_two = merge_lists_to_dict(['Bullet'], [{}, True, 100])
print(weapon_two)

weapon_three = merge_lists_to_dict([10, False, 'cry'], ['Bomb'])
print(weapon_three)
