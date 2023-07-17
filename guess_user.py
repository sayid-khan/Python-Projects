import random

def guess(x):
    random_number= random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input(f'guess a random number between 1 and {x}: '))
        if guess < random_number:
         print('sorry, the guess is too low')
        elif guess > random_number:
          print('sorry, the guess is too high')

    print(f'yaay congrats you have gussed the right number {random_number}')

guess(10)



def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback != 'c':
          if low != high:
             guess= random.randint(low,high)
    else:
        guess=low  #could also be high because low=high
    feedback=input(f'Is guess too high(h), too low(l) or correct(c)').lower()
    if feedback=='h':
       high=guess-1
    elif feedback=='l':
       low=guess+1

print(f'yaay! the computer has guessed the number,{guess} correctly')      

computer_guess(10)