import pygame
from pygame.locals import *

class Char:

    def __init__(self):
        self.surface = None        
        self.x = 0
        self.y = 0
        
    def set_x(self, x):
        self.x = x
        
    def set_y(self, y):
        self.y = y
        
    def get_x(self):
        return self.x
        
    def get_y(self):
        return self.y

    def set_surface(self, file_name):
        self.surface = pygame.image.load(file_name).convert()
        self.surface.set_colorkey((0,0,0))
    
class Jogo:

    def __init__(self):
        pygame.init()        
        self.screen = pygame.display.set_mode((640,480),0,32)        
        self.character = Char()
        self.background = None       
        self.clock = pygame.time.Clock();
        pygame.key.set_repeat(75)  
        
    def key_pressed(self, key):

        if key == K_DOWN:
            self.character.set_y(self.character.get_y()+10)
        if key == K_UP:
            self.character.set_y(self.character.get_y()-10)
        if key == K_LEFT:
            self.character.set_x(self.character.get_x()-10)
        if key == K_RIGHT:
            self.character.set_x(self.character.get_x()+10)
            
    def set_background(self, file_name):
        self.background = pygame.image.load(file_name).convert()
        
    def run(self):     
        while True:
             self.clock.tick(40)
             for event in pygame.event.get():
                 if event.type == QUIT:
                     return
                 if event.type == KEYDOWN:
                     self.key_pressed(event.key)
             self.screen.blit(self.background,(0,0))
             self.screen.blit(self.character.surface, (self.character.get_x(),self.character.get_y()))             
             pygame.display.flip()
        
game = Jogo()
game.set_background("background.png")
game.character.set_surface("char.png")
game.run()
