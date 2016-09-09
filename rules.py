# events-example0.py
# Barebones timer, mouse, and keyboard events
import random
import copy
import pyaudio
import wave
import sys

from Tkinter import *
from PIL import Image, ImageTk

def mousePressed(event):
    for elem in cd.textCenters:
        if (event.x > elem[0][0] - 50 and event.x < elem[0][0] + 50):
            if(event.y > elem[1][0] - 50 and event.y < elem[1][0] + 50):
                tmp = cd.textCenters.index(elem)
                if(legalRule(cd.numList[tmp]) == True):
                    cd.cellCenters.pop(tmp)
                    cd.numList.pop(tmp)

                    cd.textCenters = []
                    print "nummyList ", cd.numList
                    if(cd.numList == []):
                        
                        cd.sameRule = False
                        cd.rule += cd.subCount
                        print "theRule ", cd.theRule
                        cd.subCount = 1
                        cd.theRule += 1
                        if(cd.rule > 10):
                            cd.isGameOver = True
                        
                    elif(boardLeg() == False):
                        while(boardLeg() == False):
                            cd.subCount += 1
                            cd.rule -= 1
                        canvas.create_text(60, 10, text = "Now follow rule: " + str(cd.rule))
                    else:
                        cd.sameRule = True
                    break  
                else:
                    pass
                    #cd.mistakes += 1  
                    #print "swahg ", cd.mistakes
        else:
            continue        
    redrawAll()
            
                
def keyPressed(event):
    if(event.keysym == "a"):
        cd.title = False 
    redrawAll()

def timerFired():
    pass
 #   redrawAll()
  #  delay = 250 # milliseconds
   # canvas.after(delay, timerFired) # pause, then call timerFired again

def redrawAll():
    canvas.delete(ALL)
    drawGame()

def legal1(cell):
    stringy = "".join(cell)
    iCell = int(stringy)
    print "celly ", iCell
    for num in cd.numList:
        if num == iCell:
            continue
        tmp = "".join(num)
        print type(tmp)
        print tmp
        print iCell
        print "test ", tmp > iCell
        if int(tmp) > iCell:
            print "LIT"
            return False
        
    return True

def legal2(cell):
    tmp = str(cell[0])
    val = cd.vars[tmp]
    val = str(val[0])
    print val
    if("grn" in val):
        return True

def legal3(cell):
    tmp = str(cell[0])
    tmp = int(tmp)
    if(tmp % 2 != 0):
        return True

def legal4(cell):
    tmp = int(str(cell[0]))
    if(tmp == 9):
        return True

def legal5(cell):
    tmp = str(cell[0])
    val = cd.vars[tmp]
    for elem in val:
        tmp2 = str(elem)
        if(tmp2 == "anim"):
            return True

def legal6(cell):
    tmp = str(cell[0])
    val = cd.vars[tmp]
    for elem in val:
        tmp2 = str(elem)
        if ("Wale" in tmp2):
            return True 

def legal7(cell):
    tmp = str(cell[0])
    val = cd.vars[tmp]
    for elem in val:
        tmp2 = str(elem)
        if ("Mon" in tmp2):
            return True 

def legal8(cell):
    tmp = str(cell[0])
    val = cd.vars[tmp]
    for elem in val:
        tmp2 = str(elem)
        if ("grnMon" in tmp2):
            return True 

def legal9(cell):
    tmp = str(cell[0])
    val = cd.vars[tmp]
    for elem in val:
        tmp2 = str(elem)
        if ("Stache" in tmp2):
            return True 


def legal10(cell):
    tmp = str(cell[0])
    if int(tmp) == 10:
        return True


def boardLeg():
    if(cd.rule == 2):
        for num in cd.numList:
            tmp = int(num[0])
            if tmp == 2 or tmp == 9:
                return True
        return False
    elif(cd.rule == 3):
        for num in cd.numList:
            tmp = int(num[0])
            if tmp % 2 != 0:
                return True
        return False
    elif(cd.rule == 4):
        for num in cd.numList:
            tmp = int(num[0])
            if tmp == 9: 
                return True
        return False
    elif(cd.rule == 5):
        for num in cd.numList:
            tmp = str(num[0])
            elem = cd.vars[tmp]
            if "anim" in elem:
                return True
        return False
    elif(cd.rule == 6):
        for num in cd.numList:
            tmp = str(num[0])
            elem = cd.vars[tmp]
            for wrd in elem:
                if "Wale" in wrd:
                    return True
        return False
    elif(cd.rule == 7):
        for num in cd.numList:
            tmp = str(num[0])
            elem = cd.vars[tmp]
            for wrd in elem:
                if "Mon" in wrd:
                    return True
        return False
    elif(cd.rule == 8):
        for num in cd.numList:
            tmp = str(num[0])
            elem = cd.vars[tmp]
            for wrd in elem:
                if "grnMon" in wrd:
                    return True
        return False
    elif (cd.rule == 9):
        for num in cd.numList:
            tmp = str(num[0])
            elem = cd.vars[tmp]
            for wrd in elem:
                if "Stache" in wrd:
                    return True
        return False
    elif(cd.rule == 10):
        for num in cd.numList:
            tmp = str(num[0])
            if int(tmp) == 10:
                return True
        return False


            

