greeting = input("Greeting: ").strip().lower()

if greeting.startswith("hello"):
    print("$0")

elif greeting.startswith("h") and not greeting.startswith("hello"):
    print("$20")

else:
    print("$100")
