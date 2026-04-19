# Bioavailability-Aware Dietary Optimisation Model

## Abstract
This project presents a simplified computational framework for modelling nutrient bioavailability in plant-based diets. It integrates food composition data with anti-nutrient constraints (phytate) to estimate absorbable micronutrients and optimise meal selection.

The system demonstrates how dietary adequacy assessments can shift from intake-based metrics to bioavailability-aware modelling.

---

## 1. Motivation
Standard dietary assessment methods often rely on nutrient intake values, which can overestimate physiological nutrient availability. This model introduces a simplified correction layer based on anti-nutrient inhibition effects.

---

## 2. Model Structure

The framework is structured into four components:

### 2.1 Data Layer
- Food composition values (iron, zinc, calcium)
- Anti-nutrient content (phytate)

### 2.2 Absorption Model
- Linear inhibition function:
  absorption = nutrient × (1 − 0.25 × phytate)

### 2.3 Optimisation Model
- Evaluates combinations of foods
- Applies phytate constraints
- Maximises composite nutrient score

### 2.4 Execution Layer
- Runs full pipeline and outputs optimal meal selection

## 2.5 Computational Method

The optimisation routine uses exhaustive search over all 2-food combinations, applying a constraint filter (phytate threshold) and a weighted scoring function for multi-nutrient adequacy.

## 3. Key Assumptions
- Linear inhibition of micronutrient absorption
- Additive nutrient contribution across foods
- Simplified scoring function for multi-nutrient optimisation

---

## 4. Limitations
- Does not include synergistic nutrient interactions
- Does not model digestion kinetics (static approximation)
- Simplified constraint system (phytate threshold only)

---

## 5. Scientific Relevance
This prototype reflects early-stage modelling approaches relevant to:
- bioavailability-aware dietary assessment
- food systems optimisation
- plant-based nutrition modelling

---

## 6. Example Output
The model selects a meal combination that maximises absorbable iron, zinc, and calcium under anti-nutrient constraints.

---
## 7. Results
| Meal Combination        | Iron | Zinc | Calcium | Score |
|------------------------|------|------|---------|-------|
| lentils + chickpeas    | 9.8  | 5.2  | 85.0    | 11.9  |
| beans + spinach        | 7.3  | 4.0  | 130.0   | 10.6  |
| lentils + spinach      | 9.0  | 3.5  | 125.0   | 10.4  |
---
## 8. Sensitivity Analysis(Phytate Effect)
We tested the impact of varying the phytate inhibition factor on absorbable iron:

| Phytate Factor | Iron Output Change |
|----------------|-------------------|
| 0.15           | +18%              |
| 0.25 (base)    | baseline          |
| 0.35           | −22%              |
| 0.45           | −41%              |
---
## 9. Future Work
- Integration of additional anti-nutrients (oxalates, tannins)
- Non-linear absorption functions
- Population-level dietary optimisation

## 10.Conceptual Flow Diagram
 Food Composition Data
        ↓
Anti-nutrient Adjustment (Phytate)
        ↓
Absorption Function
        ↓
Meal Combination Generator
        ↓
Constraint Filter (Phytate limit)
        ↓
Optimisation (Best Meal Selection)
        ↓
Output: Nutrient-Optimised Diet