def legalRule(cell):
    rule = cd.rule
    if rule == 1:
        return legal1(cell) 
    elif rule == 2:
        return legal2(cell)
    elif rule == 3:
        return legal3(cell)
    elif rule == 4:
        return legal4(cell)
    elif rule == 5:
        return legal5(cell)
    elif rule == 6:
        return legal6(cell)
    elif rule == 7:
        return legal7(cell)
    elif rule == 8:
        return legal8(cell)
    elif rule == 9:
        return legal9(cell)
    elif rule == 10: 
        return legal10(cell)


def getRule():
    if cd.rule == 1:
        return "Rule 1: Click numbers in descending order"
    elif cd.rule == 2:
        return "Rule 2: Click greens"
    elif cd.rule == 3:
        return "Rule 3: Click all odd numbers"
    elif cd.rule == 4:
        return "Rule 4: Click all nines"
    elif cd.rule == 5:
        return "Rule 5: Click all animals (Unicorns count!)"
    elif cd.rule == 6:
        return "Rule 6: Click all whales"
    elif cd.rule == 7:
        return "Rule 7: Click all monsters"
    elif cd.rule == 8:
        return "Rule 8: Click green monsters"
    elif cd.rule == 9:
        return "Rule 9: Click all mustaches"
    elif cd.rule == 10:
        return "Rule 10: Click all tens"

def drawGame():
    if(cd.title == True):
        canvas.delete(ALL)
        canvas.create_image(cd.canvasWidth/2, cd.canvasHeight/2, image = cd.bg)
        canvas.create_text(cd.canvasWidth/2, cd.canvasHeight/2 - 70, text = "Welcome to Rules! Press 'a' to play!", font = (None, 20), fill = "red")
        canvas.create_image(cd.canvasWidth/2, cd.canvasHeight/2, image = cd.bigUni)
    elif(cd.isGameOver == True):
        canvas.delete(ALL)
        canvas.create_image(cd.canvasWidth/2, cd.canvasHeight/2, image = cd.bg)
        canvas.create_text(cd.canvasWidth/2,10, text = "Game over! 'R' to restart", font = (None, 20))
        cd.title = True

    else:
        canvas.create_rectangle(0,0,cd.canvasWidth, cd.canvasHeight, fill = "gray") #background
        #canvas.create_text(cd.canvasWidth-50, 30, text = "Mistakes: " + str(cd.mistakes))

        if(cd.theRule == cd.rule):
            stringo = getRule()
            canvas.create_text(cd.canvasWidth/2, 30, text = stringo)
        else:
            canvas.create_text(cd.canvasWidth/2, 30, text = "Now follow rule: " + str(cd.rule))
        drawboard()
        drawPieces()


def drawboard():
    for xCell in xrange(cd.rows):
        for yCell in xrange(cd.cols):
            drawCell(xCell, yCell, cd.board[xCell][yCell]) #loops through each elem 

def drawCell(row, col, color):
    top = canvas.data.margin + row*canvas.data.cellSize 
    left = canvas.data.margin + col*canvas.data.cellSize 
    bottom = top + canvas.data.cellSize 
    right = left + canvas.data.cellSize
    canvas.create_rectangle(left, top, right, bottom, fill = color)
    xMid = left+right/2
    yMid = top+bottom/2
    cd.cellCenters.append([[xMid],[yMid]])


def initBoard():
	emptyColor = "tan"
	cd.emptyColor = emptyColor
	board = []
	board = [[emptyColor]*cd.cols for x in xrange(cd.rows)]

	cd.board = board

def initVars():
    varDict = dict()
    varDict["1"] = ["yelMon"]
    varDict["2"] = ["grnMon"]
    varDict["3"] = ["bluMon"]
    varDict["4"] = ["redMon"]
    varDict["5"] = ["bluRob"]
    varDict["6"] = ["BluWale", "anim"]
    varDict["7"] = ["redFox", "anim"]
    varDict["8"] = ["yelStache"]
    varDict["9"] = ["grnPhn"]
    varDict["10"] = ["gryUni", "anim"]

    return varDict

def genNumLst():
    lst = []
    for x in xrange(16):
        lst.append(random.sample(cd.vars, 1))
    return lst

