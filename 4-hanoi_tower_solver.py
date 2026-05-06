
def hanoi_solver(n):

    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    def record_state():
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")

    record_state()

    def move_disks(disks, source, target, auxiliary):
        if disks > 0:
            move_disks(disks - 1, source, auxiliary, target)
            disk = rods[source].pop()
            rods[target].append(disk)
            record_state()
            move_disks(disks - 1, auxiliary, target, source)

    move_disks(n, 0, 2, 1)
    
    return "\n".join(moves)

def hanoi_simulator():
    print("--- TOWER OF HANOI SOLVER ---")
    
    try:
        n = int(input("How many disks do you want to play with? (Recommended 3 or 4): "))
        
        if n <= 0:
            print("Please enter a number greater than 0.")
            return

        print(f"\nGenerating steps for {n} disks...")
        print("Rods state: [Rod 0] [Rod 1] [Rod 2]")
        print("-" * 40)
        
        steps = hanoi_solver(n)
        
        print(steps)
        
        total_moves = 2**n - 1
        print("-" * 40)
        print(f"Completed in {total_moves} moves.")

    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    hanoi_simulator()