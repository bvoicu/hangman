import random

print("This is a Hangman Game")

tari = ["Belgium", "Brazil", "Bulgaria", "Canada", "Chile", "China", "Croatia", "Denmark", "Ecuador", "Egypt", "Estonia", "Finland", "France", "Germany", "Greece", "Japan", "Latvia", "Lithuania", "Luxembourg", 
        "Moldova", "Monaco", "Netherlands", "Peru", "Philippines", "Poland", "Portugal", "Romania", "Russia", "Serbia", "Slovakia", "Slovenia"]


def pick_word():
    word = random.randint(0, len(tari)-1)
    return tari[word]

secret_word = pick_word()

guess = []
guess_str = ""

def build_guess():
    for i in range(len(secret_word)):
        guess.append("._")
    guess_str = ''.join(map(str, guess))
    return guess_str

print(build_guess())

def update_guess():
    litera = str(input("Enter a letter:"))
    for i in range(0, len(secret_word)):
        if litera == secret_word[i]:
            guess[i] = litera
    guess_str = ''.join(map(str, guess))
    return guess_str


while(secret_word != guess_str):
    guess_str = update_guess()
    print(guess_str)
    #print(secret_word)

print("Congrats, the word is", secret_word)
    

