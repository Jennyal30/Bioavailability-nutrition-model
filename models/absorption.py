# Absorption model for micronutrients

def absorbable_iron(food):
    iron = food["iron"]
    phytate = food["phytate"]

    # simple anti-nutrient inhibition
    absorption_factor = 1 - (0.25 * phytate)

    if absorption_factor < 0:
        absorption_factor = 0

    return iron * absorption_factor
