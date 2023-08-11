import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    regex = r'(?:https?://)?\w*\.?youtube.com\/embed\/([a-zA-z0-9]+)\"'
    match = re.search(regex, s, re.IGNORECASE)
    if match:
        return f"https://youtu.be/{match.group(1)}"


if __name__ == "__main__":
    main()