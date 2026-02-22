import pygame
from settings import *
from board import Board
from board import Board

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.message = "Clique para iniciar o jogo"
        self.board = Board()  # Cria tabuleiro do jogo

        self.message = "Clique em uma célula"
        self.shots = 10
        self.game_over = False

        # Carregar as imagens para ficar bonito kkk
        # Aqui estou usando o convert.alpha para otimizar a renderização das imagens para elas respeitarem o limite das telas,
        # o .alpha faz ainda melhor mantento a transparência das imagens, o que é importante para as imagens de água, acerto e erro.
        self.images = {
            "water": pygame.image.load("assets/images/water.png").convert_alpha(), # Imagem para água
            "hit": pygame.image.load("assets/images/hit.png").convert_alpha(),
            "miss": pygame.image.load("assets/images/miss.png").convert_alpha(),
            "hover": pygame.image.load("assets/images/hover.png").convert_alpha()
        }


        # Ajustando o tamanho das imagens
        for key in self.images:
            self.images[key] = pygame.transform.scale(
                self.images[key], (CELL_SIZE, CELL_SIZE)

            )
    def handle_event(self, event): # Lida com eventos do jogo
        if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
            self.handle_click(event.pos)

    def handle_click(self,mouse_pos):
        mx, my = mouse_pos

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x = BOARD_OFFSET_X + col * CELL_SIZE
                y = BOARD_OFFSET_Y + row * CELL_SIZE
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)  # Rect em pygame cria um retângulo clicável onde x e y são as coordenadas do canto superior esquerdo, e CELL_SIZE é a largura e altura do retângulo.

                if rect.collidepoint(mx, my): # Verifica se o clique do mouse colidio com a área criada pelo Rect
                     result = self.board.attack(row, col) # Ataca a célula clicada e recebe o resultado do ataque (hit, miss ou already)
                     if result is None:
                          self.message = "Célula já atacada!"
                          return
                     self.shots -= 1
                     if result == "hit":
                        self.message = "Acerto!"
                     else:
                          self.message = "Água!"

                     if self.board.all_destroyed():
                            self.message = "Você VENCEU!"
                            self.game_over = True
                     elif self.shots == 0:
                          self.message = "Fim de jogo!"
                          self.game_over = True
                        
            


def update(self):
        pass # Atualiza o estado do jogo

def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_board()
        self.draw_hud()

    def draw_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x = BOARD_OFFSET_X + col * CELL_SIZE
                y = BOARD_OFFSET_Y + row * CELL_SIZE
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

                if not self.board.attacked[row][col]:
                    color = (70, 130, 180)
                elif (row, col) in self.board.ships:
                    color = (200, 50, 50)
                else:
                    color = (220, 220, 220)

                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)

    def draw_hud(self):
        font = pygame.font.SysFont("arial", 24)

        shots_text = font.render(f"Disparos: {self.shots}", True, TEXT_COLOR)
        msg_text = font.render(self.message, True, TEXT_COLOR)

        self.screen.blit(shots_text, (20, 20))
        self.screen.blit(msg_text, (20, 60))
