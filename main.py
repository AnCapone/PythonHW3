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
try:
    numberOne = int(input("Please, enter first number: "))
except ValueError as error:
    print("Incorrect input. Only numerical values available!")

try:
    numberTwo = int(input("Please, enter second number: "))
except ValueError as error:
    print("Incorrect input. Only numerical values available!")

if numberOne < numberTwo:
    print("Numbers are not equal: ", numberOne, numberTwo)

elif numberTwo < numberOne:
    print("Numbers are not equal: ", numberTwo, numberOne)

elif numberTwo == numberOne:
    print("Numbers are equal!")
