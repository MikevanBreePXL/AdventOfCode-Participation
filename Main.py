from Ingredient_watcher import Ingredient_Watcher

def main():
    ingredient_watcher = Ingredient_Watcher()
    ingredient_watcher.process_input()
    print("Fresh Ingredients Found:", ingredient_watcher.get_fresh_ingredients())
    print("Available Ingredients Found:", ingredient_watcher.get_available_ingredients())
    fresh_and_available = ingredient_watcher.find_available_fresh_ingredients()
    print("Fresh and Available Ingredients:", fresh_and_available)
    print("Total Fresh and Available Ingredients:", len(fresh_and_available))

if __name__ == "__main__":
    main()