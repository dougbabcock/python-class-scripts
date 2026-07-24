# DEV 108 Project 2: mad libs
# 07/23/2026
# Doug Babcock

def main():
    print("Welcome to the Mad Libs game!")

    # Ask user if they want to play the game they opened
    play = input("Would you like to play? (yes or no): ")
    if play.lower() != "yes" and play.lower() != "y":   # Testing by roommate determined yes and y should be accepted
        print("Thank you for visiting!")    
        return
    
    # Initialize the counter
    counter = 0

    # Didn't really feel like I needed another function for the game loop
    while True:
        print()
        print("Choose a story:")
        print("1. Python")
        print("2. Dentist")
        print()

        choice = input("Enter your choice (1 or 2): ")
        # Validate the choice
        if choice == "1":
            madPython()
        elif choice == "2":
            madDentist()
        else:
            print("Invalid choice. Please try again.")
            continue    # Go directly to top of loop. Do not pass go. Do not increase counter
        
        # If it passes the validation, we know they played a story
        counter += 1

        # Grammar is great
        if counter == 1:
            print("You have created your first story!")
        else:
            print("You have created", counter, "stories.")

        playAgain = input("Do you want to play again? (yes or no): ")
        if playAgain.lower() != "yes" and playAgain.lower() != "y":     # If it's not a yes, it's a no
            print("Thank you for playing!")
            break   # Breaking loop ends the function, ends the program.
    
# Madlib for python story
def madPython():
    adjective = input("Adjective: ")
    pluralNoun = input("Plural noun: ")
    verb = input("Verb: ")
    noun = input("Noun: ")
    funnyWord = input("Funny word: ")
    number = input("Number: ")
    animal = input("Animal: ")
    exclamation = input("Silly exclamation: ")
    # Triple comments for the absolute win, wish I knew it worked this well when I did project1
    print(f"""
    Today I opened my computer and started writing a Python program. My goal was to
    build a {adjective} app that could {verb} thousands of {pluralNoun} every
    second. First, I imported the mysterious {noun} module and created a function
    named {funnyWord}. Suddenly, my code crashed because I forgot a single colon.
    After fixing it, the terminal proudly displayed {number} successful results.
    My {animal} celebrated by dancing across the keyboard while shouting,
    "{exclamation}!" I finally realized debugging isn't so scary after all.
    """)

# Madlib for dentist story
def madDentist():
    bodyPart = input("Body part: ")
    pluralFood = input("Plural food: ")
    adjective = input("Adjective: ")
    noun = input("Noun: ")
    exclamation = input("Silly exclamation: ")
    food = input("Food: ")
    number = input("Number: ")
    color = input("Color: ")
    animal = input("Animal: ")

    print(f"""
    This morning I visited the dentist because my {bodyPart} hurt after eating too
    many {pluralFood}. The dentist greeted me with a {adjective} smile and handed
    me a shiny {noun}. During the exam I suddenly yelled, "{exclamation}!", making
    everyone laugh. After polishing my teeth until they smelled like {food}, the
    dentist took {number} X-rays. I left carrying a {color} toothbrush, a sticker
    shaped like a {animal}, and a much healthier smile.
    """)

if __name__ == "__main__":
    main()