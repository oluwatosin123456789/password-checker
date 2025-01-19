import re

def is_weak_password(password):
    # Commonly used weak passwords
    common_passwords = [
        "123456", "password", "123456789", "12345678", "12345",
        "1234567", "1234567890", "123123", "000000", "iloveyou",
        "qwerty", "abc123", "letmein", "monkey", "football"
    ]

    # Criteria checks
    if len(password) < 8:
        return "Password is too short (minimum 8 characters)."
    if password in common_passwords:
        return "Password is a commonly used weak password."
    if password.isdigit():
        return "Password contains only numbers."
    if password.isalpha():
        return "Password contains only letters."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."

    return "Password is strong."

def main():
    print("Weak Password Checker")
    print("----------------------")

    while True:
        password = input("Enter a password to check (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Welcome!")
            break

        result = is_weak_password(password)
        print(f"Result: {result}\n")

if __name__ == "__main__":
    main()
