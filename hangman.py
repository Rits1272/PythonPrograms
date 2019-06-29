import random
from collections import Counter

somewords = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

somewords = somewords.split(' ')
word = random.choice(somewords)

print(word)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit.')

    for i in word:
        print('_', end=' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0

    try:
        while(chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input("Enter a letter to guess : "))
            except:
                print('Enter only a letter')
                continue

            # Validation of the guess
            if not guess.isalpha(): #isalpha = isalphabet
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Only a single letter')
                continue
            elif guess is letterGuessed:
                print("You have already guessed that letter")
                continue

            # If letter is guessed correctly 
            if guess in word:
                k = word.count(guess) # k = {'a': 3}
                # k stores the number of times the guess appears in the
                # the secret word

                for _ in range(k):
                    letterGuessed += guess 

            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed)):
                    print(char, end=' ')
                    correct += 1
                # if user has guessed all the letters
                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is : ", end='')
                    print(word)
                    flag = 1
                    print('Congratulations you won!')
                    break
                    break
                else:
                    print('_', end= ' ')
            print()        
            print('You have {} chances left'.format(chances))

            # If user has used all of his chances.
            if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
                print()
                print("You lost! Try again")
                print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print("Bye! Try again.")
        exit()



        





















                    
                    














                
            














            
