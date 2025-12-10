class Ingredient_Watcher:
    available_ingredients = []
    fresh_ingredients = []

    class fresh_input:
        def __init__(self, start, end):
            self.start = start
            self.end = end
        
    def process_input(self):
        with open('input.txt', 'r') as file:
            found_empty_line = False
            for line in file.readlines():
                line = line.strip()
                print(f"Processing line: '{line}'")
                if line == "":
                    found_empty_line = True
                    continue

                if not found_empty_line:
                    print(f"Adding to fresh ingredients: {line}")
                    input_data = self.fresh_input(*map(int, line.split('-')))
                    self.fresh_ingredients.append(input_data)
                else:
                    print(f"Adding to available ingredients: {line}")
                    self.available_ingredients.append(int(line))
    
    def get_available_ingredients(self):
        return self.available_ingredients
    
    def get_fresh_ingredients(self):
        return self.fresh_ingredients
    
    def sort_fresh_ranges(self):
        self.fresh_ingredients.sort(key=lambda x: x.start)

    def count_fresh(self):
        # account for overlapping and non-touching ranges
        self.sort_fresh_ranges()
        total_count = 0
        current_start = None
        current_end = None
        for fresh_range in self.fresh_ingredients:
            if current_start is None:
                current_start = fresh_range.start
                current_end = fresh_range.end
            elif fresh_range.start > current_end + 1:
                total_count += (current_end - current_start + 1)
                current_start = fresh_range.start
                current_end = fresh_range.end
            else:
                current_end = max(current_end, fresh_range.end)
        if current_start is not None:
            total_count += (current_end - current_start + 1)
        return total_count
