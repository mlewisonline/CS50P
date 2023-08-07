def main():
    users_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    answer_the_question(users_input)

def answer_the_question(input):
    # Remove any whitespace from the input and lower the case
    input = input.strip().lower()

    # Print yes to 42 anything else no
    if input == "forty two" or input == "forty-two" or input =="42":
        print("Yes")
    else:
        print("No")


main()