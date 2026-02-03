# Hardcoded values for the season and plant type
''' Adding more options for season and plant type would enhance the program. '''

'''Listing input available options for user to choose
from, assisting in valid input selection.'''
seasons = ["spring", "summer", "autumn", "winter"]
plant_types = ["flower", "vegetable", "shrub", "tree", "herb"]

# Get user input for season and plant type
'''printing the available options for seasons and plant types
to guide the user in making a selection.
Input user prompts for both season and plant type'''
print("Possible seasons:", seasons)
season = input("Enter the current season (spring, summer, autumn, winter): ").lower()
print("Possible plant types:", plant_types)
plant_type = input("Enter the type of plant (flower, vegetable, shrub, tree, herb): ").lower()

'''Creating an empty string to accumulate gardening advice
based on the user's input for season and plant type.'''
# Variable to hold gardening advice
advice = ""

'''Taking into account user input,
generating specific gardening advice
based on the selected season and plant type.'''
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


'''Printing the generated gardening advice based on user input.'''
# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
