class Joltage_Calculator():
    def __init__(self):
        self.data = [line for line in open("input.txt").read().splitlines()]
        print("Joltage Calculator initialized with data:", self.data)

    def calculate_voltages(self):
        calculated_banks = []
        total_sum = 0

        for line in self.data:
            print("Processing line:", line)
            first_battery, second_battery = self.process_line(line)
            
            calculated_banks.append((first_battery, second_battery))
            total_sum += int(str(first_battery) + str(second_battery))
        print("Calculated banks:", calculated_banks)
        print("Calculated total bank voltages sum:", total_sum)
    
    def process_line(self, line):
        first_battery = 0
        second_battery = 0
        for index, character in enumerate(line):
            number = int(character)
            if number > second_battery:
                second_battery = number
            
            if second_battery > first_battery and index + 1 < len(line):
                first_battery = second_battery
                second_battery = 0

        return first_battery, second_battery