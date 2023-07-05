import json

def read_map():
    # Replace with the correct path to your JSON file
    with open('map.json', 'r') as f:
        game_map = json.load(f)
    return game_map

def generate_message(game_map):
    message = "Here's your game map:\n"
    for tile in game_map["map"]:
        message += f"Tile {tile['tile']} is a {tile['terrain']} terrain. It has {tile['north']} to the North, {tile['west']} to the West, {tile['south']} to the South, and {tile['east']} to the East.\n"
    return message

game_map = read_map()
message = generate_message(game_map)
print(message)

