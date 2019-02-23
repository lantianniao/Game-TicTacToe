#Tic Tac Toe

import random

def drawBoard(board):
    #画出游戏板，board是一个长度为十的列表，里面有十个长度为一的字符串，只有三种：' ','X','O'
    dash = '-+-+-'
    print(board[6]+'|'+board[7]+'|'+board[8])
    print(dash)
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(dash)
    print(board[0]+'|'+board[1]+'|'+board[2])


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Which letter do you want pick?(X or O)')
        letter = input().upper()
    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

def decideFirst():
    a = random.randint(1,2)
    if a == 1:
        return 'computer'
    if a == 2:
        return 'player'

def playAgain():
    print('Do you want to play again?(input start with \'y\' to continue)')
    return input().lower().startswith('y')

def makeMove(board,letter,step):
    board[step] = letter

def isWinner(bo,le):
    return ((bo[6] == le and bo[7] == le and bo[8] == le)or
            (bo[3] == le and bo[4] == le and bo[5] == le)or
            (bo[0] == le and bo[1] == le and bo[2] == le)or
            (bo[6] == le and bo[3] == le and bo[0] == le)or
            (bo[7] == le and bo[4] == le and bo[1] == le)or
            (bo[8] == le and bo[5] == le and bo[2] == le)or
            (bo[6] == le and bo[4] == le and bo[2] == le)or
            (bo[8] == le and bo[4] == le and bo[0] == le)
            )

def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board,step):
    return board[step] == ' '

def getPlayerMove(board):
    print('此时board是:',end='')
    print(board)
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)-1):
        print('What is your next move?(1-9)')
        move = input()
##    print('玩家要走到'+move+'位置上')
    return int(move)-1

def chooseRandomMoveFromList(board,movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
##    print('此时possibleList是：'+str(possibleMoves))
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
##接下来是电脑AI出招的步骤：
##第一步：判断是否再走某一部可以直接赢下比赛
    for i in range(0,9):
        copyBoard = getBoardCopy(board)
        if isSpaceFree(copyBoard,i):
            makeMove(copyBoard,computerLetter,i)
            if isWinner(copyBoard,computerLetter):
##                print('电脑要走到'+str(i+1)+'位置上')
                return i
##    print('电脑并不能再走一步就获胜！！！！！！！！！！！！！！！！！')
##    第二步：判断玩家是否再走某一步就可以获胜，是的话就返回这个把玩家堵住
    for i in range(0,9):
        copyBoard = getBoardCopy(board)
        if isSpaceFree(copyBoard,i):
            makeMove(copyBoard,playerLetter,i)
            if isWinner(copyBoard,playerLetter):
                print('电脑要走到'+str(i+1)+'位置上')
                return i
##    print('玩家并不能再走一部就获胜！！！！！！！！！！！！！！！')
##    第三步：优先占4角其次占中心，再考虑边
##    占角：
    move = chooseRandomMoveFromList(board,[0,2,6,8])
    if move != None:
##        print('电脑要走到'+str(move+1)+'位置上')
        return move
##    占中心
    if isSpaceFree(board,4):
##        print('电脑要走到5位置上')
        return 4
##    占边,因为没有其他可能了，直接返回即可
##    print('电脑要走到边上了')
    return chooseRandomMoveFromList(board,[1,3,5,7])

def isBoardFull(board):
    for i in board:
        if i == ' ':
            return False
    return True



##函数全部完成，主程序如下：
    
print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 9
    playerLetter , computerLetter = inputPlayerLetter()
    turn = decideFirst()
    print("The "+turn+' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':                                    #玩家走
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard,playerLetter,move)
            if isWinner(theBoard,playerLetter):
                drawBoard(theBoard)
                print('Hooray!You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:                                                       #电脑走
            move = getComputerMove(theBoard,computerLetter)
            makeMove(theBoard,computerLetter,move)
            if isWinner(theBoard,computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you ! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('THe game is a tie!')
                    breake
                else:
                    turn = 'player'

    if not playAgain():
        break
