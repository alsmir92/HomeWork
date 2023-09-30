# Создать функцию для проверки пароля и email
# Пароль минимум 8 символов
# Пароль содержит: нижний и верхний регистр, цифры, спец. символы
# Ввести пароль в терминале и проверить его
import re


def check_password(password):
    length_pattern = re.compile(r"\S{8,}")
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")
    number_pattern = re.compile(r"^.*[0-9]+.*$")
    special_symb_pattern = re.compile(r"^.*[!@#$*&^?]+.*$")
    no_whitespace_pattern = re.compile(r"^\S*$")

    if not re.fullmatch(no_whitespace_pattern, password):
        return (False, "No whitespaces allowed in the password")

    if not re.fullmatch(length_pattern, password):
        return (False, "Password must have at list 8 symbols")

    if not re.fullmatch(lowercase_pattern, password):
        return (False, "Password must have at least one lowercase letter")

    if not re.fullmatch(uppercase_pattern, password):
        return (False, "Password must have at least one uppercase letter")

    if not re.fullmatch(number_pattern, password):
        return (False, "Password must have at least one number")

    if not re.fullmatch(special_symb_pattern, password):
        return (False, "Password must have at least one special symbol !@#$*&^?")

    return (True, "Password is valid")


def check_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern = re.compile(email_regexp)
    validation_result = 'valid' if email_check_pattern.fullmatch(
        email) else "not valid"
    return (email, validation_result)


# print(check_password('1Ab!df34  s'))
# print(check_password('123'))
# print(check_password('12345678'))
# print(check_password('1234567a'))
# print(check_password('12334WEFef'))

# print(check_email('bs@gmail.com'))
# print(check_email('bsgmail.com'))
# print(check_email('bs@gm.gf.ail.com'))
# print(check_email('bs@gmail.'))
# print(check_email('@gmail.com'))
# print(check_email('b.s@gmail.com'))

while True:
    password = input("Please enter password: ")
    password_check_res = check_password(password)
    if password_check_res[0]:
        print(password_check_res[1])
        break
    print(password_check_res[1])

    email = input("Please enter your email: ")
    email_check_pattern = check_email(email)
    if email_check_pattern[0]:
        print(email_check_pattern[1])
        break
    print(email_check_pattern[1])
