def main():
    user_input = input("Input: ")
    print(f"Output: {shorten(user_input)}")


def shorten(input):
    output =""
    for letter in input:
        if letter in "aeiouAEIOU":
            pass
        else:
            output += letter
    return output

if __name__ == "__main__":
    main()