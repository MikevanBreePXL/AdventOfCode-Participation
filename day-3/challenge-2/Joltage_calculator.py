class Joltage_Calculator():
    def __init__(self):
        self.data = [line for line in open("input.txt").read().splitlines()]
        print("Joltage Calculator initialized with data:", self.data)

    def calculate_voltages(self):
        calculated_banks = []
        total_sum = 0

        for line in self.data:
            print("Processing line:", line)
            calculated_banks.append(int(self.find_largest_12_digits(line)))
            total_sum += calculated_banks[-1]
        
        print("Calculated Banks:", calculated_banks)
        print("Total Sum of Calculated Banks:", total_sum)
    
    def find_largest_12_digits(self, line):
        """
        Find 12 digits from the input string that form the largest possible number.
        
        Args:
            line: A string of digits
            
        Returns:
            A string of 12 digits forming the largest possible number
        """
        if len(line) < 12:
            return line  # Return as is if less than 12 digits
        
        if len(line) == 12:
            return line  # Return as is if exactly 12 digits
        
        # We need to select 12 digits from len(line) digits
        # Use a greedy approach: at each position, choose the largest digit
        # that still leaves enough digits to complete the selection
        
        result = []
        remaining_to_select = 12
        start_index = 0
        
        while remaining_to_select > 0:
            # Calculate how many digits we can look ahead
            # We need to leave at least (remaining_to_select - 1) digits after our choice
            end_index = len(line) - remaining_to_select + 1
            
            # Find the maximum digit in the valid range
            max_digit = max(line[start_index:end_index])
            
            # Find the first occurrence of this max digit in the range
            max_index = line.index(max_digit, start_index, end_index)
            
            # Add this digit to result
            result.append(max_digit)
            
            # Move start_index past this chosen digit
            start_index = max_index + 1
            remaining_to_select -= 1
        
        return ''.join(result)