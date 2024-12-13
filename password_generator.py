import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_characters=True):
    # Define the character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_characters = string.punctuation if use_special_characters else ''
    
    # Combine all selected pools
    all_characters = lowercase + uppercase + digits + special_characters
    
    if not all_characters:
        raise ValueError("At least one character type must be selected!")
    
    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# User input
if __name__ == "__main__":
    try:
        # Validate numeric input
        while True:
            length_input = input("Enter password length (default 12): ")
            if not length_input:  # Default length
                length = 12
                break
            elif length_input.isdigit():  # Valid integer input
                length = int(length_input)
                break
            else:
                print("Please enter a valid number for the password length.")
        
        use_uppercase = input("Include uppercase letters? (y/n, default y): ").lower() in ['y', 'yes', '']
        use_digits = input("Include digits? (y/n, default y): ").lower() in ['y', 'yes', '']
        use_special_characters = input("Include special characters? (y/n, default y): ").lower() in ['y', 'yes', '']
        
        password = generate_password(length, use_uppercase, use_digits, use_special_characters)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
