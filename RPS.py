'''
Play Rock Paper Scisor.

'''
from random import randint

options = ['ROCK', 'PAPER', 'SCISSORS']

display = {
    'won':"congo!!!!!!!!!!!!!!!!",
    'lost':'HeHeHe!!!! Looser',
    'tie':'Just Lucky'
}

def get_userip():
    user_ip = input ("Enter Rock, Paper or Scissors: ")
    user_ip = user_ip.upper()
    return user_ip

def get_pcip():
    pc_ip = options[randint(0,2)]
    return pc_ip

def winner(user_ip=get_userip(), pc_ip=get_pcip()):
    print("your choice: %s" %user_ip)
    print("PC choice: %s" %pc_ip)
    if user_ip==pc_ip:
        print(display["tie"])
    elif ((user_ip==options[0])and(pc_ip==options[2])or\
    ((user_ip==options[1])and(pc_ip==options[0]))or\
    ((user_ip==options[2])and(pc_ip==options[1]))):
        print(display["won"])
    else:
        print(display["lost"])

winner()