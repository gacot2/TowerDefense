import pygame, sys
import os
from Tower import Tower
from Map import Map
import time 
from Characters import Characters
from GrayEnemy import GrayEnemy
import random
from GrayTurret import GrayTurret
from BrownEnemy import BrownEnemy


y = Map(0,0)

WIDTH = 1000
HEIGHT = 700
WIN = pygame.display.set_mode( (WIDTH, HEIGHT) )
FPS = 60
RED = (255,0,0)

pygame.display.set_caption( "Jeux" )


class Game():

    def __init__(self):
        self.lives = 50
        self.towers = [GrayTurret(100,200), Tower(800,200), Tower(500,600)]
        self.characters = []

        self.characterNum = len(self.characters)
        self.towerNum = len(self.towers)
        self.compteur = 0
        self.objectCount = 0

        self.gameLife = 100

        self.test = 0



    def gameDmg(self):

        for i in range (self.characterNum):
           # print("pos de 0 ",self.characters[0].isVisible())

            if self.characters[i].getYPos() >= 650 and self.characters[i].isVisible() == True and self.characters[i].getDmgCount() !=0:

                self.gameLife = self.gameLife - self.characters[i].getDmg()

                self.characters[i].decDmgCount()
                print("dans if")


    def getGameLife(self):

        return self.gameLife


    def draw_window(self,game):

       
        #draw the map
        WIN.blit( Map.surfaceMap(self), (0, 0) )

        #draw characters
        self.drawCharacters()





        #draw the towers and their range 
        for tower in range (self.towerNum):

            WIN.blit(self.towers[tower].shooterRange(self.towers[tower].getNormalPosX(), self.towers[tower].getNormalPosY()),  (int(self.towers[tower].getNormalPosX()-self.towers[tower].getNormalPosX()), (int(self.towers[tower].getNormalPosY()-self.towers[tower].getNormalPosY())) ) ) 
            WIN.blit(self.towers[tower].surfaceTower(), ( self.towers[tower].getXPos(), self.towers[tower].getYPos() ) )

        pygame.display.update()


    #Draw the characters on the map
    def drawCharacters(self):

        #character
        for i in range (self.characterNum):
            if self.characters[i].isVisible():

                self.characters[i].drawHealthBar(WIN)

                WIN.blit(self.characters[i].move(self.characters[i]), ( (self.characters[i].getXPos()), (self.characters[i].getYPos()))  ) 
                

    """
        TODO: faire certain que les enemies perdes leurs vies
    """

    def towerAttack(self):

        for tower in range (self.towerNum-1):

            for i in range (self.characterNum-1):

                    if self.characters[i].getXPos() > self.towers[tower].getShootingZoneX(0) and self.characters[i].getXPos() < self.towers[tower].getShootingZoneX(1) and self.characters[i].getYPos() > self.towers[tower].getShootingZoneY(0)and self.characters[i].getYPos() < self.towers[tower].getShootingZoneY(1):

                        self.characters[i].getAttacked()



                       



    #add the different characters to the game every x seconds
    def addCharacters(self):

        if self.compteur %30 == 0:


                randomEnemy = [Characters(),GrayEnemy(), BrownEnemy()]

                randomNumber = random.randint(0,2)

                self.characters.append(randomEnemy[randomNumber])

                self.characterNum = self.characterNum +1

                self.objectCount = self.objectCount + 1


                


def main():
    game = Game()
    clock = pygame.time.Clock()
    run = True
   
    
    character = game.characters


    while run:

        game.addCharacters()

        game.towerAttack()

        game.gameDmg()
        print("this is game life", game.getGameLife())
        
       


        game.compteur = game.compteur+1

        #print(game.compteur)
        #print(game.characters[game.objectCount].checkDelete())

        

        isclicked = True
        # clock
        clock = pygame.time.Clock()
        run = True
        # make sure that we dont go over 60 fps
        clock.tick( FPS )

        # liste des différents évènements
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                #Change the position of a tower at the clicked position
                #x.changePos(x)

                #print("ceci est x ",x.getXPos())
                #print("Ceci est Y ",x.getYPos())
                print(pygame.mouse.get_pos())


        game.draw_window(game)



    pygame.quit()


if __name__ == "__main__":
    main()
