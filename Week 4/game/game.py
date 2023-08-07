import sys
import random


def main():
    # get difficulty level from user
    level = get_int_number("level: ")
    # generate a random number between 1 and level
    random_number = random.randint(1, level)
    # initialize guess number to zero
    guess_number = 0

    # start game and quit when guess is correct
    while guess_number!= random_number:
        guess_number = get_int_number("guess: ")

        if guess_number < random_number:
            print("Too Small!")
        elif guess_number > random_number:
            print("Too Large!")
        elif guess_number == random_number:
            sys.exit("Just Right!")


# return a positive integer from the user
def get_int_number(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass


if __name__ == "__main__":
    main()