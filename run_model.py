from data.foods import foods
from models.optimisation import best_meal

meal, score = best_meal(foods)

print("Best meal combination:", meal)
print("Composite nutrition score:", round(score, 2))
