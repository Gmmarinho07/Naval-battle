import pygame
from settings import *
from game import Game

def main():
    pygame.init() # Inicializa todos os módulos do Pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Batalh Naval")

    clock = pygame.time.CLock() # Controla a taxa de quadros por segundo
    game = Game(screen)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)

        game.update()
        game.draw()
        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main() # Executa a função principal se o script for executado diretamente