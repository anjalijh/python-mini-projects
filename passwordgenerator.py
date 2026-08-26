# Mini project no.02 : Password Generator

import random
import string

def generate_password(length=8, use_special_chars=True):
    """Generate a random password of the given length."""
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(length))

def main():
    try:
        length = int(input("Password length (default 8): ") or 8)
    except ValueError:
        print("Invalid input, using default length of 8.")
        length = 8

    password = generate_password(length)
    print("Generated password:", password)

if __name__ == "__main__":
    main()
