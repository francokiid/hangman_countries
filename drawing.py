class Drawing:
  def __init__(self):
    self.hangman = [ ' ' '
 ________
 |       |
 |       |   
 |       O            
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
 |       
 |                      
_|_''',   
     def print_drawing(self,chances):
print(self.hangman[chances])

  return
                                                               
                    
                    
