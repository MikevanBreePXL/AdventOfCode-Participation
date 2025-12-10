from Ingredient_watcher import Ingredient_Watcher

def main():
    ingredient_watcher = Ingredient_Watcher()
    ingredient_watcher.process_input()
    
    print("Fresh Ingredients Ranges:", [(fi.start, fi.end) for fi in ingredient_watcher.get_fresh_ingredients()])
    print("Available Ingredients:", ingredient_watcher.get_available_ingredients())
    # ingredient_watcher.save_amount_fresh()
    # print("Total valid IDs for Fresh Ingredients:", "See fresh.txt file")
    total_fresh_count = ingredient_watcher.count_fresh()
    print("Total valid IDs for Fresh Ingredients:", total_fresh_count)

if __name__ == "__main__":
    main()