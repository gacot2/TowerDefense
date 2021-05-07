import pygame, sys
import os

from Tower import Tower
from Map import Map
import time 

from Characters import Characters


y = Map(0,0)

WIDTH = 1000
HEIGHT = 700
WIN = pygame.display.set_mode( (WIDTH, HEIGHT) )
FPS = 60

pygame.display.set_caption( "Jeux" )


class Game():

    def __init__(self):
        self.lives = 100
        self.towers = []
        self.characters = [Characters()]

        self.characterNum = len(self.characters)
        self.compteur = 0
        self.l = 0


    def draw_window(self, x, y,character,game):

       
        #draw the map
        WIN.blit( Map.surfaceMap(self), (0, 0) )


        for i in range (self.characterNum):
            WIN.blit(game.characters[i].move(),  (int(0), (int(0)) ) ) 
        



        #draw the tower range
        WIN.blit(x.shooterRange(x.getNormalPosX(), x.getNormalPosY()),  (int(x.getNormalPosX()-x.getNormalPosX()), (int(x.getNormalPosY()-x.getNormalPosY())) ) ) 

        #draw the tower
        WIN.blit(x.surfaceTower(), ( x.getXPos(), x.getYPos() ) )
   
        pygame.display.update()


    def drawCharacters(self,character):

        #character        
        WIN.blit(character.move(),  (int(0), (int(0)) ) ) 
        
         


def main():
    game = Game()
    clock = pygame.time.Clock()
    run = True
    x = Tower(100,200)

    character = game.characters

   


    while run:

        if game.compteur %40 == 0:

                game.characters.append(Characters())
                print("dans le if")
                game.characterNum = game.characterNum +1
                print("ceci est le nombre de personnage ", game.characterNum)



        game.compteur = game.compteur+1

        print(game.compteur)
                


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


        game.draw_window(x,y, character, game)



    pygame.quit()


if __name__ == "__main__":
    main()
