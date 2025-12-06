from Solver import Solver

def main():
    with open("input.txt", "r") as file:
        instructions = file.readlines()
        solver = Solver()
        solver.process_instructions(instructions)
        solver.print_results()

if __name__ == "__main__":
    main()
