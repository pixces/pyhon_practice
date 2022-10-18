message = input("> ")

# split the string by space
words = message.split(" ")

emojis = {
    ":)": "😀",
    ":(": "😞"
}

output = ""

for word in words:
    emoji = emojis.get(word, word)

    output += emoji + " "


print(output)