def getThing(dictEn):
    tmp = dictEn[0]
    if(tmp == "grnMon"):
        return cd.grnMonIm
    elif (tmp == "redMon"):
        return cd.redMonIm
    elif (tmp == "bluMon"):
        return cd.bluMonIm
    elif (tmp == "BluWale"):
        return cd.whaleIm
    elif (tmp == "grnPhn"):
        return cd.grnPhnIm
    elif(tmp == "bluRob"):
        return cd.bluRobIm
    elif(tmp == "yelMon"):
        return cd.yelMonIm
    elif(tmp == "redFox"):
        return cd.redFoxIm
    elif(tmp == "gryUni"):
        return cd.gryUniIm
    elif(tmp == "yelStache"):
        return cd.yelStacheIm
    else:
        return None

def drawPieces():
    if(cd.sameRule == False):
        cd.numList = genNumLst()
        if boardLeg() == False:
            while(boardLeg() == False):
                cd.numList == genNumLst()
                print "whoa buddy"
                drawPieces()
                
    cd.sameRule = True

    for thing in cd.cellCenters:
        xCent = thing[0][0]
        yCent = thing[1][0]
        index = cd.cellCenters.index(thing)
        tmp = cd.numList[index]
        wrd = tmp[0]
        dictEn = cd.vars[wrd]
        sprite = getThing(dictEn)
        
        
        
       # canvas.create_image(((xCent)/1.5)+14,((yCent)/1.5)+14,image = im)
       # cd.imageCenters.append([[(xCent/1.5)+14], [(yCent/1.5) +14]])
        canvas.create_image(((xCent)/1.5)+40, ((yCent)/1.5)+30, image = sprite)

        canvas.create_text(((xCent)/1.5), ((yCent)/1.5), text = "".join(cd.numList[index]), font = (None, 13))

        cd.textCenters.append([[(xCent/1.5)], [(yCent/1.5)]])



def init():
    #background image:
    #http://img04.deviantart.net/b852/i/2009/252/4/4/bursty_sparkly_texture_6_by_asphyxiate_stock.jpg
    cd.bg = ImageTk.PhotoImage(Image.open("sparkles.jpg"))
    #whale image:
    #http://redbluegames.tumblr.com/post/87614545448/art-showcase-mini-fish-whale
    cd.whaleIm = ImageTk.PhotoImage(Image.open("whale.png"))
    #monster image:
    #http://pixelbeef.tumblr.com/
    cd.redMonIm = ImageTk.PhotoImage(Image.open("redMon.png"))
    cd.bluMonIm = ImageTk.PhotoImage(Image.open("bluMon.png"))
    cd.grnMonIm = ImageTk.PhotoImage(Image.open("grnMon.png"))
    cd.yelMonIm = ImageTk.PhotoImage(Image.open("yelMon.png"))
    #phone image:
    #https://www.iconfinder.com/icons/523569/avatar_cartoon_character_game_gaming_monster_pixel-art_icon
    cd.grnPhnIm = ImageTk.PhotoImage(Image.open("grnPhone.png"))
    #robot image:
    #http://nuclear-throne.wikia.com/wiki/Robot
    cd.bluRobIm = ImageTk.PhotoImage(Image.open("bluRobot.png"))
    #fox image:
    #http://fc08.deviantart.net/fs71/f/2012/220/d/c/fox_pixel_by_pokejade-d5abexj.png
    cd.redFoxIm = ImageTk.PhotoImage(Image.open("fox.png"))
    #unicorn image:
    #http://orig04.deviantart.net/1ccc/f/2013/142/6/c/rainbow_unicorn_pixel_by_foxdj-d665q9e.gif
    cd.gryUniIm = ImageTk.PhotoImage(Image.open("unicorn.png"))
    cd.bigUni = ImageTk.PhotoImage(Image.open("bigunicorn.png"))
    
    #mustache art:
    #http://n7ugc.disney.go.com/item/Monkey_Lover266/412_2gs11k6VR60S00001004wDM0-h-eb253a-as/mustache!!__600_450_q50.jpg
    cd.yelStacheIm = ImageTk.PhotoImage(Image.open("stache.png"))

    cd.vars = initVars()
    initBoard()
    drawGame()
    

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    canvas = Canvas(root, width=550, height=550)
    rows = 4
    cols = 4
    margin = 75
    cellSize = 100
    canvasWidth = 2*margin + cols*cellSize
    canvasHeight = 2*margin + rows*cellSize
    score = 0
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    global cd 
    cd = canvas.data
    cd.cellSize = cellSize
    cd.rows = rows
    cd.cols = cols
    cd.canvasWidth = canvasWidth
    cd.canvasHeight = canvasHeight
    cd.margin = margin
    cd.score = score
    cd.board = []
    cd.cellCenters = []
    cd.textCenters = []
    cd.imageCenters = []
    cd.isGameOver = False
    cd.rule = 1
    cd.sameRule = False
    cd.numList = []
    cd.subCount = 1
    cd.theRule = 1
    cd.mistakes = 0 
    cd.title = True
    init()
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()

