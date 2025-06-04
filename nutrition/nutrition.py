item = input("Item: ").lower()

table = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "kiwifruit": 90,
    "pear": 100,
    "sweet cherries": 100,
}

if item in table:
    print(table[item])
