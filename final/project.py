import re
import random
import string
import sys

def check_length(password, min_length=8):
    return len(password) >= min_length

def check_uppercase(password):
    return bool(re.search(r'[A-Z]', password))

def check_lowercase(password):
    return bool(re.search(r'[a-z]', password))

def check_digits(password):
    return bool(re.search(r'\d', password))


def check_special_chars(password):
    special_chars = "!@#$%^&*()_-+=[]{}\\|;:'\",<.>/?`~"
    count = 0

    for char in password:
        if char in special_chars:
            count+= 1
    if count >= 1:
        return True
    else:
        return False


def check_common_words(password):
    common_words = [
        "password", "123456", "qwerty", "admin", "abcdef",
        "football", "dragon", "welcome", "computer", "secret",
        "hello", "iloveyou"
    ]
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_password = re.sub(r'[^a-zA-Z0-9]', '', password).lower()

    for word in common_words:
        if word in cleaned_password:
            return True
    return False

def calc_pass_score(password):
    score = 0
    feedback = []

    if check_length(password, min_length=8):
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if check_uppercase(password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if check_lowercase(password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if check_digits(password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    if check_special_chars(password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if check_common_words(password):
        feedback.append("Password contains common or easily guessable words. Avoid common words!")

    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1


    if score <= 3:
        strength = "Low Strength Password"
    elif score <= 6:
        strength = "Medium Strength Password"
    else:
        strength = "High Strength Password"

    return strength, feedback, score

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    chars = ""
    password = []

    if use_uppercase:
        chars += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        chars += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        chars += string.digits
        password.append(random.choice(string.digits))
    if use_special:
        special_chars_set = "!@#$%^&*()_-+="
        chars += special_chars_set
        password.append(random.choice(special_chars_set))

    if not chars:
        return ""

    for _ in range(length - len(password)):
        password.append(random.choice(chars))

    random.shuffle(password)
    return "".join(password)


def main():
    print("Welcome to the Password Generator and Checker!")
    while True:
        user_choice = input("\nEnter `gen` for generator, `check` for checker or `quit` to exit: ").lower()

        if user_choice == 'gen':
            length = int(input("Enter password length (default 12): ") or 12)
            use_upp = input("Use upper characters? (default: y) [y/n]: ").lower()
            use_lwr = input("Use lower characters? (default: y) [y/n]: ").lower()
            use_dgts = input("Use digits? (default: y) [y/n]: ").lower()
            use_spcl = input("Use special characters? (default: y) [y/n]: ").lower()

            if use_upp == "y": use_upp = True
            else: use_upp = False
            if use_lwr == "y": use_lwr = True
            else: use_lwr = False
            if use_dgts == "y": use_dgts = True
            else: use_dgts = False
            if use_spcl == "y": use_spcl = True
            else: use_dgts = False

            generated = generate_password(length=length, use_uppercase=use_upp, use_lowercase=use_lwr, use_digits=use_dgts,use_special=use_spcl)
            print(f"Generated Password: {generated}")
            strength, feedback, score = calc_pass_score(generated)
            print(f"Strength: {strength} (Score: {score})")
            if feedback:
                print("Feedback for generated password:")
                for item in feedback:
                    print(f"- {item}")

        elif user_choice == 'check':
            password_to_check = input("Enter a password to check its strength: ")
            strength, feedback, score = calc_pass_score(password_to_check)
            print(f"Strength: {strength} (Score: {score})")
            if feedback:
                print("Feedback:")
                for item in feedback:
                    print(f"- {item}")
            else:
                print("Feedback: Your password looks good!")

        elif user_choice == 'quit':
            print("Exiting. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter `gen`, `check` or `quit`.")

if __name__ == "__main__":
    main()
