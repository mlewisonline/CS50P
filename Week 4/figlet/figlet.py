import sys
import json
from pyfiglet import Figlet


def main():
    figlet = Figlet()

    # Error handling and Font handling
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            figlet.setFont(font=sys.argv[2])

        elif sys.argv[1] == "-l" or sys.argv[1] == "--list":
            fonts_list = json.dumps(figlet.getFonts())
            # print(json.dumps(figlet.getFonts(), indent=4))
            for font in fonts_list.split(","):
                print(font[2:-2])
            sys.exit(0)
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    # Get Input from user and output to screen using pyfiglet
    user_input = input("Input: ")
    print("Output: ")
    print(figlet.renderText(user_input))


if __name__ == "__main__":
    main()