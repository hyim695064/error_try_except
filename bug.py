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

numbers = [10, 20, 30]
index = int(input("choose index:"))
try:
    print(numbers[index])
except IndexError:
    print("index not found")