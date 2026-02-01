# Prompt for season and plant type
season = input("Enter the season (summer, winter, other): ").strip().lower()
plant_type = input("Enter the plant type (flower, vegetable, other): ").strip().lower()

# Validate allowed values
valid_seasons = {"summer", "winter", "other"}
valid_plant_types = {"flower", "vegetable", "other"}

if season not in valid_seasons:
    season = "other"

if plant_type not in valid_plant_types:
    plant_type = "other"

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
