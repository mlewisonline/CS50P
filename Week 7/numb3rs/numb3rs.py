import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return True if re.search(regex, ip, re.IGNORECASE) else False




if __name__ == "__main__":
    main()