import random


def play():
    user = input("what's yours choice? 'r'for rock, 's' for scissors, 'p' for paper\n")
    computer= random.choice(['r','s','p'])




    def is_win(player,opponent):      # r>s s>p p>r
        if(player=='r'and opponent=='s') or (player=='s'and opponent=='p') \
        or (player=='p'and opponent=='r'):
            return True


    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user,computer):
        return 'you won'

    if is_win(computer,user):
        return 'you lost'
print(play())