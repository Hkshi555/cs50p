import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py <csv_file>")

    file_path = sys.argv[1]

    if not file_path.endswith(".csv"):
        sys.exit("Error: File name must end with .csv")

    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            data = list(reader)
    except FileNotFoundError:
        sys.exit("Error: File not found")
    except Exception as e:
        sys.exit(f"Error reading CSV file: {e}")

    print(tabulate(data, headers=header, tablefmt="grid"))

if __name__ == "__main__":
    main()
