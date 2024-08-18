# Task 1: Input Length Validator 
# Write a script that asks for and checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

def input_length_validator():
    while True:
        while True:
            first_name = input("Please enter your first name: ")
            last_name = input("Please enter your last name: ")

            if len(first_name) < 2:
                print("Please try again, your first name must be at least two characters long.")
            elif not first_name.isalpha():
                print("Please try again, your first name must contain only alphabetic characters.")
            else:
                print(f"Your first name '{first_name}' fits the format!")

            if len(last_name) < 2:
                    print("Please try again, your last name must be at least two characters long.")
            elif not last_name.isalpha():
                    print("Please try again, your last name must contain only alphabetic characters.")
            else:
                print(f"Your last name '{last_name}' also fits the format!")
                break

        continue_input = input("Would you like to enter more names? (yes/no): ").lower()
        
        if continue_input != 'yes':
            break

input_length_validator()
