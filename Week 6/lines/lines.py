import sys

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
    elif len(sys.argv) == 2:
        if sys.argv[1].endswith('.py'):
           # Process the Python file
           file = read_file(sys.argv[1])
           num_lines =get_lines_code_count(file)
           print(num_lines)         
        else:
            print("Not a Python file")
    else:
        print("Too many command-line arguments")

def read_file(filename):
    try:
        with open(filename) as f:
            file = f.readlines()
            return file
    except IOError:
            print("File not found")

def get_lines_code_count(file):
    num_lines = 0
    for line in file:
        if line.startswith('#') or line.isspace():
            pass
        else:
            num_lines += 1 
    return num_lines


if __name__ == '__main__':
    main()