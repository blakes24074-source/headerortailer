
correct = 0
attempts = 0

def validate_guess(guess : str):
    try:
        return int(guess)
    except:
        return False

def headerortailer_printcorrect(correct : bool):
    if correct:
        print(f"Correct guess!", end="")
    else:
        print(f"Incorrect guess!", end="")
    print(f" Correct: {correct}, Incorrect: {attempts - correct}, Win rate: {round(correct/attempts * 10000) / 10}%")

def headerortailer_check(guess : int, answer : int):
    if guess == answer:
        correct += 1
    headerortailer_printcorrect(guess == answer)

def headerortailer_loop():
    while True:
        guess = validate_guess(input("Guess: "))
        if not guess:
            continue
        headerortailer_check()