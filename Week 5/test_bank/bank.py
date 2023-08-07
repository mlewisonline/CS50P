def main():
    user_input = input("Greeting: ")
    print(f"${value(user_input)}")


def value(input):
    if input.startswith("hello") or input.startswith("HELLO"):
        return 0
    elif input.startswith('h') or input.startswith('H'):
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()