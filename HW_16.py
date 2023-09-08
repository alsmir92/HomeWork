# Создать класс Image
# Image иеет три атрибута: resolution, title, extension
# В классе метод resize (меняет разрешение изображения). Меняем значение атрибута resolution
# Создать несколько экземпляров класса Image и вызвать метод resize

class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extesion = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution

    def __str__(self):
        return f"{self.title}{self.extesion}"


first_image = Image("1920x1080", 'Dog', '.png')

print(first_image.resolution)
print(first_image.title)
print(first_image.extesion)

first_image.resize("2000x4000")

print(first_image.resolution)

second_image = Image("8000x5000", "My cat", '.png')

print(first_image)
print(second_image)

# 1920x1080
# God
# .png
# 2000x4000
# God.png
# My cat.png
