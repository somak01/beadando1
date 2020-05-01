import string

def game(num):
    player1 = 0
    player2 = 0
    while True:
        try:
            points = input('Add meg a pontszamokat (2 szam  1-1000 kozott szokozzel elvalasztva): ')
            point1,point2 = points.split(' ')
            if int(point1)>1000 or int(point1)<1 or int(point2)<1 or int(point2)>1000:
                print('ervenytelen szam')
                continue
            player1 +=int(point1)
            player2 +=int(point2)
            num -= 1
            if num == 0:
                break
            if player1>player2:
                print('Player1 vezet {} ponttal'.format(player1-player2))
            elif player2>player1:
                print('Player2 vezet {} ponttal'.format(player2 - player1))
            else:
                print("az allas dontetlen")
        except ValueError:
            print('ervenytelen input')
    print('a vegeredmeny: Player1 {} - {} Player2'.format(player1, player2))
    if player1>player2:
        print('Player1 nyert {} ponttal '.format(player1-player2))
    elif player2>player1:
        print('Player2 nyert {} ponttal '.format(player2-player1))
    else:
        print('dontetlen lett a meccs')

while True:
    try:
        rounds = int(input('add meg a korok szamat:' ))
        game(rounds)
        break
    except ValueError:
        print('hibas input')