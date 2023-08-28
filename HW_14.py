# Создать цикл, в котором нужно попросить пользователя ввести в терминале два числа
# Вывести результат деления первого числа на второе
# Спросить пользователя, хочет ли он продолжить yes/no
# Ответ no, нужно вйти из цикла
# Иначе всё повторяется сначала

while True:
    try:
        num_one = float(input("Sir please enter the first number: "))
        num_two = float(input("Sir please enter the second number: "))
    except ValueError as e:
        print(e)
        print("You must enter numbers!")
        continue

    print(num_one / num_two)

    answer = input("Sir, do you wanna continue?: (yes/no)")
    if answer == 'no':
        print("Good luck!")
        break
    if answer == 'yes':
        print("Ok, let's try again")
        continue
    else:
        print("Get out")
        break
