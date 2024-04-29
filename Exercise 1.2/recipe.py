recipe_1 = {
    "name": "Tea",
    "cooking_time": 5,
    "ingredients": ["tea leaves", "sugar", "water"]
}

recipe_2 = {
    "name": "Chicken Alfredo",
    "cooking_time": 30,
    "ingredients": ["fettuccine", "chicken breast", "heavy cream", "Parmesan cheese", "garlic"]
}

recipe_3 = {
    "name": "Vegetable Stir-Fry",
    "cooking_time": 15,
    "ingredients": ["broccoli", "carrots", "bell peppers", "onion", "soy sauce"]
}

recipe_4 = {
    "name": "Caprese Salad",
    "cooking_time": 10,
    "ingredients": ["tomatoes", "fresh mozzarella", "basil leaves", "balsamic glaze", "olive oil"]
}

recipe_5 = {
    "name": "Chocolate Chip Cookies",
    "cooking_time": 25,
    "ingredients": ["flour", "butter", "sugar", "chocolate chips", "vanilla extract"]
}

all_recipes = [recipe_1]

all_recipes.extend([recipe_2, recipe_3, recipe_4, recipe_5])

for recipe in all_recipes:
 print(recipe['ingredients'])