import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py <python_file>")

    file_path = sys.argv[1]

    if not file_path.endswith(".py"):
        sys.exit("Error: File name must end with .py")

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("Error: File not found")

    code_lines = 0
    for line in lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith('#'):
            code_lines += 1

    print(code_lines)

if __name__ == "__main__":
    main()
