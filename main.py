import random # random library is used for generating the computers' answer

"""
 CONFIG
  *  Main configuration for this script.

    "options"
      - what options the user can select, will also change the computers' options, making the game harder if increased in size
    "namelen"
      - what lengths of the users' name are acceptable
"""
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


"""
 validate_str
  *  Check if the string supplied is a valid name or not, by
  *     - checking if the name is a vlaid length (customisable)
  *     - checking that the name does not contain any numbers

@param {str} name         =       the name that the user has supplied

@return {bool}            =       whether or not the name is valid
"""
def validate_str(name : str):
    if (len(name) < CONFIG["namelen"]["min"] or len(name) > CONFIG["namelen"]["max"]): # check the length of the name, if it's outside of the valid range, return false
        return False
    return name.isalpha() # check if there are any numbers in the name, if there are, return false, else, return true


"""
 intro
  *  Main intro function, ask what the user's name is, and make sure it is actually a name
"""
def intro():
    while (True):
        name = input("Name: ")
        if (validate_str(name)):
            print("Welcome, "+name+"!")
            return
        print("Invalid name!")

    

"""
 validate_guess
  *  Check if the guess supplied by the user was a valid guess, and return what that guess actually is within CONFIG["options"]

@param {str} guess        =       the input that the user has supplied

@return {int}             =       what the guess of the user is, translated into the index of an option in CONFIG["options"]
"""
def validate_guess(guess : str):
    for i in range(len(CONFIG["options"])): # check each choice that you can use
        if (CONFIG["options"][i] == str.lower(guess)): # see if the input the user has supplied is equal to what the option is called
            return i # return what choice the user made
    return -1 # otherwise, if no choice is found, the guess must be invalid, so return -1


"""
 headerortailer_printcorrect
  *  Feedback to the user to whether or not they guessed wrong, and what their updated stats are.
  *  Prints out whether or not the user was correct, and what their stats (correct guesses, incorrect guesses, win rate) are.

@param {bool} succ        =       whether or not the user guessed the right answer
@param {int} attempts     =       how many times the user has attempted guessing
@param {int} correct      =       how many times the user has guessed correctly
"""
def headerortailer_printcorrect(succ : bool, attempts, correct):
    if (succ): # was the guess right? we do seperate prints here to avoid repetition / weird nested behaviour
        print(f"Correct guess!", end="")
    else:
        print(f"Incorrect guess!", end="")
    print(f" Correct: {correct}, Incorrect: {attempts - correct}, Win rate: {round(correct/attempts * 10000) / 100}%") # make the percentage to 2 d.p


"""
 headerortailer_check
  *  Validate whether or not the guess supplied by the user is valid
  *  Iterate through each option within CONFIG["options"]

@param {int} guess        =       the guess of the user
@param {int} answer       =       the correct answer that the computer has decided
@param {int} attempts     =       how many times the user has attempted guessing, passed to headerortailer_printcorrect for use within calculations
@param {int} correct      =       how many times the user has supplied a correct guess, incremented by 1 if correct, and passed to headerortailer_printcorrect for use within
                                        calculations
@return {int} correct     =       parameter "correct" but incremented by one if guess is correct
"""
def headerortailer_check(guess : int, answer : int, attempts, correct):
    if (guess == answer): # check if the guess is correct
        correct += 1 # increment the correct tally if correct
    headerortailer_printcorrect(guess == answer, attempts, correct) # give feedback to the user, saying if the guess was correct and their updated stats
    return correct # update the main loop with the new correct


"""
 headerortailer_loop
  *  The main loop of the program, primarily for validating user input and storing correct answers/attempts
  *  "correct" is assigned within the function because we have to send "correct" to the functions, which also increment the value if the guess is correct
"""
def headerortailer_loop():
    attempts = 0
    correct = 0
    while (True): # make sure the game loop is eternal!!!!! we don't just want to run the code one single time, that would be boring
        guess = validate_guess(input("Guess (h or t): ")) # get the input from the user
        answer = random.randint(0, len(CONFIG["options"]) - 1) # generate what the correct guess would be, or "answer"
        if (guess == -1): # the validate_guess function returns an integer of the position of a choice within CONFIG["options"], if its -1, it's invalid (see: headerortailer_check)
            print("Invalid guess!")
            continue # skip the current loop, because their guess is invalid!
        attempts += 1
        correct = headerortailer_check(guess, answer, attempts, correct)   # we supply "correct" and "attempts" because of value scope, with "attempts" being for printing
                                                                        # and "correct" so we can update it later


#---------------main
intro() # start by asking the user for their name
headerortailer_loop()