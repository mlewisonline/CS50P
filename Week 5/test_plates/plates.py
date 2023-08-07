def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def start_plate_check(plate):
    # Get length of string
    length_of_string = len(plate)
    # Check string between 2 and chars in length
    if length_of_string > 1 and length_of_string < 7 :
        return check_alpha_numeric(plate)
    return False


def check_alpha_numeric(plate):
    for character in plate:
        if not character.isalnum():
            return False
    return check_for_leading_zeros(plate)


def check_for_leading_zeros(plate):
  if plate[0:2].isalpha() and plate.isalnum():
        for index, character in enumerate(plate):
            if character.isdigit():
                if plate[index:].isdigit() and int(character) != 0:
                    return True
                else:
                    return False
        return True


def is_valid(s):
 return start_plate_check(s)


if __name__ == "__main__":
    main()