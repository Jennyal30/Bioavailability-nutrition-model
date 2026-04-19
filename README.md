# developed as a prototype for bioavailability-aware dietary modelling in plant-based systems.

This project demonstrates a simple model for estimating absorbable iron in plant-based foods.

It accounts for anti-nutrient effects (phytate), showing how nutrient intake differs from actual absorption.

This aligns with research in:
- micronutrient bioavailability
- food systems modelling
- plant-based diet optimisation
## Additional Model: Optimisation

A second script (`optimisation_model.py`) demonstrates simple optimisation logic by selecting foods that maximise absorbable iron under anti-nutrient constraints.

This reflects early-stage decision modelling used in dietary optimisation frameworks.
## Diet and Constraint Models

Additional scripts extend the model to meal-level analysis:

- `diet_model.py`: calculates absorbable iron from combined foods  
- `constraint_model.py`: selects optimal food combinations under anti-nutrient constraints  

These demonstrate simplified dietary optimisation logic relevant to plant-based diet modelling.
