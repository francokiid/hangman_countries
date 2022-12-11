class Drawing:
    def __init__(self):
        self.hangman = ['''
 ________
 |       |
 |       |
 |       x
 |      /|\\
 |      / \\
_|_''', '''
 ________
 |       |
 |       |
 |       O
 |      /|\\
 |      / 
_|_''', '''
 ________
 |       |
 |       |
 |       O
 |      /|\\
 |      
_|_''', '''
 ________
 |       |
 |       |
 |       O
 |      /|
 |      
_|_''', '''
 ________
 |       |
 |       |
 |       O
 |       |
 |      
_|_''', '''
 ________
 |       |
 |       |
 |       O
 |       
 |      
_|_''', '''
 ________
 |       |
 |       |
 |          
 |           O
 |          /|\\        
_|_         / \\'''] 

    def print_drawing(self, chances):
        print(self.hangman[chances])
        return
