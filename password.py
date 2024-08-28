import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # Includes both uppercase and lowercase letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive integer.")
            return

        use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

        if not (use_letters or use_numbers or use_symbols):
            print("At least one character type must be selected.")
            return

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")

    except ValueError:
        print("Invalid input. Please enter numerical values for length and yes/no for character preferences.")

if __name__ == "__main__":
    main()
