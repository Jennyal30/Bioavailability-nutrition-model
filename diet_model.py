# Mini Diet Model
# Combine foods and calculate total absorbable iron

foods = {
    "beans": {"iron": 5.0, "phytate": 2.0},
    "lentils": {"iron": 6.5, "phytate": 1.5},
    "spinach": {"iron": 2.5, "phytate": 1.0}
}

def absorbable_iron(food):
    iron = food["iron"]
    phytate = food["phytate"]
    
    absorption_factor = 1 - (0.25 * phytate)
    
    if absorption_factor < 0:
        absorption_factor = 0
        
    return iron * absorption_factor

# Define a simple meal (2–3 foods)
meal = ["beans", "spinach"]

total_absorbable_iron = 0

for item in meal:
    total_absorbable_iron += absorbable_iron(foods[item])

print("Meal:", meal)
print("Total absorbable iron:", round(total_absorbable_iron, 2))
