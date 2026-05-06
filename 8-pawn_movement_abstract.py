
import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)
        new_x = self.position[0] + move[0]
        new_y = self.position[1] + move[1]
        self.position = (new_x, new_y)
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self):
        diagonals = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.moves.extend(diagonals)

def game_simulator():
    print("--- MOVEMENT SIMULATOR (OOP) ---")
    pawn = Pawn()
    
    while True:
        print(f"\nCurrent position: {pawn.position}")
        print(f"Possible moves: {len(pawn.moves)}")
        print("1. Make a random move")
        print("2. Level up (Enable diagonals)")
        print("3. View path history")
        print("4. Exit")
        
        option = input("What do you want to do?: ")

        if option == "1":
            new_pos = pawn.make_move()
            print(f"The pawn moved to: {new_pos}")

        elif option == "2":
            pawn.level_up()
            print("LEVEL UP! The pawn can now move diagonally.")

        elif option == "3":
            print("Path traveled so far:")
            visual_path = " -> ".join(str(p) for p in pawn.path)
            print(visual_path)

        elif option == "4":
            print("Game over!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    game_simulator()