from Solver import Solver

def main():
    solver = Solver()
    solver.load_instructions_from_file('input.txt')
    solver.execute_instructions()
    print(f"Number of times pointer_safe reached zero: {solver.counter_solution}")

if __name__ == "__main__":
    main()
