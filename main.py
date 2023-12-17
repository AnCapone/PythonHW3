# Task 1: Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня.
# Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.

# while True:  # цикл на введення числа
#
#     try:
#         number = int(input("Please enter 1-7 to get the day of week: "))  # зчитування введеного значення
#     except ValueError as error:  # перехоплення помилки з невідповідним значення введення
#         print("Please, enter 1-7 number only!")
#         continue
#     if number < 1 or number > 7:  # перевірка чи знаходиться введене значення в діапазоні від 1 до 7
#         print("Please, enter 1-7 number: ")
#         continue
#
#     break  # вихід з циклу, коли введене коректне число
#
# match number:  # обробка отриманого числа конструкцією match/case
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")


# Task 2. Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у
# порядку зростання
# while True:  # запуск цикла для введення коректного значення першого числа
#     try:
#         numberOne = float(input("Please, enter first number: "))  # зчитування числа з клавіатури. Використовуємо
#         # float для дробних чисел
#     except ValueError as error:  # захоплюємо помилку невірного значення і повертаємось на зчитування числа
#         # до тих пір, поки не буде введене корректне число
#         print("Incorrect input. Only numerical values available!")
#         continue
#     break  # якщо введене коректне число, завершуємо виконання цикла
#
# while True: # запуск цикла для введення коректного значення другого числа (все по аналогії з першим циклом)
#     try:
#         numberTwo = float(input("Please, enter second number: "))
#     except ValueError as error:
#         print("Incorrect input. Only numerical values available!")
#         continue
#     break
#
# if numberOne < numberTwo:  # порівняння чисел та виведення результату
#     print("Numbers are not equal: ", numberOne, numberTwo)
#
# elif numberTwo < numberOne:
#     print("Numbers are not equal: ", numberTwo, numberOne)
#
# elif numberTwo == numberOne:
#     print("Numbers are equal!")

# 3. Користувач вводить два числа та матем дію: + - * або /
# Залежно від введеної матем дії вивести результат
while True:
    try:
        numberOne = float(input("Please, enter first number: "))
    except ValueError as error:
        print("Incorrect input. Use only numerical values!")
        continue
    break

while True:
    try:
        numberTwo = float(input("Please, enter second number: "))
    except ValueError as error:
        print("Incorrect input. Use only numerical values!")
        continue
    break

while True:
    mathOperator = input("Please, enter +, -, *, / to perform a mathematical operation with entered numbers: ")
    match mathOperator:
        case "+":
            print("Sum of entered numbers: ", numberOne + numberTwo)
            break
        case "-":
            print("Difference of entered numbers: ", numberOne - numberTwo)
            break
        case "*":
            print("Product of entered numbers: ", numberOne * numberTwo)
            break
        case "/":
            try:
                print("Quotient of entered numbers: ", numberOne / numberTwo)
                break
            except ZeroDivisionError as error:
                print("Division by zero!")
                break
        case _:
            print("Invalid symbol. Please, use +, -, *, / only!")
            continue