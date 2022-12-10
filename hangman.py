from os import system
from getpass import getpass

from word_generator import WordGenerator
from utils.print_sleep import PrintSleep
from utils.boolean import Boolean

print_sleep = PrintSleep().ps


class HangmanGame(WordGenerator):
    def __init__(self):
        self.chances = 6
        self.guesses = set()
        self.hidden_word = self.get_country()
        self.display = []
        for char in self.hidden_word:
            if not char.isalpha():
                self.display.append(char)
            else:
                self.display.append("_")
                
    def greeting(self):
        getpass("\nLet's play a classic game of HANGMAN: COUNTRIES!\n\n\nPress the <ENTER> key to continue...")
        print_sleep("\n\nThe goal is to save the man from being hanged!", 2)
        print_sleep("I will choose a random country, and you have to guess it one letter at a time.", 2)
        print_sleep("Make 6 wrong guesses and you lose. The man will die!", 2)
    
    def update_display(self):
        for idx, letter in enumerate(self.hidden_word):
            if self.hidden_word[idx] in self.guesses:
                self.display[idx] = letter

    def take_guess(self):
        pass

    def get_hint(self):
        pass 
    
    def check_guess(self):
        pass
                
    def check_win(self):
        pass        

    def play_again(self):
        pass
    
    def goodbye(self):
        pass         
                
    def play_game(self):
        pass

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
