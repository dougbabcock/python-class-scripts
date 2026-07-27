"""
DEV 108 Coding Lab 3
07/14/2026
Doug Babcock
"""

def startQuiz():
    # Initialize score
    score = 0

    # Initialize questions and answers - I used AI to come up with the questions
    questions = [["1. What is the name of Harry Potter\'s owl?\n", "A. Errol", "B. Hedwig", "C. Crookshanks", "D. Fawkes"],
                ["2. Which Hogwarts house does Harry belong to?\n", "A. Slytherin", "B. Hufflepuff", "C. Gryffindor", "D. Ravenclaw"],
                ["3. What position does Harry play on his Quidditch team?\n", "A. Seeker", "B. Chaser", "C. Beater", "D. Keeper"],
                ["4. What platform at King's Cross Station leads to the Hogwarts Express?\n", "A. Platform 9", "B. Platform 10", "C. Platform 9 3/4", "D. Platform 8"],
                ["5. Who is the headmaster of Hogwarts during Harry's time there?\n", "A. Severus Snape", "B. Albus Dumbledore", "C. Minerva McGonagall", "D. Dolores Umbridge"]]
    answers = ["B", "C", "A", "C", "B"]
    userAnswers = []  # I added responses later to have a more robust results section

    # Loop through questions and get user input - this loop took me a while to get working but at least I can add more questions
    for i in range(len(questions)):     # in case we wanted to add more questions - though we'd have to change our results func
        print("-----------------------------------------------------\n")
        j = 0                           # initialize at 0 here so it does not exceed 4 after first loop
        while j <= 4:                   # We know there are 5 columns per row
            # print each column
            print(f"{questions[i][j]}")
            j += 1
        response = getResponse()        # put input in a different function so its easier for me to troubleshoot
        userAnswers.append(response)
        if response == answers[i]:      
            score +=1
            print()
            # input("Correct! Press Enter to continue...")
            print("Correct!")           # edited to improve user experience
        else:
            print()
            print("Incorrect! The correct answer was:", answers[i])
            # input("Press Enter to continue...")    # removed to improve user experience

        print()
    
    displayResults(score, userAnswers, answers)

# Sanitize user response so we get real answers [a-d]
def getResponse():
    response = input("Answer: ").upper()
    
    # Check for valid choice until they pick the correct choice
    # --------------------------------------------------------
    # This used to be an if statement that called getResponse() if it was incorrect,
    # but it still returned the initial unsanitized value, not from the most recent call
    # --------------------------------------------------------
    while response not in ["A", "B", "C", "D"]:
        print("Invalid response. Please enter A, B, C, or D")
        response = input("Answer: ").upper()
    return response
    

def displayResults(score, userAnswers, answers):
    print("************************************\n\n" \
        "Your Results:\n")
    # Print their responses and whether it was correct or not
    i = 0
    for i in range(len(userAnswers)):
        if userAnswers[i] == answers[i]:
            print(f"Question {i+1}: {userAnswers[i]} ✅")
        else:
            print(f"Question {i+1}: {userAnswers[i]} ❌")
    print()
    print(f"Your final score is: {score}\n")
    
    # Give a farewell message
    if score == 5:
        input("A perfect score, good job!\nPress Enter to exit...")
        exit
    elif score == 4:
        input("Great work, almost perfect!\n Press Enter to exit...")
    elif score == 3 or score == 2:
        input("Not too bad, maybe it's time to watch it again!\n Press Enter to exit...")
    else:
        input("You've never seen it, have you?\nPress Enter to exit...")
    
def main():
    print("\n================================\n\n" \
        "Welcome to the Harry Potter Quiz!\n\n" \
        "================================")
    print("\n" * 2)
    ans = input("Would you like to test your Harry Potter knowledge? [Y/n] ").upper()
    if ans == "N":
        print("\nToo bad! Maybe next time")
        return
    else:
        print()
        startQuiz()
    return

if __name__ == "__main__":
    main()