import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith('.py'):
           # Process the Python file
           file = read_file(sys.argv[1])
           num_lines =get_lines_code_count(file)
           print(num_lines)
        else:
            sys.exit("Not a Python file")


def read_file(filename):
    try:
        with open(filename) as f:
            file = f.readlines()
            return file
    except IOError:
            sys.exit("File not found")

def get_lines_code_count(file):
    num_lines = 0
    for line in file:
        if line.lstrip().startswith('#') or line.isspace():
            pass
        else:
            num_lines += 1
    return num_lines


if __name__ == '__main__':
    main()