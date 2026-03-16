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
        self.title_font = pygame.font.SysFont ("arial", 48, bold = True)
        self.text_font = pygame.font.SysFont ("arial", 28)




#----------------
#-----EVENTOS----
#----------------


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.state == STATE_MENU:
                self.start_game()
            elif self.state == STATE_PLAYING:
                self.handle_click(event.pos)
            elif self.state == STATE_GAME_OVER:
                self.state = STATE_MENU






#-------------------
#----INICIAR JOGO---
#-------------------
    def start_game(self):
        self.board = Board()
        self.shots = 10
        self.message = "Clique em uma célula"
        self.state = STATE_PLAYING

    #-------------------
    #----TRATAR CLIQUE--
    #-------------------
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
                        self.message = "Celula ja atacada"
                        return
                    
                    self.shots -= 1

                    if result: 
                        self.message = "Acertou !"
                    else:
                        self.message = "Água!"

                    if self.board.all_destroyed():
                        self.message = "Você venceu!"
                        self.state = STATE_GAME_OVER
                    elif self.shots == 0:
                        self.message = "Fim de jogo!"
                        self.state = STATE_GAME_OVER


    #-------------------
    #---UPDATE----------
    #-------------------
    def update(self):
        pass


    #-------------------
    #----DESENHAR-------
    #-------------------

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)

        if self.state == STATE_MENU:
            self.draw_menu()
        elif self.state == STATE_PLAYING:
            self.draw_board()
            self.draw_hud()
        elif self.state == STATE_GAME_OVER:
            self.draw_game_over()



    #------------------
    #-----TELAS--------

    def draw_menu(self):
        title = self.title_font.render ("Batalha Naval", True, TEXT_COLOR)
        text = self.text_font.render ("Clique para começar", True, TEXT_COLOR)

        self.screen.blit(title, (WIDTH// 2 - title.get_width() // 2, 200)) # Centralizando o título
        self.screen.blit(text, (WIDTH//2 - text.get_width() // 2, 300)) # Centralizando o texto

    def draw_game_over(self):
        over = self.title_font.render(self.message, True, TEXT_COLOR)
        restart = self.text_font.render("Clique para voltar ao menu", True, TEXT_COLOR)
        self.screen.blit(over, (WIDTH//2 - over.get_width() // 2, 250)) # Centralizando a mensagem de fim de jogo
        self.screen.blit(restart, (WIDTH//2 - restart.get_width() // 2, 330))

    def draw_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x = BOARD_OFFSET_X + col * CELL_SIZE
                y = BOARD_OFFSET_Y + row * CELL_SIZE
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                

                if not self.board.attacked[row][col]:
                    color = (70, 130, 180) # Azul para células não atacadas
                elif(row, col) in self.board.ships:
                    color = (200, 50, 50)
                else:
                    color = (220, 220, 220) # Ciano para água

                    pygame.draw.rect(self.screen, color, rect)
                    pygame.draw.rect(self.screen, (0,0,0), rect, 2)

    def draw_hud(self):
        shots_text = self.text_font.render(f"Disparos restantes: {self.shots}", True, TEXT_COLOR)
        msg_text = self.text_font.render(self.message, True, TEXT_COLOR)

        self.screen.blit(shots_text, (20, 20))
        self.screen.blit(msg_text, (20, 60))
