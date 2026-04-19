# Simple Optimisation Model
# Goal: Select food with highest absorbable iron

foods = {
    "beans": {"iron": 5.0, "phytate": 2.0},
    "lentils": {"iron": 6.5, "phytate": 1.5},
    "spinach": {"iron": 2.5, "phytate": 1.0},
    "chickpeas": {"iron": 4.0, "phytate": 1.8}
}

def absorbable_iron(food):
    iron = food["iron"]
    phytate = food["phytate"]

    absorption_factor = 1 - (0.25 * phytate)

    if absorption_factor < 0:
        absorption_factor = 0

    return iron * absorption_factor

# Find best food (simple optimisation)
best_food = None
best_value = 0

for name, data in foods.items():
    value = absorbable_iron(data)

    if value > best_value:
        best_value = value
        best_food = name

print("Best food based on absorbable iron:", best_food)
print("Absorbable iron value:", round(best_value, 2))
