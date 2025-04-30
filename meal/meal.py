def main():
    time = input("Enter time: ").strip()

    converted = convert(time)
    print(converted)

    if converted :
        print("breakfast time")
    elif converted in range(12, 13):
        print("lunch time")
    elif converted in range(18, 19):
        print("dinner time")

def convert(time):
    hour = int(time.split(":")[0])
    minutes = int(time.split(":")[1])


    return float(hour + (minutes / 60))


if __name__ == "__main__":
    main()
