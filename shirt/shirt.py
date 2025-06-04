import sys
from PIL import Image, ImageOps
import os

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    input_ext = input_path.lower().split('.')[-1]
    output_ext = output_path.lower().split('.')[-1]
    valid_extensions = ["jpg", "jpeg", "png"]

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Input and output files must end in .jpg, .jpeg, or .png")

    if input_ext != output_ext:
        sys.exit("Input and output files must have the same extension")

    if not os.path.exists(input_path):
        sys.exit(f"Input file '{input_path}' does not exist")

    try:
        input_image = Image.open(input_path)
        shirt = Image.open("shirt.png")

        size = shirt.size
        resized_input = ImageOps.fit(input_image, size)

        resized_input.paste(shirt, (0, 0), shirt)
        resized_input.save(output_path)

    except FileNotFoundError:
        sys.exit(f"Error: Could not open '{input_path}' or 'shirt.png'")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
