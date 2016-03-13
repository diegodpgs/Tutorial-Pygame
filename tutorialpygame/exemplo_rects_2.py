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
        self.background.set_colorkey((0,0,0))
        self.clock = pygame.time.Clock()
        self.posicao_atual = 0 #atributo para saber qual sprite esta sendo blintado na tela
        self.x = 0 #coordenada x do sprite na tela
        self.y = 0 #coordenada y do sprite na tela
        self.sprites = []  
        pygame.key.set_repeat(75)#fazer com que quando a tecla presionada, a acao seja realizada
        #continuamente
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
        c_sprites.image.set_colorkey((0,0,0))
        
        return c_sprites.image
    
    #armazena os recortes das imagens em uma lista    
    def get_sprites(self): 
        self.sprites.append(self.cortar_imagem("char2.png", 158, 0, 90, 100))
        self.sprites.append(self.cortar_imagem("char2.png", 248, 0, 102, 100))
        self.sprites.append(self.cortar_imagem("char2.png", 350, 0, 62, 100))
        self.sprites.append(self.cortar_imagem("char2.png", 412, 0, 84, 100))
        self.sprites.append(self.cortar_imagem("char2.png", 496, 0, 90, 100))

    #metodo que recebe um evento do teclado e que faz o sprite movimentarse 
    def key_pressed(self, key):
        if key == K_LEFT:
            #se o sprite recortado e o primeiro da imagem
            if self.posicao_atual == 0:
               self.posicao_atual = len(self.sprites)-1
            else: self.posicao_atual -= 1			
            self.x = self.x - 10
        if key == K_RIGHT:
            #se o sprite recortado e o ultimo da imagem
            if self.posicao_atual >= len(self.sprites)-1:
               self.posicao_atual = 0
            else: self.posicao_atual += 1
            self.x = self.x + 10
                            
    def run(self):        #passa a imagem que quer ser cortada, a posicao de origem  e o tamanho
        self.surface = self.cortar_imagem("char2.png",498,0,82,117)        self.get_sprites()
        while True:
             self.clock.tick(40)
             for event in pygame.event.get():
                 if event.type == QUIT:
                     return
                 if event.type == KEYDOWN:
                     self.key_pressed(event.key)     
             self.screen.blit(self.background,(0,0))
             self.screen.blit(self.sprites[self.posicao_atual], (self.x,0))
             pygame.display.flip()



game = Jogo("char.png")
game.run()
