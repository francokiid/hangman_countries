from getpass import getpass
from os import system

from word_generator import WordGenerator
from player import Player
from utils.print_sleep import PrintSleep


print_sleep = PrintSleep().ps

class HangmanGame(WordGenerator):
    def __init__(self):
        self.player_name = ""
        self.chances = 7
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
        print_sleep("\n\nThe goal is to save the man from being hung!", 2)
        print_sleep("I will choose a random country, and you have to guess it one letter at a time.", 2)
        print_sleep("Make 7 wrong guesses and you LOSE. The man will die!\n\n", 2)
    
    def login(self):
        while True:
            try:
                name = input("Enter player name: ")
                if not name:
                    raise ValueError
                self.player_name = Player(name)
                self.play_game()
                break
            except ValueError:
                print("Oops! A name is required to play the game.\n")

    def update_display(self):
        for idx, letter in enumerate(self.hidden_word):
            if self.hidden_word[idx] in self.guesses:
                self.display[idx] = letter

    def take_guess(self):
        pass
    
    def check_guess(self):
        pass
                
    def check_win(self):
        pass                
                
    def get_hint(self):
        pass             

    def play_again(self):
        pass
    
    def logout(self):
        pass  
    
    def goodbye(self):
        pass         
                
    def play_game(self):
        self.greeting()
        self.login()

if __name__ == "__main__":
    hangman = HangmanGame()
    hangman.play_game()
