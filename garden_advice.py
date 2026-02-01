# Store advice in dictionaries for easy extension
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
    "other": "No advice for this season.",
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "other": "No advice for this type of plant.",
}

# Recommend plants based on the entered season
PLANT_RECOMMENDATIONS = {
    "summer": ["sunflower", "marigold", "tomato"],
    "winter": ["kale", "spinach", "pansy"],
    "other": ["herbs", "succulents"],
}


def get_normalized_input(prompt: str) -> str:
    """Prompt the user, trim whitespace, and lowercase the response."""
    return input(prompt).strip().lower()


def validate_choice(value: str, allowed: set[str]) -> str:
    """Validate a value against allowed options; return 'other' if invalid."""
    return value if value in allowed else "other"


def build_advice(season_choice: str, plant_choice: str) -> str:
    """Build combined season and plant advice text."""
    season_line = SEASON_ADVICE.get(season_choice, SEASON_ADVICE["other"])
    plant_line = PLANT_ADVICE.get(plant_choice, PLANT_ADVICE["other"])
    return f"{season_line}\n{plant_line}"


def recommend_plants(season_choice: str) -> str:
    """Return a recommendation line based on the season."""
    plants = PLANT_RECOMMENDATIONS.get(
        season_choice, PLANT_RECOMMENDATIONS["other"]
    )
    return "Recommended plants for this season: " + ", ".join(plants) + "."


# Prompt for season and plant type (normalized input)
season = get_normalized_input("Enter the season (summer, winter, other): ")
plant_type = get_normalized_input(
    "Enter the plant type (flower, vegetable, other): "
)

# Validate allowed values (fallback to 'other')
valid_seasons = set(SEASON_ADVICE.keys())
valid_plant_types = set(PLANT_ADVICE.keys())
season = validate_choice(season, valid_seasons)
plant_type = validate_choice(plant_type, valid_plant_types)

# Generate advice and recommendations
advice = build_advice(season, plant_type)
recommendations = recommend_plants(season)

# Print the generated advice and recommendations
print(advice)
print(recommendations)
