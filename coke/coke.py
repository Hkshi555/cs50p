accepted = [25,10,5]

price = 50


while price > 0:
    coin = int(input("Insert coin: "))


    if coin in accepted:
        price = price - coin
        if price <= 0:
            print(f"Change Owed: {abs(price)}")
            continue
        print(f"Amount due: {price}")
    else:
        print(f"Amount due: {price}")
        continue

