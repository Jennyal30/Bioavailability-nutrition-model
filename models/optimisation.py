from models.absorption import absorbable_nutrients

def evaluate_meal(meal, foods):
    total = {"iron": 0, "zinc": 0, "calcium": 0}

    for item in meal:
        nutrients = absorbable_nutrients(foods[item])

        total["iron"] += nutrients["iron"]
        total["zinc"] += nutrients["zinc"]
        total["calcium"] += nutrients["calcium"]

    return total


def best_meal(foods):
    food_names = list(foods.keys())

    best_meal = None
    best_score = 0

    PHYTATE_LIMIT = 4.0

    for i in range(len(food_names)):
        for j in range(i + 1, len(food_names)):

            meal = [food_names[i], food_names[j]]

            # phytate constraint
            total_phytate = sum(foods[f]["phytate"] for f in meal)

            if total_phytate <= PHYTATE_LIMIT:

                nutrients = evaluate_meal(meal, foods)

                # simple scoring function (multi-nutrient)
                score = nutrients["iron"] + nutrients["zinc"] + nutrients["calcium"] / 100

                if score > best_score:
                    best_score = score
                    best_meal = meal

    return best_meal, best_score
