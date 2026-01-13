import random
from settings import BOARD_SIZE, NUM_SHIPS

class Board:
    def __init__(self):
        self.attacked = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.ships = set()

        while len(self.ships) < NUM_SHIPS:
            row = random.randint( 0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - 1)
            self.ships.add((row, col))
    def attack(self, row, col):
        if self.attacked[row][col]:
            return None  # lugar ja atacado
        
        self.attacked[row][col] = True
        return (row, col) in self.ships # Retorna True se acertou um navio, False caso contrario
    
    def all_destroyed(self):
        return all(self.attacked[r][c] for r, c in self.ships)
    
