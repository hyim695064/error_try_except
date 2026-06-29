age = input("enter your age:")
try:
    next_year = int(age) + 1

    print("next year you will be", next_year)
except ValueError:
    print("except error")
