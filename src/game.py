import pygame
from settings import *
from board import Board

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.board = Board()

        self.message = "Clique em uma célula"
        self.shots = 10
        self.game_over = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
            self.handle_click(event.pos)

    def handle_click(self, mouse_pos):
        mx, my = mouse_pos

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x = BOARD_OFFSET_X + col * CELL_SIZE
                y = BOARD_OFFSET_Y + row * CELL_SIZE
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

                if rect.collidepoint(mx, my):
                    result = self.board.attack(row, col)

                    if result is None:
                        self.message = "Célula já atacada"
                        return

                    self.shots -= 1

                    if result:
                        self.message = "Acertou!"
                    else:
                        self.message = "Água!"

                    if self.board.all_destroyed():
                        self.message = "Você venceu!"
                        self.game_over = True
                    elif self.shots == 0:
                        self.message = "Fim de jogo!"
                        self.game_over = True

    def update(self):
        pass   # ← ESSE MÉTODO PRECISA EXISTIR

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