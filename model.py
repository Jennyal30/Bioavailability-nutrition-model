# Simple Bioavailability Model
# Estimate absorbable iron using phytate inhibition

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

for name, data in foods.items():
    print(name, "-> absorbable iron:", round(absorbable_iron(data), 2))
