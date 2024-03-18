import json
import csv

with open('./visuals/the_gala.tmj') as f:
    map_data = json.load(f)

# print(map_data)
    
for layer in map_data['layers']:

    base_path = './matrix/maze'
    csv_file = None

    if layer['name'] == 'Collisions':
        csv_file = f'{base_path}/collision_maze.csv'    
    elif layer['name'] == 'Arena Blocks':
        csv_file = f'{base_path}/arena_maze.csv'
    elif layer['name'] == 'Sector Blocks':
        csv_file = f'{base_path}/sector_maze.csv'
    elif layer['name'] == 'Spawning Blocks':
        csv_file = f'{base_path}/spawning_location_maze.csv'
    elif layer['name'] == 'Object Interaction Blocks':
        csv_file = f'{base_path}/game_object_maze.csv'
    else:
        continue

    print(f'Writing to {csv_file}')

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(layer['data'])
