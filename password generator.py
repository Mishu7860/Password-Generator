import random
import string

def generate_password(length):
    # Define the character sets to be used in the password
    upper = string.ascii_uppercase  # Uppercase letters
    lower = string.ascii_lowercase  # Lowercase letters
    digits = string.digits          # Digits
    symbols = string.punctuation    # Special characters

    # Combine all character sets
    all_characters = upper + lower + digits + symbols

    # Ensure at least one character from each set is included
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random characters from all sets
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Return the generated password as a string
    return ''.join(password)

def main():
    try:
        # Prompt the user to specify the desired password length
        length = int(input("Enter the desired length of the password (minimum 4): "))
        
        if length < 4:
            print("Password length should be at least 4 to include all character types.")
            return
        
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input! Please enter a numeric value for the password length.")

if __name__ == "__main__":
    main()
