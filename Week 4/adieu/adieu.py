def main():
    names = []
    while True:
        try:
            user_input = str(input("Name: "))
            names.append(user_input.capitalize())
        except (EOFError, KeyError):
            index = len(names)
            match index:
                case 1:
                    print(f"Adieu, adieu, to {names[0]}")
                case 2:
                    print(f"Adieu, adieu, to {names[0]} and {names[1]}")
                case 3:
                    print(f"Adieu, adieu, to {names[0]}, {names[1]}, and {names[2]}")
                case 4:
                    print(f"Adieu, adieu, to {names[0]}, {names[1]}, {names[2]}, and {names[3]}")
                case 5:
                    print(f"Adieu, adieu, to {names[0]}, {names[1]}, {names[2]}, {names[3]}, and {names[4]}")
                case 6:
                    print(f"Adieu, adieu, to {names[0]}, {names[1]}, {names[2]}, {names[3]}, {names[4]}, and {names[5]}")
                case 7:
                    print(f"Adieu, adieu, to {names[0]}, {names[1]}, {names[2]}, {names[3]}, {names[4]}, {names[5]}, and {names[6]}")
                case _:
                   print("Adieu, adieu, to yieu, yieu, and yieu")
            quit()

if __name__ == "__main__":
    main()