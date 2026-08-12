import random

CONFIG = {
    "options" : [
        "h",
        "t"
    ],
    "namelen" : {
        "min": 2,
        "max": 12
    }
}


# make sure the name is correct, check len and make sure it is made only of letters and not numbers or special characters
def validate_str(name : str):
    if (len(name) < CONFIG["namelen"]["min"] or len(name) > CONFIG["namelen"]["max"]):
        return False
    return name.isalpha()

# introduction sequence
def intro():
    while (True):
        name = input("Name: ")
        if (validate_str(name)):
            print("Welcome, "+name+"!")
            return
    

# make sure that the guess is valid and not "t8340u684695864"
def validate_guess(guess : str):
    for i in range(len(CONFIG["options"])): # check each choice that you can use
        if (CONFIG["options"][i] == str.lower(guess)): # see if the choice = input
            return i # return what choice the user made
    return -1

# print whether or not the guess was correct
def headerortailer_printcorrect(succ : bool, attempts, correct):
    if (succ): # was the guess right? we do seperate prints here to avoid repetition
        print(f"Correct guess!", end="")
    else:
        print(f"Incorrect guess!", end="")
    print(f" Correct: {correct}, Incorrect: {attempts - correct}, Win rate: {round(correct/attempts * 10000) / 100}%") # make the percentage to 2 d.p

# check if the answer is correct
def headerortailer_check(guess : int, answer : int, attempts, correct):
    if (guess == answer):
        correct += 1
    headerortailer_printcorrect(guess == answer, attempts, correct)
    return correct

# main loop function
def headerortailer_loop():
    
    while (True):
        guess = validate_guess(input("Guess (h or t): "))
        ans = random.randint(0, len(CONFIG["options"]) - 1)
        if (guess == -1):
            print("Invalid guess!")
            continue
        attempts += 1
        correct = headerortailer_check(guess, ans, attempts, correct)   # we supply "correct" and "attempts" because of value scope, with "attempts" being for printing
                                                                        # and "correct" so we can update it later

intro()
headerortailer_loop()