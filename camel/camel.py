camel = input("camelCase: ")
snake = ""



for char in camel:

    if char.isupper():
        char = f"_{char}".lower()

    snake = snake + char

print(snake)
