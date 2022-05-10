import random
from phrase import Phrase

class Game:

    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase("hello World"),
                        Phrase("there is no trying"),
                        Phrase("may the force be with you"),
                        Phrase("you have to see the matrix for yourself"),
                        Phrase("life is like a box of chocolates")]
        
        
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
    
    def get_random_phrase(self):
        return random.choice(self.phrases)
    
    def welcome(self):
        print("============================")
        print("  Welcome to Phrase Hunter  ")
        print("============================")

        print("Number missed:", f"{self.missed}")
        self.active_phrase.display(self.guesses)

        
        
        
    def start(self):
        self.welcome()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            self.user_guess = self.get_guess()
            self.guesses.append(self.user_guess)
            if not self.active_phrase.check_guess(self.user_guess):       
                self.missed += 1
                print(f"Number missed: {self.missed}")
            
            self.active_phrase.display(self.guesses)
        
        self.game_over()
        

    def get_guess(self):
        while True:
            letter = input("\nEnter a letter: ").lower()
            if len(letter) == 1 and letter.isalpha():
                break
            else:
                if len(letter) != 1:
                    print("Enter only one letter please!")
                if not letter.isalpha():
                    print('Enter a letter please!')
                    
        self.guesses.append(letter)

        return letter

    def game_over(self):
        if  self.active_phrase.check_complete(self.guesses):
            print("\n Contratulations! You won!")
            
            return True

        elif self.missed == 5:
            print("\n You lose!")
            return True
        else:
            return False

    
   


        

    
    
