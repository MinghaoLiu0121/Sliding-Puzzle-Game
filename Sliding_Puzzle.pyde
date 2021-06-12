
import random

def loadNumberImages():
    
    numbersListNames = ["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png", ""]
    numImages = len( numbersListNames )
    numbersList = [ "" for i in range( numImages ) ]
    for i in range( numImages-1 ):
        numbersList[ i ] = loadImage( numbersListNames[ i ] )
    delay ( 2000 )
    return( numbersList)

def loadButtonImages():
    
    buttonListNames = ["help.png","resetButton.png","playButton.png","exit"]
    numButtons = len( buttonListNames )
    buttonList = [ " " for i in range( numButtons ) ]
    for i in range( numButtons):
        buttonList[ i ] = loadImage( buttonListNames[ i ] )
    delay(2000)
    return(buttonList)

def loadBackGround():
    backGroundNames = ["gameInterface.png","title.png","boardBack.png","gameRule.png"]
    numbackGrounds = len( backGroundNames)
    backGroundLists = [" " for i in range( numbackGrounds )]
                       
    for i in range( numbackGrounds):
        backGroundLists[i] =loadImage( backGroundNames[i])
    delay(2000)
    
    return(backGroundLists)


def setup():
    global numbers, buttons, backGrounds, startFill, numSquares, board, blank, whichSquare
    global squareXShow, squareYShow, squareHeight, squareWidth, startSquareX, startSquareY
    global winCondition, forWin
    
    global titleXshow,titleYshow, titleWidth, titleHeight,title
    global helpX,helpY, helpWidth, helpHeight, help
    global interface, interfaceX, interfaceY, interfaceWidth, interfaceHeight
    global gameRule, gameRuleX, gameRuleY , gameRuleWidth , gameRuleHeight 
    global reset, resetX , resetY, resetWidth, resetHeight 
    global boardBack
    
    global playX, playY, playWidth, playHeight, play
    global buttonBoundaries, numButtons
    global afterShuffle
    global keyStates, numKeys, whichKey, x, y
    global up, down, left, right
    global moveCount

    size(900,900)
    number = 0
    numSquares = 3
    numKeys = 4
    buttonBoundaries = []
    blank = 0
    x = 0
    y = 0
    moveCount = 0
    startFill = 255
    
    #to generate the 2D winCondition
    winCondition = []
    forWin = 0
    board = []

    buttons = loadButtonImages()
    backGrounds = loadBackGround()
    startSquareX = 150
    startSquareY = 100
    squareXShow = startSquareX
    squareYShow = startSquareY
    squareHeight = 200
    squareWidth = 200

    #backGrounds
    interface = 0
    interfaceX = 0
    interfaceY= 0 
    interfaceWidth = 900
    interfaceHeight = 900
    
    title = 1
    titleXshow = 150
    titleYshow = 75
    titleWidth = 600
    titleHeight = 350
    
    gameRule = 3
    gameRuleX = 150
    gameRuleY = 75
    gameRuleWidth = 600
    gameRuleHeight = 550
    
    #buttons
    play = 2
    playX = 250 
    playY = 450
    playWidth = 400 
    playHeight = 150
    
    help = 0
    helpX = 250
    helpY = 650
    helpWidth = 400
    helpHeight = 100
    
    reset = 1
    resetX = 700
    resetY = 700
    resetWidth = 200
    resetHeight = 200
    
    boardBack = 2
    
    whichSquare = -1
    numButtons = len(buttons)
    buttonBoundaries = [True for i in range (numButtons)]
    buttonBoundaries[3] = False
    
    keyStates = False
    whichKey = -1
    up = 0
    down = 1
    left = 2
    right = 3
    
    image(backGrounds[interface], interfaceX, interfaceY, interfaceWidth, interfaceHeight)
    image(backGrounds[title], titleXshow,titleYshow, titleWidth, titleHeight)
    image(buttons[play], playX, playY, playWidth, playHeight)
    image(buttons[help], helpX,helpY, helpWidth, helpHeight)
    
def shuffleBoard():
    global numbers, numSquares, board
    global winCondition
    numbers = loadNumberImages()
    board = []
    afterShufflle = 0
    puzzle = [1,2,3,4,5,6,7,8,9]
    for i in range(numSquares*3):
        puzzle[i] = numbers[i]
        
    #generate shuffled 2D arrray
    afterShuffle = [puzzle[5],puzzle[8],puzzle[4],puzzle[1], puzzle[2], puzzle[3],puzzle[7],puzzle[0], puzzle[6]]
    for i in range(numSquares):
        board.append(afterShuffle[:3])
        afterShuffle= afterShuffle[3:]
        
    #generate 2D winCondition
    winCondition = []
    forWin = 0
    forWin = puzzle
    for i in range(numSquares):
        winCondition.append(forWin[:3])
        forWin = forWin[3:]

    return

def setupGame():
    
    startSquareX = 150
    startSquareY = 100
    squareXShow = startSquareX
    squareYShow = startSquareY
    squareHeight = 200
    squareWidth = 200
    
    image(backGrounds[boardBack], 0, 0, 900, 900)
    image(buttons[reset], 700,700,200,200)
    fill(0,0,0)
    textSize(50)
    text("Use arrow keys to move the tiles", 80,80)
    
    for i in range( numSquares ):
        squareXShow = startSquareX    
        for j in range( numSquares ):    
            fill ( startFill )
            rect( squareXShow, squareYShow, squareWidth, squareHeight )
            squareXShow = squareXShow + squareWidth
        squareYShow += squareHeight

    startSquareX = 150
    startSquareY = 100
    squareXShow = startSquareX
    squareYShow = startSquareY
    squareHeight = 200
    squareWidth = 200

    for i in range(len(board)):
        squareXShow = startSquareX
        for j in range(len(board)):
            if board[i][j] != "":
                image(board[i][j], squareXShow, squareYShow, squareWidth, squareHeight)
                squareXShow = squareXShow + squareWidth
            else:
                squareXShow += squareWidth
        squareYShow +=squareHeight
    return

