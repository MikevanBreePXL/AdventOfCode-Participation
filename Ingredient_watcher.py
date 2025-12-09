class Ingredient_Watcher:
    available_ingredients = []
    fresh_ingredients = []
        
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
                    self.fresh_ingredients.append(line.strip())
                else:
                    print(f"Adding to available ingredients: {line}")
                    self.available_ingredients.append(int(line))
    
    def get_available_ingredients(self):
        return self.available_ingredients
    
    def get_fresh_ingredients(self):
        return self.fresh_ingredients
    
    def find_available_fresh_ingredients(self):
        fresh_and_available = []
        for ingredient in self.available_ingredients:
            for fresh_range in self.fresh_ingredients:
                start, end = map(int, fresh_range.split('-'))
                if start <= ingredient <= end:
                    fresh_and_available.append(ingredient)
                    break
        return fresh_and_available