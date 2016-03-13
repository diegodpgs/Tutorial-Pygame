import os
import pygame
import pygame
from pygame.locals import *

class Jogo:

    def __init__(self, file_name):
        pygame.init()        
        self.screen = pygame.display.set_mode((640,480),0,32)        
        self.surface = pygame.image.load(file_name).convert()
        self.background = pygame.image.load("background.png").convert()

    #metodo que faz cortar uma imagem    
    def cortar_imagem(self, image, x, y, largura, altura):
        #converte para surface a imagem a qual deseja cortar
        image = pygame.image.load(image).convert()
        #cria um rect ( Rect e um objeto que manipula retangulos, ele tem a funcao
        #de obter recortes retangulos das imagems http://www.pygame.org/docs/ref/rect.html
        #passa as coordenadas x, y , altura e largura
        recorte_da_imagem = pygame.Rect((x, y), (largura, altura))
        #cria um objeto sprite
        c_sprites = pygame.sprite.Sprite()
        #recorta a imagem e passa para o sprite
        c_sprites.image = pygame.Surface(recorte_da_imagem.size).convert()
        #desenha a imagem cortada
        c_sprites.image.blit(image, (0,0),recorte_da_imagem)
        
        return c_sprites.image
    
    def run(self):        #passa a imagem que quer ser cortada, a posicao de origem  e o tamanho
        self.surface = self.cortar_imagem("char2.png",498,0,82,117)
        while True:            
             self.screen.blit(self.background,(0,0))
             self.background.blit(self.surface, (0,0))
             pygame.display.flip()



game = Jogo("char.png")
game.run()




    
        
