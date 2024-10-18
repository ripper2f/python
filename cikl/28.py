import random

secret_number = random.randint(1, 100)
guess = 0

print("Я загадал число от 1 до 100. Попробуй угадать!")

while guess != secret_number:
    guess = int(input("Введите Ваше предположение: "))

    if guess < secret_number:
        print("Больше!")
    elif guess > secret_number:
        print("Меньше!")
    else:
        print("Поздравляю! Вы угадали число:", secret_number)
