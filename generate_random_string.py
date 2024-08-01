import random

def generate_password(input_str, number):
    # Seed the random number generator with a combination of input_str and number
    random.seed(input_str + str(number))
    
    # Generate a list of random characters
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password_length = len(input_str) + number
    password = ''.join(random.choice(characters) for _ in range(password_length))
    
    return password

# Contoh penggunaan
input_str = input("Masukkan Kata: ")
number = int(input("Masukkan Angka: "))
password = generate_password(input_str, number)
print(password)
