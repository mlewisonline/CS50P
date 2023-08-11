import validators

def main():
    response = isemail_vaild(input("What's your email address? ").strip())
    print(response)

def isemail_vaild(address):
    return "Valid" if validators.email(address) else "Invalid"


if __name__ == "__main__":
    main()