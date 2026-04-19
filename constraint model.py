# Constraint-Based Meal Model
# Goal: select foods maximizing absorbable iron under phytate constraint

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

# Constraint: total phytate must be below threshold
PHYTATE_LIMIT = 3.0

best_meal = []
best_value = 0

# Try simple combinations of 2 foods
food_names = list(foods.keys())

for i in range(len(food_names)):
    for j in range(i+1, len(food_names)):
        meal = [food_names[i], food_names[j]]
        
        total_phytate = sum(foods[f]["phytate"] for f in meal)
        
        if total_phytate <= PHYTATE_LIMIT:
            total_iron = sum(absorbable_iron(foods[f]) for f in meal)
            
            if total_iron > best_value:
                best_value = total_iron
                best_meal = meal

print("Best meal under phytate constraint:", best_meal)
print("Absorbable iron:", round(best_value, 2))
