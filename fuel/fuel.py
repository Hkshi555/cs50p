


while True:
    frac = input("Fraction: ")

    if "/" not in frac:
        continue

    x, y = frac.split("/")

    try:
        ans = round((int(x) / int(y)) * 100)
        if ans > 100:
            continue
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if ans <= 1:
            print("E")
            break
        elif ans >= 99 and ans <= 100:
            print("F")
            break
        else:
            print(f"{ans}%")
            break


