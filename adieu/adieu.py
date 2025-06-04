import inflect

p = inflect.engine()
names = []

while True:
    try:
        user = input().strip()
        names.append(user)
    except EOFError:
        break

print(f"Adieu, adieu, to {p.join(names, conj="and")}")
