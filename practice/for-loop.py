# numbers = [5,2,5,2,2]

numbers = [2,2,2,2,5]

# basic solution
# for num in numbers:
#    print("X" * num)

for num in numbers:
    pattern = ""
    for x in range(num):
        pattern += "X"
    print(pattern)




