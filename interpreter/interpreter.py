expression = input("Enter expression: ").strip()
split_expression = expression.split(" ")

x = int(split_expression[0])
y = split_expression[1]
z = int(split_expression[2])


# Can be cheated with this
#ans = eval(f"{x} {y} {z}")

match y:
    case "+":
        ans = x + z
    case "-":
        ans = x - z
    case "/":
        ans = x / z
    case "*":
        ans = x * z


print(float(ans))

