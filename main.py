import random
import string

def generate_password(length):
    if length < 4:
        return "Password must be at least 4 characters long!"

    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password = []
    password.append(random.choice(letters))
    password.append(random.choice(numbers))
    password.append(random.choice(symbols))

    all_characters = letters + numbers + symbols
    for _ in range(length - 3):
        password.append(random.choice(all_characters))

    random.shuffle(password)
    return ''.join(password)

while True:
    user_input = input("How many characters should the password have? ")
    if user_input.isdigit():
        user_length = int(user_input)
        break
    else:
        print("Please enter a valid number.")

final_password = generate_password(user_length)
print("Here is your password:", final_password)
