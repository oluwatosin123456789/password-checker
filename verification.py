def verification(phone_number):
    phone_number = str(phone_number).strip()
    
    if phone_number.startswith("+234") or phone_number.startswith("080"):
        return "valid_number"
    else:
        return "invalid_number"

# Prompt the user to input their phone numbers
print("Enter your phone numbers to verify (separate multiple numbers with commas):")
user_input = input("Phone numbers: ")

# Split the input by commas and verify each number
phone_numbers = user_input.split(",")
for phone_number in phone_numbers:
    result = verification(phone_number)
    print(f"Phone number {phone_number.strip()} is {result}.")