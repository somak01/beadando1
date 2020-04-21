import string

def game(num):
    player1 = 0
    player2 = 0
    while True:
        try:
            num -= 1
            points = input('2 szam  1-1000 kozott: ')
            point1,point2 = points.split(' ')
            if int(point1)>1000 or int(point1)<1 or int(point2)<1 or int(point2)>1000:
                print('ervenytelen szam')
                continue
            player1 +=int(point1)
            player2 +=int(point2)
            if num==0:
                break
            if player1>player2:
                print('player1 vezet {} ponttal'.format(player1-player2))
            elif player2>player1:
                print('player2 vezet {} ponttal'.format(player2 - player1))
            else:
                print("az allas dontetlen")
        except ValueError:
            print('ervenytelen input')
            continue
    if player1>player2:
        print('player1 nyert {} ponttal'.format(player1-player2))
    elif player2>player1:
        print('player2 nyert {} ponttal'.format(player2-player1))
    else:
        print('dontetlen lett a meccs')




rounds = int(input('add meg a korok szamat: '))
game(rounds)