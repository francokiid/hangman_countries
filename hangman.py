from os import system
from getpass import getpass

from word_generator import WordGenerator
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
        pass
    
    def update_display(self):
        for idx, letter in enumerate(self.hidden_word):
            if self.word_gen.hidden_word[idx] in self.guesses:
                self.display[idx] = letter

    def get_hint(self):
        pass 
    
    def check_guess(self):
        pass
                
    def check_win(self):
        pass        

    def play_again(self):
        return yes_no("\nGreat game! Would you like to guess another country? ")
    
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
