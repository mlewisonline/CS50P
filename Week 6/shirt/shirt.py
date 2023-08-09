import sys
from PIL import Image, ImageOps

def main():
   input, output = check_args()
   try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input_image:
            cropped_image = ImageOps.fit(input_image, shirt.size)
            cropped_image.paste(shirt, mask = shirt)
            cropped_image.save(output)
   except IOError:
        sys.exit("Invalid input")


def check_args():
    if len(sys.argv) < 3:
        sys.exit("Too few Command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many Command-line arguments")
    else:
        if sys.argv[1].endswith('.jpg') and sys.argv[2].endswith('.jpg'):
            return sys.argv[1], sys.argv[2]
        else:
            sys.exit("Invalid input")


if __name__ == "__main__":
    main()