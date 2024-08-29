import random

def generate_password(n_letters, n_symbols, n_numbers):
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '0', 'P', 'Q', 'R', 'S',
        'W', 'X', 'Y', 'Z' ]
    

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    for i in range(n_letters):
        password_list.append(random.choice(letters))

    for i in range(n_symbols):
        password_list.append(random.choice(symbols))

    for i in range(n_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = ''.join(password_list)
    return password

def main():
    print("Welcome to Password Generator!")
    n_letters = int(input("How many letters you want in your password?\n"))
    n_symbols = int(input("How many symbols you want in your password?\n"))
    n_numbers = int(input("How many numbers you want in your password?\n"))

    password = generate_password(n_letters, n_symbols, n_numbers)
    print("Generated Password: ", password)
main()
