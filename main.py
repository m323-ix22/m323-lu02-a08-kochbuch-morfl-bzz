"""A08"""
import json


def load_recipe(json_string):
    return json.loads(json_string)


def adjust_recipe(recipe, num_people):
    factor = num_people / recipe['servings']
    adjusted_ingredients = {ingredient: int(amount * factor) for ingredient, amount in recipe['ingredients'].items()}
    return {
        'title': recipe['title'],
        'ingredients': adjusted_ingredients,
        'servings': num_people
    }


if __name__ == '__main__':
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'

    recipe = load_recipe(recipe_json)
    print('Originales Rezept:', recipe)

    adjusted_recipe = adjust_recipe(recipe, 2)
    print('Angepasstes Rezept für 2 Personen:', adjusted_recipe)
