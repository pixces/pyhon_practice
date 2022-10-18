# define a function first and then use
# supply default to the parameter
# while defining keyword arguments, order may change
# while defining position argungts, order has to stay
def greet_user(first_name,last_name):
    print(f"Hi {first_name} {last_name}!")
    print(f"Great to have you aboard")


print("-- start --")
greet_user(last_name="Abdeen",first_name="Zainul")
print("-- end --")


# return value
# default return value is 'None' aka Null,null,nil;
def square(number):
    return number * number


result = square(3)
print(result)