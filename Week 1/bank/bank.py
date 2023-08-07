def main():
    user_input = input("Greeting: ")
    dollar_greeting(user_input)


def dollar_greeting(input):
    input = input.lower().lstrip()
    if input.startswith("hello"):
        print("$0")
    elif input.startswith('h'):
        print("$20")
    else:
        print("$100")

main()