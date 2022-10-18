# write a program to remove duplicates in a list

# by updating the input list
list = [1, 2, 5, 7, 8, 9, 1, 5, 7, 6]
# list.sort()

print(list)
for item in list:
    if list.count(item) > 1:
        list.pop(list.index(item))

print(list)


# not updaing the input list
list = [1, 2, 5, 7, 8, 9, 1, 5, 7, 6]
new_list = []

for num in list:
    if num not in new_list:
        new_list.append(num)



print(list)
print(new_list)