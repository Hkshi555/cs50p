expression = input("Enter expression: ")
split_expression = expression.split(" ")
x = int(split_expression[0])
y = split_expression[1]
z = int(split_expression[2])
ans = 0

match y:
    case "+":
        ans = x + y
    case "-":
        ans = x - y
    case "/":
        ans = x / y
    case "*":
        ans = x * y

print(float(ans))

