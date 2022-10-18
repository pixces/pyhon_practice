customer = {
    "name": "Zainul Abdeen",
    "email": "pixces@yahoo.com",
    "phone": "9742074452",
    "age": 40,
    "is_verified": True
}

print(customer.get("name"))
print(customer.get("oun", False))

# program to ask a number and then return the word for it

# using tupple
# digits = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine",
#     "0": "Zero"
# }

# using list
# digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

phone_number = input("Enter your Phone number: ")
num_in_words = ""
for num in phone_number:
    # digits.get(num,"!")
    num_in_words += digits[int(num)] + " "

print(f"Number {phone_number} converted to {num_in_words}")
