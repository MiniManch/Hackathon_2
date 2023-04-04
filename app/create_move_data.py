import json
import random as rand
import requests

# First I downloaded all the moves from Pokemon Website Bulbapedia,
# using Chrome extension I downloaded the table, converted it to json,
# then I loop through the file to create some logic for my game move database!

moves_dict = {
	'Electric': [],
	'Grass': [],
	'Rock': [],
	'Flying': [],
	'Normal': [],
	'Psychic': [],
	'Fighting': [],
	'Water': [],
	'Fire': [],
	'Ghost': [],
	'Ground': []
}


def create_move_json():
	with open('static/moves.json') as file:
		file = json.loads(file.read())
		for line in file:
			if line['Type'] in moves_dict.keys():
				if len(moves_dict[line['Type']]) < 20:
					moves_dict[line['Type']].append(line)
		with open('static/moves_2.json', 'w') as new_file:
			json.dump(moves_dict, new_file)

	with open('static/moves_2.json', 'r+') as file:
		id = 1
		value_list = ['Power', 'Acc.']
		to_change_list = ['Attack+', 'Attack-', 'Health+', 'Health-', 'Skip']
		file = json.loads(file.read())
		for key, value in file.items():
			for line in value:
				for key, stat in line.items():
					if key == 'Effect':
						line['Effect_type'] = line.pop('Effect')
						line['Effect_type'] = ''
						for x in range(rand.randint(0, len(to_change_list))):
							choice = rand.choice(to_change_list)
							if choice not in line['Effect_type']:
								line['Effect_type'] = line['Effect_type'] + ' ' + choice
							line['Effect_type'] = line['Effect_type'].strip(' ')
					if key == 'Prob. (%)':
						line['Effect_power'] = line.pop('Prob. (%)')
						line['Effect_power'] = rand.randint(1, 11) * 5
					if key in value_list:
						line[key] = rand.randint(1, 20) * 5
				line.pop('TM')
				line.pop('PP')
				line.pop('Cat.')
				line['id'] = id
				id += 1
		new_moves = []
		for key,value in file.items():
			for line in value:
				new_moves.append(line)
		with open('static/moves_3.json', 'w') as new_file:
			json.dump(new_moves, new_file)

create_move_json()
def get_all_pokemon():
	r = requests.get('http://pokeapi.co/api/v2/pokemon/?limit=811')
	pokemon_dict = []
	results = r.json()
	for result in results['results']:
		r = requests.get(result['url']).json()
		for stat in r['stats']:
			if stat['stat']['name'] =='attack':
				attack = stat['base_stat']
			if stat['stat']['name'] == 'hp':
				hp = stat['base_stat']
		new_pokemon = {'id': r['id'],
		               'name':r['name'],
		               'type': r['types'][0]['type']['name'],
		               'moves':None,
		               'strength':attack,
		               'health':hp,
		               'image_front':r['sprites']['front_default'],
		               'image_back':r['sprites']['back_default']
		               }
		pokemon_dict.append(new_pokemon)
		for pokemon in pokemon_dict:
			if pokemon['type'].capitalize() not in moves_dict.keys() or pokemon['id'] % 3 != 0:
				pokemon_dict.remove(pokemon)

	with open('static/pokemon.json', 'w') as new_file:
		json.dump(pokemon_dict, new_file)


