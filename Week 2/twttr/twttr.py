def main():
    user_input = input("Input: ")
    print(f"Output: {remove_vowels(user_input)}")



def remove_vowels(input):
    vowels = "aeiouAEIOU"
    output =""
    for letter in input:
        if letter in vowels:
            pass
        else:
            output += letter
    return output

main()