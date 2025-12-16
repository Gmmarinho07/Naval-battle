import random
from settings import BOARD_SIZE, NUM_SHIPS

class Board: # Classe criada para o tabuleiro do jogo
    def __init__(self):
        self.attacked = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.ships = set()

        while len(self.ships) < NUM_SHIPS: # Adiciona navios aleatoriamente no tabuleiro
            row = random.randint(0, BOARD_SIZE -1)
            col = random.randint(0, BOARD_SIZE - 1)
            self.ships.add((row, col))

    def attack(self, row, col):
        if self.attacked[row][col]:
            return "Já atacado" # if para evitar ataques no mesmo lugar
        
        self.attacked[row][col] = True
        return (row, col) in self.ships # Retorna se houve acerto ou não
    
    def all_destroyed(self): # Verifica se todos os navios foram destruídos
        return all(self.attacked[r][c] for r, c in self.ship)
