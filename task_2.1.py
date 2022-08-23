"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""

def calculations():
    oper = input("Choose the operation: '+', '-', '*', '/'. Enter 0 to stop: ")
    if oper == "0":
        return "The process has been stopped."
    elif oper in "+-*/":
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            if oper == '+':
                res = num1 + num2
                print(f"The sum of {num1} and {num2} is: {res}")
                return calculations()
            elif oper == '-':
                res = num1 - num2
                print(f"The difference of {num1} and {num2} is: {res}")
                return calculations()
            elif oper == '*':
                res = num1 * num2
                print(f"The multiplication of {num1} and {num2} is: {res}")
                return calculations()
            elif oper == '/':
                if num2 == 0:
                    print("Can't divided by zero. Choose another second number. ")
                    return calculations()
                else:
                    res = num1 / num2
                    print(f"The division of {num1} and {num2} is: {res}")
                    return calculations()
        except ValueError():
            print("Enter digits not strings. ")
            return calculations()
    else:
        print("The operation sign is not valid. Try again.")
        return calculations()


calculations()
