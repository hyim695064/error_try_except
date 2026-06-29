# age = input("enter your age:")
# try:
#     next_year = int(age) + 1

#     print("next year you will be", next_year)
# except ValueError:
#     print("except error")

# a = int(input("first number:"))
# b = int(input("second number:"))
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("dont divide by zero")

# numbers = [10, 20, 30]
# index = int(input("choose index:"))
# try:
#     print(numbers[index])
# except IndexError:
#     print("index not found")

# prices = {"apple": 3, "banana": 5}
# item = input("enter item:")
# try:
#     print(prices[item])
# except KeyError:
#     print("item not found")
# numbers = [100, 200, 300]
# try:
#     index = int(input("choose index:"))
#     divider = int(input("choose divider"))
#     result = numbers[index]/divider
#     print(result)
# except IndexError:
#     print("error is fine")
# except ZeroDivisionError:
#     print("zero error")
# except ValueError:
#     print("error ok")
# try:
#     score = int(input("enter score:"))
#     print("your score is", score)
# except ValueError:
#     print("invalid score")
# finally:
#     print("check finished")
# name = input("enter your name")
# if name == "admin":
#     print("welcome admin")
# else:
#     print("welcome user")
# #syntax error 
# price = 100
# discount = 20
# final_price = price - (price * discount / 100)
# print(final_price)
# print(discount/ 100)
# password = "abc123"
# guess = input("enter password")
# print("guess:", guess, "passsword:",password)
# if guess == password:
#     print("login successful")
# else:
#     print("wrong password")
# try:
#     num1 = int(input("number1"))
#     op = input("operafor")
#     num2 = int(input("number 2"))
#     if op == "+":
#         print(num1+num2)
#     elif op =="-":
#         print(num1-num2)
#     elif op =="*":
#         print(num1*num2)
#     elif op == "/":
#         print(num1/num2)
#     else:
#         print("unknown operator")
# except ZeroDivisionError:
#     print("no zero numbers")
# except ValueError:
#     print("only numbers allowed")
# finally:
#     print("calculate closed")
celsius = input("celsius")
try:
    fahrenheit = int(celsius) * 9 / 5 + 32
    print(fahrenheit)
except ValueError:
    print("temperature must be a number")