from data.foods import foods
from models.optimisation import best_food

# Run optimisation
best, value = best_food(foods)

print("Best food based on absorbable iron:", best)
print("Absorbable iron value:", round(value, 2))
