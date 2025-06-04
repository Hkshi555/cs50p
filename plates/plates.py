def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

marks = [" ", ".", ","]
def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False


    for char in range(0,1):
        if s[char].isdigit():
            return False

    for char in s:
        if char in marks:
            return False


    if s[-1].isdigit() and s[-2].isalpha():
        return False


    digits = ""
    for char in s:
        if char.isdigit():
            digits = digits + char
    if digits.startswith("0"):
        return False



    return True
main()
