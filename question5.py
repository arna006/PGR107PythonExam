import random 

with open("words.txt", "r") as f:
    words = f.read().splitlines()
    
    word = random.choice(words)
    
    spaces = [" _ "] * len(word)
    
    number_turns = len(word)

    
    
    def get_letter():
        while True:
            guess = input('Guess a letter: ').lower()
            if guess.isalpha() and len(guess) == 1:
                return guess
            else:
                print('invalid input')
                
                
    def update_spaces(guess):
        for i in range(len(word)):
            if word[i] == guess:
                spaces[i] = guess
                
                
    def check_win():
        if '_' not in spaces:
            print('Congratulations, you found the word')
            return True
        else:
            return False
        
    while number_turns > 0:
        print(''.join(spaces))
        guess = get_letter()
        if guess in word:
            update_spaces(guess)
        else:
            print('Sorry, that letter is not in the word.')
            number_turns -= 1
        if check_win():
            break
        print(f'You have {number_turns} turns left')
        print()
        
        if number_turns == 0:
            print(f'Sorry, you lost. The word is {word}')
        
                
        
