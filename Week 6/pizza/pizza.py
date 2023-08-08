import sys
import csv
from tabulate import tabulate


def main():
    data = read_csv_file(check_args())
    print(tabulate(data[1:], headers = data[0], tablefmt="grid"))


def check_args():
    if len(sys.argv) < 2:
        sys.exit("Too few Command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many Command-line arguments")
    else:
        if sys.argv[1].endswith('.csv'):
            return sys.argv[1]
        else:
            sys.exit("Not a CSV file")


def read_csv_file(filename):
    try:
        with open(filename) as f:
            csv_file = csv.reader(f)
            return list(csv_file)
    except IOError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()