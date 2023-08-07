from fractions import Fraction

def main():
    users_fraction = get_fraction_from_user()
    percentage = fraction_to_percentage(users_fraction)
    print(process_result(percentage))


def get_fraction_from_user():
    while True:
        try:
            numerator, denominator = Fraction(input("Fraction: ")).as_integer_ratio()
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if numerator > denominator or denominator == 0:
                pass
            else:
                return numerator, denominator


def fraction_to_percentage(fraction_tuple):
    try:
        numerator, denominator = fraction_tuple
        return round((numerator / denominator) * 100)
    except TypeError:
        return None


def process_result(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()