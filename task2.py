import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation

    # Create a pool of characters based on user preferences
    char_pool = ""
    if use_uppercase:
        char_pool += uppercase_letters
    if use_lowercase:
        char_pool += lowercase_letters
    if use_numbers:
        char_pool += numbers
    if use_symbols:
        char_pool += symbols

    # Check if at least one character set is selected
    if not char_pool:
        return "Error: Please select at least one character set."

    # Generate the password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def get_user_input():
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    return length, use_uppercase, use_lowercase, use_numbers, use_symbols

def main():
    print("Welcome to the Random Password Generator!")
    
    while True:
        length, use_uppercase, use_lowercase, use_numbers, use_symbols = get_user_input()
        
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)
        print(f"\nGenerated Password: {password}")
        
        again = input("\nGenerate another password? (y/n): ").lower()
        if again != 'y':
            break

    print("Thank you for using the Random Password Generator!")

if __name__ == "__main__":
    main()