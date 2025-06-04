import random


def main():
    correct = 0
    level = get_level()

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        attempts = 0

        while attempts < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == answer:
                    correct += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1

        if attempts == 3:
            print(f"{x} + {y} = {answer}")

    print(f"Score: {correct}/10")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass
        print("Invalid level. Please enter 1, 2, or 3.")


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")


if __name__ == "__main__":
    main()
