import json
import random as rand


# First I downloaded all the moves from Pokemon Website Bulbapedia,
# using Chrome extension I downloaded the table, converted it to json,
# then I loop through the file to create some logic for my game move database!

moves_dict = moves_dict = {
		'Electric': [],
		'Grass'   : [],
		'Rock'    : [],
		'Flying'  : [],
		'Normal'  : [],
		'Psychic' : [],
		'Fighting': [],
		'Water'   : [],
		'Fire'    : [],
		'Ghost'   : [],
		'Ground'  : []
	}

with open('static/moves.json') as file:
	file = json.loads(file.read())
	for line in file:
		if line['Type'] in moves_dict.keys():
			if len(moves_dict[line['Type']]) < 20 :
				moves_dict[line['Type']].append(line)
	with open('static/moves_2.json','w') as new_file:
		json.dump(moves_dict,new_file)
	for key in moves_dict.values():
		print(len(key))


with open('static/moves_2.json','r+') as file:
	value_list = ['Power','Acc.']
	to_change_list = ['Attack+','Attack-','Health+','Health-','Skip']
	file = json.loads(file.read())
	for key, value in file.items():
		for line in value:
			for key, stat in line.items():
				if key == 'Effect':
					line['Effect_type'] = line.pop('Effect')
					line['Effect_type'] = ''
					for x in range(rand.randint(0,len(to_change_list))):
						choice = rand.choice(to_change_list)
						if choice not in line['Effect_type']:
							line['Effect_type'] = line['Effect_type'] + ' ' + choice
						line['Effect_type'] = line['Effect_type'].strip(' ')
				if key == 'Prob. (%)':
					line['Effect_power'] = line.pop('Prob. (%)')
					line['Effect_power'] = rand.randint(1,11)*5
					print('hey')
				print(line)
				if key in value_list:
					line[key] = rand.randint(1,20)*5

	with open('static/moves_3.json', 'w') as new_file:
		json.dump(file,new_file)

