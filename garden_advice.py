# Hardcoded values for the season and plant type
''' Adding more options for season and plant type would enhance the program. '''
seasons = ["spring", "summer", "autumn", "winter"]
plant_types = ["flower", "vegetable", "shrub", "tree", "herb"]
# Get user input for season and plant type
# List of possible seasons and plant types
print("Possible seasons:", seasons)
season = input("Enter the current season (spring, summer, autumn, winter): ").lower()
print("Possible plant types:", plant_types)
plant_type = input("Enter the type of plant (flower, vegetable, shrub, tree, herb): ").lower()

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
