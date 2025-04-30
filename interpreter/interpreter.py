expression = input("Enter expression: ").strip()
split_expression = expression.split(" ")

x = int(split_expression[0])
y = split_expression[1]
z = int(split_expression[2])

ans = eval(f"{x} {y} {z}")




print(float(ans))

