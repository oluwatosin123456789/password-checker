import random
import string

def generate_password(length=12):
    if length < 6:
        print("Password length should be at least 6 characters for strong security.")
        return None

    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password contains at least one character from each pool
    all_characters = lowercase + uppercase + digits + symbols
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    # Return the password as a string
    return ''.join(password)

def main():
    print("Welcome to the Strong Password Generator!")
    try:
        length = int(input("Enter the desired password length (min 6): ").strip())
        password = generate_password(length)
        if password:
            print("\nYour strong password is:", password)
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
