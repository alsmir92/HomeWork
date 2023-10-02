doc_info = {
    'size': 'A4',
    'color': 'white',
    'format': 'string'
}

style_info = {
    'style': 'TNR'
}

government = {
    'signature': 'manually',
    'color': 'black'
}

union = {  # объединение с оператором **
    **doc_info,
    **style_info,
    **government
}

print(union)

union = doc_info | style_info | government  # объединение с оператором |

print(union)
