from word_generator import WordGenerator
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
        pass
    
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
                
    def play_game(self):
        pass
        
