class HanoiGame:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        # Towers
        self.A = list(range(num_disks, 0, -1))  # Start tower
        self.B =[]
        self.C =[]

    def show_towers(self):
        print(f"A: {self.A}")
        print(f"B: {self.B}")
        print(f"C: {self.C}")
        print("-"*20)

    def move_disk( self, from_tower, to_tower):
        # Get source and destination towers
        source = getattr(self, from_tower)
        dest = getattr(self, to_tower)
        disk = source[-1]          # Take top disk
        dest.append(disk)          # Place on destination
        source[:] = source[:-1]    # Remove top disk without pop()
        print(f"Move disk {disk} from {from_tower} to {to_tower}")
        self.show_towers()

    def solve(self, n, from_tower, to_tower, aux_tower):
        if n == 0:
            return
        # Move n-1 disks to auxiliary tower
        self.solve(n-1, from_tower, aux_tower, to_tower)
        # Move the remaining disk to destination
        self.move_disk(from_tower, to_tower)
        # Move n-1 disks from auxiliary to destination
        self.solve(n-1, aux_tower, to_tower, from_tower)

# ===============================
# Play the game
num_disks = 3
game = HanoiGame(num_disks)

print("Initial Towers:")
game.show_towers()

print("Solving Tower of Hanoi...\n")
game.solve(num_disks, "A", "C", "B")

print("Completed! 🎉")



