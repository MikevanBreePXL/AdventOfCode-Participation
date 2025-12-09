class Solver:
    def __init__(self):
        self.pointer_safe = 50
        self.counter_solution = 0
        self.instructions = []

    def load_instructions_from_file(self, path):
        with open(path, 'r') as file:
            self.instructions = [line.strip() for line in file.readlines()]

    def execute_instructions(self):
        amount = 0
        for instruction in self.instructions:
            amount = int(instruction[1:])
            if instruction.startswith("L"):
                self.rotate_left(amount)
            elif instruction.startswith("R"):
                self.rotate_right(amount)

            if self.pointer_safe == 0:
                self.counter_solution += 1
    
    def rotate_left(self, amount):
        self.pointer_safe -= amount
        while self.pointer_safe < 0:
            self.pointer_safe += 100  # Assuming a circular buffer of size 100
    
    def rotate_right(self, amount):
        self.pointer_safe += amount
        while self.pointer_safe >= 100:
            self.pointer_safe -= 100  # Assuming a circular buffer of size 100