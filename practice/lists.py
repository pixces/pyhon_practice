# write a program to find the largest number in a list
# lists are mutables
number_list = [2, 5, 57, 2, 8, 9, 10, 1]
largest_number = number_list[0]

for num in number_list:
    if num > largest_number:
        largest_number = num

print(f"Largest number is: {largest_number}")
