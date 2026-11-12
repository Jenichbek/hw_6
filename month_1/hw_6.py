# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# sym = input("Enter the operation (+, -, *, /): ")
# def numbers():
#     if sym == "+":
#         return num1 + num2
#     elif sym == "-":
#         return num1 - num2
#     elif sym == "*":
#         return num1 * num2
#     elif sym == "/":
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Ошибка: На ноль делить нельзя"
#     else:
#         return "Ошибка: Неверная операция"
# print("Result:", numbers())
# numbers()

# n1 = int(input("Ведите первое число:"))
# n2 = int(input("Ведите второе число:"))
# n3 = int(input("Ведите третье число:"))
# result = lambda n1, n2, n3: n1 > n2 and n1 > n3 and n1 or n2 > n1 and n2 > n3 and n2 or n3 > n1 and n3 > n2 and n3
# print(result(n1, n2, n3))

# price = [1200, 2500, 800, 3500, 1500, 4200]
# sales_tax = list(map(lambda x: x * 0.15, price))
# print("Цены товаров с налогом:", sales_tax)

# age = [12, 18, 25, 16, 30, 14, 21, 17, 45, 19]
# age_18 = list(filter(lambda age: 18 <= age <= 30, age))
# print(age_18)