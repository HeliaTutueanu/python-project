class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = int(0)
        self.difficulty = ""

    all_ingredients = []

    def calculate_difficulty(self):
        ingredients_len = len(self.ingredients)

        if self.cooking_time < 10 and ingredients_len < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and ingredients_len >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and ingredients_len < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and ingredients_len >= 4:
            self.difficulty = "Hard"
        else:
            print("Not able to calculate difficulty")
        
    def get_name(self):
        return self.name

    def get_cooking_time(self):
        return self.cooking_time
    
    def get_ingredients(self):
        return self.ingredients
    
    def get_difficulty(self):
        if not self.difficulty:
            self.calculate_difficulty()
        return self.difficulty
    
    def set_name(self, name):
        self.name = name 
    
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def add_ingredients(self, items):
        items = list(items)
        self.ingredients.extend(items)
        self.update_all_ingredients()

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.all_ingredients:
                self.all_ingredients.append(ingredient)

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients
        
    def __str__(self):
        return f"Recipe: {self.name}\nCooking time (min): {self.cooking_time}\nDifficulty: {self.get_difficulty()}\nIngredients: {', '.join(self.ingredients)}"

def recipe_search(data, search_term):
    found = False
    print("\n\nRecipes found with the ingredient:", search_term)
    print("---------------------------------------------")
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(str(recipe))
            found = True
    if not found:
        print("Couldn't find", search_term)
       
# Tea Recipe
tea = Recipe("Tea")
tea.add_ingredients(["Tea Leaves", "Sugar", "Water"])
tea.set_cooking_time(5)

# Coffee Recipe
coffee = Recipe("Coffee")
coffee.add_ingredients(["Coffee Powder", "Sugar", "Water"])
coffee.set_cooking_time(5)

# Cake Recipe
cake = Recipe("Cake")
cake.add_ingredients(["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"])
cake.set_cooking_time(50)

# Banana Smoothie
banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients(["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"])
banana_smoothie.set_cooking_time(5)

recipes_list = [tea, coffee, cake, banana_smoothie]

for recipe in recipes_list:
    print(str(recipe))

recipe_search(recipes_list, "Water")
recipe_search(recipes_list, "Sugar")
recipe_search(recipes_list, "Bananas")