from data.foods import foods
from models.optimisation import best_meal
from models.absorption import absorbable_nutrients

def run_with_phytate_factor(factor):
    def modified_absorption(food):
        phytate = food["phytate"]
        adjusted_factor = 1 - (factor * phytate)
        if adjusted_factor < 0:
            adjusted_factor = 0
        return {
            "iron": food["iron"] * adjusted_factor,
            "zinc": food["zinc"] * adjusted_factor,
            "calcium": food["calcium"] * adjusted_factor
        }

    # simple override test
    return factor

factors = [0.15, 0.25, 0.35, 0.45]

for f in factors:
    print("Phytate factor:", f)
