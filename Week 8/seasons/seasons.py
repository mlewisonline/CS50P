from datetime import date
import inflect
import sys

n = inflect.engine()

def main():
    date_of_birth = get_date_of_birth(input("Date of Birth: ").strip())
    print(minutes_past(date_of_birth))


def get_date_of_birth(s):
    try:
        year, month, day = s.split("-")
    except ValueError:
        sys.exit("Invalid date")
    else:
        return date.fromisoformat(f"{year}-{month}-{day}")


def minutes_past(date_of_birth):
    delta = date.today() - date_of_birth
    minutes = delta.days * 24 * 60
    return f"{(n.number_to_words(minutes, andword='')).capitalize()} minutes"

if __name__ == "__main__":
    main()