# Создать функцию image_info с одним параметром типа dict
# Функция ожидает словарь, в котором должно быть как минимум два ключа: image_id, image_title
# Функция должна возвращать строку такого вида "Image 'my cat' has id 5136"
# Если хотя бы одного из этих ключей в словаре нет, функция должна генерировать ошибку TypeError
# Вызовите функцию и корректно обработайте ошибку в случае возникновения

def image_info(img):
    if ("image_id" not in img):
        raise TypeError("Key image_id must be present")
    if ("image_title" not in img):
        raise TypeError("Key image_title must be present")
    return f"Image '{img['image_id']}' has id {img['image_title']}"


try:
    print(image_info({'image_id': 'My gun', 'image_title': 100}))
except TypeError as e:
    print(e)

try:
    print(image_info({'image_title': 100}))
except TypeError as e:
    print(e)
