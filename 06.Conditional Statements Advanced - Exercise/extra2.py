import random
import pyautogui

s = "01234567890"
character_list = list(s)
iteration_counter = 0
password = pyautogui.password("Enter your password: ")

guess_password = ""

while guess_password != password:
    guess_password = random.choices(character_list, k=len(password))
    iteration_counter += 1

    print(f">>>>>> {str(guess_password)} <<<<<<")

    if guess_password == list(password):
        print(f"Your password is {''.join(guess_password)} / Number of iteration: {iteration_counter}")
        break