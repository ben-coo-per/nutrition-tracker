_NUTRITION_IDENTIFIERS = [
    {"identifier": "EnergyConsumed", "description": "A quantity sample type that measures the amount of energy consumed.", "unit": "kcal"},
    {"identifier": "FatTotal", "description": "A quantity sample type that measures the total amount of fat consumed.", "unit": "g"},
    {"identifier": "Carbohydrates", "description": "A quantity sample type that measures the amount of carbohydrates consumed.", "unit": "g"},
    {"identifier": "Protein", "description": "A quantity sample type that measures the amount of protein consumed.",  "unit": "g"},
    {"identifier": "FatSaturated", "description": "A quantity sample type that measures the amount of saturated fat consumed.", "unit": "g"},
    {"identifier": "Cholesterol", "description": "A quantity sample type that measures the amount of cholesterol consumed.", "unit": "g"},
    {"identifier": "Sodium", "description": "A quantity sample type that measures the amount of sodium consumed.", "unit": "mg"},
    {"identifier": "Fiber", "description": "A quantity sample type that measures the amount of fiber consumed."},
    {"identifier": "Sugar", "description": "A quantity sample type that measures the amount of sugar consumed."},
    {"identifier": "VitaminA", "description": "A quantity sample type that measures the amount of vitamin A consumed."},
    {"identifier": "VitaminC", "description": "A quantity sample type that measures the amount of vitamin C consumed."},
    {"identifier": "Calcium", "description": "A quantity sample type that measures the amount of calcium consumed."},
    {"identifier": "Iron", "description": "A quantity sample type that measures the amount of iron consumed."},
    {"identifier": "Folate", "description": "A quantity sample type that measures the amount of folate consumed."},
    {"identifier": "Potassium", "description": "A quantity sample type that measures the amount of potassium consumed."},
    {"identifier": "VitaminB12", "description": "A quantity sample type that measures the amount of vitamin B12 consumed."},
    {"identifier": "VitaminD", "description": "A quantity sample type that measures the amount of vitamin D consumed."},
    {"identifier": "VitaminE", "description": "A quantity sample type that measures the amount of vitamin E consumed."},
    {"identifier": "VitaminK", "description": "A quantity sample type that measures the amount of vitamin K consumed."},
    {"identifier": "Zinc", "description": "A quantity sample type that measures the amount of zinc consumed."},
    {"identifier": "Biotin", "description": "A quantity sample type that measures the amount of biotin consumed."},
    {"identifier": "Niacin", "description": "A quantity sample type that measures the amount of niacin consumed."},
    {"identifier": "PantothenicAcid", "description": "A quantity sample type that measures the amount of pantothenic acid consumed."},
    {"identifier": "Phosphorus", "description": "A quantity sample type that measures the amount of phosphorus consumed."},
    {"identifier": "Iodine", "description": "A quantity sample type that measures the amount of iodine consumed."},
    {"identifier": "Magnesium", "description": "A quantity sample type that measures the amount of magnesium consumed."},
    {"identifier": "Manganese", "description": "A quantity sample type that measures the amount of manganese consumed."},
    {"identifier": "Molybdenum", "description": "A quantity sample type that measures the amount of molybdenum consumed."},
    {"identifier": "Riboflavin", "description": "A quantity sample type that measures the amount of riboflavin consumed."},
    {"identifier": "Selenium", "description": "A quantity sample type that measures the amount of selenium consumed."},
    {"identifier": "Thiamin", "description": "A quantity sample type that measures the amount of thiamin consumed."},
    {"identifier": "VitaminB6", "description": "A quantity sample type that measures the amount of vitamin B6 consumed."},
    {"identifier": "Choline", "description": "A quantity sample type that measures the amount of choline consumed."},
    {"identifier": "Copper", "description": "A quantity sample type that measures the amount of copper consumed."}
]

# Macros that you want returned from the nutrition estimation machine every time
IMPORTANT_MACROS = ["EnergyConsumed", "FatTotal", "Carbohydrates", "Protein"]

# The nutrition identifiers that are currently supported by the logging shortcut
SUPPORTED_IDENTIFIERS = IMPORTANT_MACROS + ["FatSaturated", "Cholesterol", "Sodium"]
NUTRITION_IDENTIFIERS = filter(lambda x: x["identifier"] in SUPPORTED_IDENTIFIERS, _NUTRITION_IDENTIFIERS)