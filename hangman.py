from os import system
from getpass import getpass

from word_generator import WordGenerator
from drawing import Drawing 
from utils.print_sleep import PrintSleep
from utils.boolean import Boolean


print_slp = PrintSleep().print_slp
yes_no = Boolean().yes_no

class HangmanGame:
    def __init__(self):
        self.word_gen = WordGenerator()
        self.drawing = Drawing()
        self.chances = 6
        self.guesses = set()
        self.display = []
        for char in self.word_gen.hidden_word:
            if not char.isalpha():
                self.display.append(char)
            else:
                self.display.append("_")
                
    def greeting(self):
        getpass("\nLet's play a classic game of HANGMAN: COUNTRIES!\n\n\nPress the <ENTER> key to continue...")
        print_slp("\n\nThe goal is to save the man from being hanged.", 2)
        print_slp("I will choose a random country, and you have to guess it one letter at a time.", 2)
        print_slp("For every wrong guess, a new body part is drawn, and the man is brought closer to death.", 2)
        print_slp("Make 6 wrong guesses and you lose!", 3)
    
    def update_display(self):
        for idx, letter in enumerate(self.word_gen.hidden_word):
            if self.word_gen.hidden_word[idx] in self.guesses:
                self.display[idx] = letter

    def get_hint(self):
        if yes_no("\nWould you like a hint? [Y/N] "):
            print_slp(f"\nCapital City: {self.word_gen.words[self.word_gen.hidden_word]}", 3)
            return True
        else:
            return False
    
    def check_guess(self, guess):
        if not guess.isalpha() or len(guess) > 1:
            print_slp("Oops! Guess must be one letter.", 1)
            return
        if guess in self.guesses:
            print_slp("Oops! You already guessed that letter.", 1)
            return
        if guess in self.word_gen.hidden_word:
            print_slp("Yay! You guessed correct.", 1)
        else:
            print_slp("Oops! You guessed wrong.", 1)
            self.chances -= 1
        self.guesses.add(guess)
                
    def check_win(self):
        if "_" not in "".join(self.display):
            print("You win! The man has been saved.")
        else:
            print("You lose! The man has been hanged.")
        print(f"\nCountry: {self.word_gen.hidden_word}")        

    def play_again(self):
        return yes_no("\nGreat game! Would you like to guess another country? [Y/N] ")
    
    def goodbye(self):
        print_slp("\nThank you for playing!", 3)         
                
    def play_game(self):
        got_hint = False
        while self.chances > 0 and "_" in self.display:
            system("cls")
            print("HANGMAN: Guess the country to save the man!\n")
            print(*self.display)
            self.drawing.print_drawing(self.chances)
            guess = input("\nGuess a letter >>> ").upper()
            self.check_guess(guess)
            self.update_display()
            if got_hint is False and self.chances in (range(1, 3)):
                got_hint = self.get_hint()
        system("cls")
        self.check_win()
        self.drawing.print_drawing(self.chances)
            
            
if __name__ == "__main__":
    times_played = 0
    while True:
        game = HangmanGame()
        if times_played == 0:
            game.greeting()
        game.play_game()
        times_played += 1
        if not game.play_again():
            break
    game.goodbye()
