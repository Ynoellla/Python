#Levi Noell-Baba, July 16, 2023, CPT-168-W17, Lab 10-3
import wordlist

# Get a random word from the word list
def get_word():
    word = wordlist.get_random_word() #random and get function used to get a random word from the wordlist file
    return word.upper()

# Add spaces between letters
def add_spaces(word):
    word_with_spaces = " ".join(word) #spaces added between the letters of the words
    return word_with_spaces

# Draw the display
def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    print("-" * 79) #print function that prints dashes to separate sections
    draw_hangman(num_wrong) #determines what of the hangman figure is drawn based on the num_wrong variable
    print("Word:", add_spaces(displayed_word), #print function that puts spaces between the displayed words
          "  Guesses:", num_guesses, #print function that prints the number of guesses, wrong guesses, and attempts
          "  Wrong:", num_wrong, 
          "  Tried:", add_spaces(guessed_letters))

def draw_hangman(num_wrong): #function that displays portions of the hangman based on number of wrong guesses.
    print("____")
    print("    |") #prints the noose for the hangman
    if num_wrong == 0: #if number wrong is 0 then nothing is printed
        print()
    if num_wrong == 1: #if number wrong is 1 then it prints a capital O for the head
        print("    O")
    elif num_wrong == 2: #if number wrong is 2 then it prints the head and body
        print("    O")
        print("    |\n")
    elif num_wrong == 3: #if the number wrong is 3 then the function prints the head, body, and an arm.
        print("    O")
        print("   \\|\n")
    elif num_wrong == 4: #if the number wrong is 4 then the function prints the head, body, and both arms
        print("    O")
        print("   \\|/\n")
    elif num_wrong == 5: #if the number wrong is 5 then the function prints the head, body, both arms, and the lower body
        print("    O")
        print("   \\|/")
        print("    |\n")
    elif num_wrong == 6: #if the number wrong is 6 then the function prints the head, body, both arms, lower body, and a leg
        print("    O")
        print("   \\|/")
        print("    |")
        print("   /\n")
    elif num_wrong == 7: #if the number wrong is 7 then the function prints the entire hangman
        print("    O")
        print("   \\|/")
        print("    |")
        print("   / \\\n")

# Get next letter from user
def get_letter(guessed_letters): #get_letter function that gets the users guess
    while True:
        guess = input("Enter a letter: ").strip().upper()
    
        # Make sure the user enters a letter and only one letter
        if guess == "" or len(guess) > 1:
            print("Invalid entry. ",
                  "Please enter one and only one letter.")
            continue
        # Don't let the user try the same letter more than once
        elif guess in guessed_letters:
            print("You already tried that letter.")
            continue
        else:
            return guess

# The input/process/draw technique is common in game programming
def play_game():
    word = get_word()
    
    word_length = len(word)
    remaining_letters = word_length
    displayed_word = "_" * word_length

    num_wrong = 0               
    num_guesses = 0
    guessed_letters = ""

    draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    while num_wrong < 7 and remaining_letters > 0: #function that makes sure the player can continue playing
        guess = get_letter(guessed_letters)
        guessed_letters += guess
        
        pos = word.find(guess, 0)
        if pos != -1:
            displayed_word = ""
            remaining_letters = word_length
            for char in word:
                if char in guessed_letters:
                    displayed_word += char
                    remaining_letters -= 1
                else:
                    displayed_word += "_"              
        else:
            num_wrong += 1

        num_guesses += 1

        draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    print("-" * 79)
    if remaining_letters == 0:
        print(f"Congratulations! You got it in {num_guesses} guesses.")   
    else:    
        print("Sorry, you lost.")
        print(f"The word was: {word}")

def main():
    print("Play the H A N G M A N game")
    draw_hangman(7)

    again = "y"
    while again.lower() == "y":
        play_game()
        print()
        again = input("Do you want to play again (y/n)?: ")

    print("Bye!")

if __name__ == "__main__":
    main()
