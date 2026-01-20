import requests
import random

license_code = input("Enter your license code: ")
email = input("Enter your email: ")

# Відправка запиту на сервер
try:
    response = requests.get(f"http://127.0.0.1:5000/mottak?license={license_code}&email={email}")
except requests.exceptions.RequestException:
    print("Cannot connect to the license server. Make sure app.py is running.")
    exit()

# Логування
with open("key.txt", "a") as f:
    f.write(f"License: {license_code}, Email: {email}, Result: {response.text}\n")

if response.text == "License approved":
    print("License OK! Let's play the game.")
    number_to_guess = random.randint(1, 50)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess a number between 1 and 50: "))
        except ValueError:
            print("Enter a valid number.")
            continue
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
else:
    print(response.text)
    print("Program terminated.")
