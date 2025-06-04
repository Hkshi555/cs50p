user = input("Input: ")
output = ""

vowels = ["a","i","u","e","o"]

for char in user:
    if char.lower() in vowels:
        char = ""
    output = output + char
print(output)
