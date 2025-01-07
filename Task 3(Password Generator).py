import random
import string

def generate_password(length):
    """Generate a random password of specified length."""
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure password contains at least one of each type of character
    all_chars = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    """Main function to run the password generator."""
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            password = generate_password(length)
            if password:
                print(f"Generated Password: {password}")

            play_again = input("Do you want to generate another password? (yes/no): ").lower()
            if play_again != "yes":
                print("Thank you for using the Password Generator! Goodbye!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
