
items = []
while True:
    try:
        item = input().lower()
        items.append(item.upper())
    except EOFError:
        items.sort()
        dict = {}
        for i in items:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        out = ""
        for item in dict:
            out = out + f"{dict[item]} {item}\n"
        print(out)
        break
