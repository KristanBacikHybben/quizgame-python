import datetime

def new_game():
    guesses=[]
    correct_guesses = 0
    question_counter = 1
    for key in questions:
        print("-------------------")
        print(key)
        for i in options[question_counter-1]:
            print(i)
        guess = input("Enter A, B, C or D: ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_counter+=1
    
    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("That was not the right answer :(")
        return 0
    
def display_score(correct_guesses, guesses):
    print("Final results: ")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = int(correct_guesses/len(questions)*100)
    print("Your score is "+str(score)+"%")


def play_again():
    response = input("Do you want to play again?: (yes or no): ").upper()
    if response == "YES":
        return True
    else:
        return False


questions = {
"What is pi's value?: ":"B",
"What color is the sun?: ":"D",
"Which month is the ninth one in a year?: ":"A",
"How is the weather on the Everest right now?: ":"C"
}

options = [["A. 4","B. 3.14","C. 6","D. 8"],
           ["A. Blue","B. Red","C. Pink","D. Yellow"],
           ["A. September","B. January","C. November","D. October"],
           ["A. sunny","B. rainy","C. snowing","D. tornados"]]

new_game()

while play_again():
    new_game()

print("See you soon!")