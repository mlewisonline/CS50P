import sys
import csv

def main():
    # Get Args
    before , after = check_args()
    # Read the input CSV file
    before_csv = read_csv_file(before)
    # Sort the input CSV file
    sorted_csv = sort_data(before_csv)
    # Write the sorted CSV file
    write_csv(sorted_csv, after)

def check_args():
    if len(sys.argv) < 3:
        sys.exit("Too few Command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many Command-line arguments")
    else:
        if sys.argv[1].endswith('.csv') and sys.argv[2].endswith('.csv'):
            return sys.argv[1], sys.argv[2]
        else:
            sys.exit(f"Files must end with '.csv'")


def read_csv_file(filename):
    data = []
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
            return data
    except IOError:
        sys.exit(f"Could not read {filename}")

def write_csv(data, output):
    try:
        with open(output, "w", newline='') as output:
            header = ["first", "last", "house"]
            writer = csv.DictWriter(output, fieldnames=header)
            writer.writeheader()
            for row in data:
                last, first = row['name'].split(",")
                house = row['house']
                writer.writerow({"first": first.lstrip(), "last": last, "house": house})
    except IOError:
        sys.exit(f"Could not write {output}")


def sort_data(data):
    sorted(data, key=lambda x: x['name'])
    return data


if __name__ == "__main__":
    main()