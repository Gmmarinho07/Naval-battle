import pygame
from settings import *
from board import Board

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.state = STATE_MENU

        self.board = None
        self.message = ""
        self.shots = 0

        self.title_font = pygame.font.SyaFont("arial", 48, bold=True)
        self.text_font = pygame.font.SyaFont("arial", 28)
# Resolvi dividir o jogo em eventos para ter uma cara mais profissional e jogável.

#--------------------
#     EVENTOS
#--------------------

def handle_events(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if self.state == STATE_MENU:
            self.start_game()
        elif self.state == STATE_PLAYING:
            self.handle_click(event.pos)
        elif self.state == STATE_GAME_OVER:
            self.state = STATE_MENU



#--------------------
#    INICIAR JOGO
#--------------------
def start_game(self):
    self.board = Board()
    self.shots = 10
    self.message = "Clique em uma célula"
    self.state = STATE_PLAYING





#--------------------
#    TRATAR CLIQUE
#--------------------