def mouseReleased():
    global whichSquare, help, buttonBoundaries

    whichSquare = -1
    if (mouseX > helpX) and (mouseX < helpX + helpWidth) and (mouseY > helpY) and (mouseY < helpY + helpHeight):
        if buttonBoundaries[help] == True:
           whichSquare = help
    
    if (mouseX > helpX) and (mouseX < helpX + helpWidth) and (mouseY > helpY) and (mouseY < helpY + helpHeight):
        if buttonBoundaries[help] == True and buttonBoundaries[play] == False :
           whichSquare = 10

    if (mouseX > playX) and (mouseX < playX + playWidth) and (mouseY > playY) and (mouseY < playY + playHeight):
        if buttonBoundaries[play] == True:
            whichSquare = play
            
    if (mouseX > resetX) and (mouseX < resetX + resetWidth) and (mouseY > resetY) and (mouseY < resetY + resetHeight):
        if buttonBoundaries[reset] == True:
            whichSquare = reset

def keyReleased():
    global whichKey, up, down, left, right
    if key == CODED:
        if keyCode == UP:
            whichKey = up
        if keyCode == DOWN:
            whichKey = down
        if keyCode == LEFT:
            whichKey = left
        if keyCode == RIGHT:
            whichKey = right

def moveUp():
    global moveCount, board
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "":
                x = i
                y = j
                break
    if x+1 < 3:
        blank = board[x][y]
        board[x][y] = board[x+1][y]
        board[x+1][y] = blank
        setupGame()
        moveCount += 1

    return(board)
def moveDown():
    global moveCount, board
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "":
                x = i
                y = j
                break
    if x-1> 0 or x-1 == 0:
        blank = board[x][y]
        board[x][y] = board[x-1][y]
        board[x-1][y] = blank
        setupGame()
        moveCount += 1

    return
def moveLeft():
    global moveCount,board
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "":
                x = i
                y = j
                break
    if y+1 < 3:
        blank = board[x][y]
        board[x][y] = board[x][y+1]
        board[x][y+1] = blank
        setupGame()
        moveCount += 1

    return
def moveRight():
    global moveCount,board
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "":
                x = i
                y = j
                break
    if y - 1 > 0 or y -1 == 0:
        blank = board[x][y]
        board[x][y] = board[x][y-1]
        board[x][y-1] = blank
        setupGame()
        moveCount += 1    
    return

def showMove():
    fill(0,0,0)
    textSize(35)
    text("Moves you made:", 100,800)
    text(moveCount, 400,800)


def showWin():
    if board == winCondition:
        fill(0, 0, 255)
        textSize(70)
        text("Congrats", 100,300 )
        text("You solved the puzzle in",50,360)
        text(moveCount,100,420)
        text("moves", 250,420)
    return

def draw():    
    global numbers, buttons, backGrounds, startFill, numSquares, board, blank
    global squareXShow, squareYShow, squareHeight, squareWidth, startSquareX, startSquareY
    global forWin, winCondition
    global titleXshow,titleYshow, titleWidth, titleHeight,title
    global helpX,helpY, helpWidth, helpHeight, help
    global interface, interfaceX, interfaceY, interfaceWidth, interfaceHeight
    global gameRule, gameRuleX, gameRuleY , gameRuleWidth , gameRuleHeight 
    global reset, resetX , resetY, resetWidth, resetHeight 
    global boardBack
    global playX, playY, playWidth, playHeight, play
    global buttonBoundaries, numButtons, removeBoundaries, gameRuleState
    global numberBoundaries, win, afterShuffle, whichSquare
    global x, y, moveCount
    global keyStates, numKeys, whichKey
    
    if whichSquare == help:
        image(backGrounds[gameRule], gameRuleX, gameRuleY , gameRuleWidth, gameRuleHeight )
        buttonBoundaries[play] = False
        whichSquare = -1
        
    if whichSquare == 10:
        image(backGrounds[interface], interfaceX, interfaceY, interfaceWidth, interfaceHeight)
        image(backGrounds[title], titleXshow,titleYshow, titleWidth, titleHeight)
        image(buttons[play], playX, playY, playWidth, playHeight)
        image(buttons[help], helpX,helpY, helpWidth, helpHeight)  
        buttonBoundaries[play] = True
        whichSquare -1  
    
    if whichSquare == play:
        buttonBoundaries[3] = True

        shuffleBoard()
        setupGame()

        fill(0,0,0)
        textSize(35)
        text("Moves you made:", 100,800)
        text(moveCount, 400,800)
        
        buttonBoundaries = [False for i in range(numButtons)]
        buttonBoundaries[reset] = True
        keyStates = True
        whichSquare = -1
        
    if whichSquare == reset:
        shuffleBoard()
        checkWin = winCondition
        setupGame()
        moveCount = 0
        showMove()
        whichSquare = -1
        
    if whichKey == up:
        moveUp()
        showMove()
        showWin()
        whichKey = -1
        
    if whichKey == down:
        moveDown()
        showMove()
        showWin()
        whichKey = -1
        
    if whichKey == left:
        moveLeft()
        showMove()
        showWin()
        whichKey = -1
        
    if whichKey == right:
        moveRight()
        showMove()
        showWin()
        whichKey = -1
        

    
            
