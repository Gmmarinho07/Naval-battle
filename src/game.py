import pygame
from settings import *

class Game:
    def __init__(self, screen): # Classe inicial e central do jogo
        self.screen = screen
        self.message = "Clique para iniciar o jogo"

    def handle_event(self, event): # Lida com eventos do jogo
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.message = "Clique detectado!"


    def update(self):
        pass # Atualiza o estado do jogo

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont("arial", 28)
        text = font.render(self.message, True, TEXT_COLOR)
        self.screen.blit(text, (50, 60)) # Desenha o estado atual do jogo na tela



