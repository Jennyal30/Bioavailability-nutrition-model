# Multi-nutrient absorption model

def absorbable_nutrients(food):
    phytate = food["phytate"]

    # absorption penalty
    factor = 1 - (0.25 * phytate)
    if factor < 0:
        factor = 0

    return {
        "iron": food["iron"] * factor,
        "zinc": food["zinc"] * factor,
        "calcium": food["calcium"] * factor
    }
