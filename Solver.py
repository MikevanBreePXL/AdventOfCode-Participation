class Solver:
    rotation_point = 50
    passed_zero_counter = 0
    times_turned_onto_zero = 0

    def rotate_right(self, amount):
        # Rotate right has a limit of 99, rolls back to 0
            for i in range(amount):
                self.rotation_point += 1
                if self.rotation_point > 99:
                    self.rotation_point = 0
                    self.passed_zero_counter += 1
                if self.rotation_point == 0:
                    self.times_turned_onto_zero += 1
                    self.passed_zero_counter -= 1
        
    def rotate_left(self, amount):
        # Rotate left has a limit of 0, rolls back to 99
            for i in range(amount):
                self.rotation_point -= 1
                if self.rotation_point < 0:
                    self.rotation_point = 99
                    self.passed_zero_counter += 1
                if self.rotation_point == 0:
                    self.times_turned_onto_zero += 1

    def execute_rotation(self, instruction):
        if instruction[0] == "L":
            self.rotate_left(int(instruction[1:]))
        elif instruction[0] == "R":
            self.rotate_right(int(instruction[1:]))

    def print_results(self):
        print(f"Final rotation point: {self.rotation_point}")
        print(f"Passed zero counter: {self.passed_zero_counter}")
        print(f"Times turned onto zero: {self.times_turned_onto_zero}")
        print(f"End zero result: {self.passed_zero_counter + self.times_turned_onto_zero}")

    def process_instructions(self, instructions):
        for line in instructions:
            line = line.strip()
            self.execute_rotation(line)
