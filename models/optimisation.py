# Simple optimisation model for selecting best food

from models.absorption import absorbable_iron

def best_food(foods):
    best_name = None
    best_value = 0

    for name, food in foods.items():
        value = absorbable_iron(food)

        if value > best_value:
            best_value = value
            best_name = name

    return best_name, best_value
