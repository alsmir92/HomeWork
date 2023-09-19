# Создать словарь с ключами разных типов
# Конвертировать в json и вывести результирующее значение с типом значения
# Конвертация в dict обратно

import json


auto_type = {
    'brand': 'BMW',
    'country': 'Germany',
    'price': 100_000_000.0,
    'availability': True,
    'speed': 220,
    'additional': {
        'nom': ['rugs', 'seat-cases', 'flavoring']
    },
    'package': ('full', 'standart')
}

converted_dict = json.dumps(auto_type, indent=2)

print(converted_dict)
print(type(converted_dict))

# {
#   "brand": "BMW",
#   "country": "Germany",
#   "price": 100000000.0,
#   "availability": true,
#   "speed": 220,
#   "additional": {
#     "nom": [
#       "rugs",
#       "seat-cases",
#       "flavoring"
#     ]
#   },
#   "package": [
#     "full",
#     "standart"
#   ]
# }
# <class 'str'>

converted_json = json.loads(converted_dict)
print(converted_json)
# {'brand': 'BMW', 'country': 'Germany', 'price': 100000000.0, 'availability': True, 'speed': 220, 'additional': {'nom': ['rugs', 'seat-cases', 'flavoring']}, 'package': ['full', 'standart']}
