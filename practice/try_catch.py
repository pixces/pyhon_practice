# handle errors in a program
try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(f"At age {age} risk is {risk}")
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("invalid value")
