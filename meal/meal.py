def main():
    time = input("Enter time: ").strip()

    converted = convert(time)

    if converted >= 7.0 and converted =< 8.0:
        print("breakfast time")
    elif converted >= 12.0 and converted =< 13.0:
        print("lunch time")
    elif converted >= 18.0 and converted =< 19.0:
        print("dinner time")

def convert(time):
    hour = int(time.split(":")[0])
    minutes = int(time.split(":")[1])


    return float(hour + (minutes / 60))


if __name__ == "__main__":
    main()
