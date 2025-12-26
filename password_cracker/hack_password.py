from itertools import product
alphabet = '0123456789'
a = input("Введите пароль: ")
for possible_password in product(alphabet, repeat=3):
    guess = ''.join(possible_password)
    if guess == a:
        print(f"Пароль найден: {guess}")