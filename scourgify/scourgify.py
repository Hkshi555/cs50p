import csv
import sys

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r', newline='') as infile, \
             open(output_file, 'w', newline='') as outfile:

            reader = csv.DictReader(infile)
            writer = csv.writer(outfile)

            writer.writerow(['first', 'last', 'house'])

            for row in reader:
                name = row['name'].strip('"')
                last, first = name.split(', ')
                house = row['house']
                writer.writerow([first, last, house])

    except FileNotFoundError:
        sys.exit(f"Error: Could not read input file '{input_file}'.")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
