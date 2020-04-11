import string

def game(num):
    player1 = 0
    player2 = 0
    while num>0:
        points = input('Number between 1-1000: ')
        point1,point2 = points.split('')
        player1 +=point1
        player2 +=point2





rounds = int(input())
print(game(rounds))