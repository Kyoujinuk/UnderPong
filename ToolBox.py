import pygame as pg
from Paddle import Paddle
from Ball import ball

#General Setup
Game = True
width = 700
height = 500
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
screen = pg.display.set_mode((width,height))
clock = pg.time.Clock()
ScoreA = 0
ScoreB = 0
ev = pg.event.get()

#This changes the speed depending on the level
Level = 1
Speed = {1:51,2:52,3:53,4:54,5:55,6:56,7:57,8:58,9:59,10:60}

#Paddle setup
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 2
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = width -10
paddleB.rect.y = 200

heart = pg.image.load('img/heart.png')
ball = ball(RED,10,10)
ball.rect.x = 345
ball.rect.y = 195

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pg.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

#Chracter List

SansHead1 = pg.image.load('img/sansHead1.png').convert_alpha()
friskHead = pg.image.load('img/friskHead.png').convert_alpha()
Gblaster = pg.image.load('img/Gaster.png').convert_alpha()

#Menu Screen details
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    def draw(self):
        action = False
        # get mouse position
        pos = pg.mouse.get_pos()
        #check mouse position and click
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draws the buttons on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        return action

FrontScreen = True
Logo = pg.image.load('img/Logo.png').convert_alpha()
Start = pg.image.load('img/Start.png').convert_alpha()
Options = pg.image.load('img/Options.png').convert_alpha()
Quiting = pg.image.load('img/Quit.png').convert_alpha()
StartButton = Button(99,330,Start)
OptionButton = Button(250,330,Options)
QuitButton = Button(500,330,Quiting)

#Options Screen
OptionPage = True
Option = pg.image.load('img/OptionsPage.png').convert_alpha()
Back = pg.image.load('img/Back.png').convert_alpha()
BackButton = Button(60,400,Back)

#Player Selection
PlayerPick = True
OnePlay = pg.image.load('img/OnePlayer.png').convert_alpha()
TwoPlay = pg.image.load('img/TwoPlayer.png').convert_alpha()
OnePlayButton = Button(62,330,OnePlay)
TwoPlayButton = Button(370,330,TwoPlay)

#Level Choice
LevelChoice = True
LevelOne = pg.image.load('img/LevelOne.png').convert_alpha()
Toriel = pg.image.load('img/Toriel.png').convert_alpha
TorielHead1 = pg.image.load('img/TorielHead1.png').convert_alpha()
TorielHead2 = pg.image.load('img/TorielHead2.png').convert_alpha()
TorielHead3 = pg.image.load('img/TorielHead3.png').convert_alpha()
LevelTwo = pg.image.load('img/LevelTwo.png').convert_alpha()
Papyrus = pg.image.load('img/Papyrus.png').convert_alpha()
PapHead1 = pg.image.load('img/PapHead1.png').convert_alpha()
PapHead2 = pg.image.load('img/PapHead2.png').convert_alpha()
PapHead3 = pg.image.load('img/PapHead3.png').convert_alpha()
LevelThree = pg.image.load('img/LevelThree.png').convert_alpha()
LevelFour = pg.image.load('img/LevelFour.png').convert_alpha()
LevelFive = pg.image.load('img/LevelFive.png').convert_alpha()
LevelSix = pg.image.load('img/LevelSix.png').convert_alpha()
LevelSevern = pg.image.load('img.LevelSevern.png').convert_alpha()
LevelEight = pg.image.load('img/LevelEight.png').convert_alpha()
LevelNine = pg.image.load('img/LevelNine.png').convert_alpha()
LevelTen = pg.image.load('img/LevelTen.png').convert_alpha()

LevelDict = {1:LevelOne,2:LevelTwo,3:LevelThree,4:LevelFour,
5:LevelFive,6:LevelSix,7:LevelSevern,8:LevelEight,9:LevelNine,
10:LevelTen}

def Background(Selection):
    screen.fill(BLACK)
    if Selection == FrontScreen:
        screen.blit(Logo,(40,110))
        StartButton.draw()
        OptionButton.draw()
        QuitButton.draw()
    elif Selection == Player:
        screen.blit(Logo,(40,50))
    if 

