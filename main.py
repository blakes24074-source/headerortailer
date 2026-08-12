import random

CONFIG = {
    "options" : [
        "h",
        "t"
    ]
}

correct = 0
attempts = 0

def validate_guess(guess : str):
    # if guess == "h":
    #     return 0
    # elif guess == "t":
    #     return 1
    for i in range(len(CONFIG["options"])):
        if CONFIG["options"][i] == guess:
            return i
    return -1

def headerortailer_printcorrect(succ : bool, attempt, corr):
    if succ:
        print(f"Correct guess!", end="")
    else:
        print(f"Incorrect guess!", end="")
    print(f" Correct: {corr}, Incorrect: {attempt - corr}, Win rate: {round(corr/attempt * 10000) / 100}%")

def headerortailer_check(guess : int, answer : int, attempt, corr):
    if guess == answer:
        corr += 1
    headerortailer_printcorrect(guess == answer, attempt, corr)
    return corr

def headerortailer_loop(attempt, corr):
    while True:
        guess = validate_guess(input("Guess (h or t): "))
        ans = random.randint(0, len(CONFIG["options"]) - 1)
        if guess == -1:
            print("Invalid guess!")
            continue
        attempt += 1
        corr = headerortailer_check(guess, ans, attempt, corr)

headerortailer_loop(attempts, correct)

