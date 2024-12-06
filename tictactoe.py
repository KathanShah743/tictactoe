import random
def printGameInit():
    print("Enter the desired cell number in the format:")
    print("1 1","|","1 2","|","1 3")
    print("2 1","|","2 2","|","2 3")
    print("3 1","|","3 2","|","3 3")
    print()
def printGame():
    print()
    print(game[0],"|",game[1],"|",game[2])
    print(game[3],"|",game[4],"|",game[5])
    print(game[6],"|",game[7],"|",game[8])
    print()

def rowCheck():
    for i in range(3):
        if game[3*i+0]==game[3*i+1] and game[3*i+1]==game[3*i+2] and game[3*i+2]==game[3*i+0] and game[3*i]!=' ':
            if game[3*i]=='X':
                printGame()
                print("YOU WIN!")
                print()
                quit()
            elif game[3*i]=='O':
                print("YOU LOSE!")
                print()
                quit()
def colCheck():
    for i in range(3):
        if game[0+i]==game[3+i] and game[3+i]==game[6+i] and game[6+i]==game[0+i] and game[i]!=' ':
            if game[i]=='X':
                printGame()
                print("YOU WIN!")
                print()
                quit()
            elif game[i]=='O':
                print("YOU LOSE!")
                print()
                quit()
def diagCheck():
    if game[0]==game[4] and game[4]==game[8] and game[8]==game[0] and game[0]!=' ':
        if game[0]=='X':
            printGame()
            print("YOU WIN!")
            print()
            quit()
        elif game[0]=='O':
            print("YOU LOSE!")
            print()
            quit()
    if game[2]==game[4] and game[4]==game[6] and game[6]==game[4] and game[2]!=' ':
        if game[2]=='X':
            printGame()
            print("YOU WIN!")
            print()
            quit()
        elif game[2]=='O':
            print("YOU LOSE!")
            print()
            quit()
def check():
    rowCheck()
    colCheck()
    diagCheck()
def myMove():
    x,y = input("Enter your move (two numbers separated by a space): ").split()
    a = int(x) - 1
    b = int(y) - 1
    move = 3*a + b
    if a<0 or a>2 or b<0 or b>2:
        print("Invalid move")
        myMove()
    elif game[move]!=' ':
        print("Invalid move")
        myMove()
    else:
        game[move] = 'X'
        check()
def computerMove():
    emptyGame = []
    count = 0
    for i in game:
        if i == ' ':
            emptyGame.append(count)
        count=count+1
    game[random.choice(emptyGame)] = 'O'
    printGame()
    check()
print()
game = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
printGameInit()
k = input("Do you want to move first (y/n): ")
if k=='y':
    for i in range(4):
        myMove()
        computerMove()
    myMove()
elif k=='n':
    for i in range(4):
        computerMove()
        myMove()
    computerMove()
if k=='y':
    printGame()
print("IT'S A DRAW!")
print()
quit()