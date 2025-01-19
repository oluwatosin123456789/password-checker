# Dictionary to store attendance records
attendance_records = {}

def mark_attendance():
    print("\nWelcome to CMP311 Attendance System")
    name = input("Enter your Name: ").strip()
    matric_number = input("Enter your Matric Number: ").strip()
    department = input("Enter your Department: ").strip()
    
    # Check if matric number already exists
    if matric_number in attendance_records:
        print(f"{matric_number}, ({attendance_records[matric_number]['name']}) has already been marked as Present.")
    else:
        # Add the student to attendance records
        attendance_records[matric_number] = {"name": name, "department": department}
        print(f"Thank you, {name} ({matric_number}) from {department}. You have been marked as Present.")

def main():
    while True:
        print("\n--- Attendance System ---")
        print("1. Mark Attendance")
        print("2. Exit")
        
        choice = input("Enter your choice (1/2): ").strip()
        
        if choice == "1":
            mark_attendance()
        elif choice == "2":
            print("Exiting the Attendance System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the attendance system
main()
