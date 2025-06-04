import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip: str) -> bool:
    match = re.fullmatch(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)

    if not match:

        return False
    octets = match.groups()


    for octet_str in octets:
        try:

            octet_int = int(octet_str)

            if not (0 <= octet_int <= 255):

                return False
        except ValueError:
            return False

    return True

if __name__ == "__main__":
    main()
