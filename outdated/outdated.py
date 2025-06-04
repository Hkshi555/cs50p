months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# month-day-year
while True:
    date = input("Date: ").lower().title().strip()



    if "/" in date:
        month, day, year = date.split("/")
        if month.isalpha():
            continue
    elif "," in date:
        year = date.split(" ")[2]
        month =  date.split(" ")[0]
        day = date.split(" ")[1].replace(",", "")

        if month.isdigit():
            continue

        month = months.index(month) + 1
    else:
        continue




    if int(month) > 12:
        continue
    if int(day) > 31:
        continue

    print(f"{year}-{int(month):02}-{int(day):02}")
    break






