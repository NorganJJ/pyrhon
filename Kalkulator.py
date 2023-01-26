print("Калькулятор")
kolvo = int(input("Введите кол-во чисел в операции: "))

number = 2
summary = 0

if kolvo < 2:
    print("Ошибка, вводимое число не может быть меньше двух")
    exit()

number1 = float(input("Введите число: "))
number2 = float(input("Введите число: "))
symbol = input("Выберите операцию операцию из + - / *: ")
if number2 == 0 and symbol == "/":
    print("Ошибка, на ноль делить нельзя")
    number1 = float(input("Введите число: "))
    number2 = float(input("Введите число: "))
    symbol = input("Выберите операцию операцию из + - / *: ")
if symbol == "+":
     summary = number1 + number2
if symbol == "-":
    summary = number1 - number2
if symbol == "/":
    summary = number1 / number2
if symbol == "*":
    summary = number1 * number2
print(summary)

while number < kolvo:
    numberinput = float(input("Введите число: "))
    symbol = input("Выберите операцию операцию из + - / *: ")
    if numberinput == 0 and symbol == "/":
        print("Ошибка, на ноль делить нельзя")
        numberinput = float(input("Введите число: "))
        symbol = input("Выберите операцию операцию из + - / *: ")
    if symbol == "+":
        summary = summary + numberinput
    if symbol == "-":
        summary = summary - numberinput
    if symbol == "/":
        summary = summary / numberinput
    if symbol == "*":
        summary = summary * numberinput
    number +=1
    print(summary)

