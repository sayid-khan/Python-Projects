import random



def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
           computer_guess = random.randint(low, high)
        else:
            computer_guess = low  # could also be high b/c low = high
        feedback = input(f'Is {computer_guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = computer_guess - 1
        elif feedback == 'l':
            low = computer_guess + 1

    print(f'Yay! The computer guessed your number, {computer_guess}, correctly!')


computer_guess(10)