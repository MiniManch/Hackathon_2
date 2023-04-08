import random


def first_turn():
	return random.randint(0, 1)


def play(turn, player_list):
	player = player_list[turn]
	print(f'{player.name} its your turn! \n you have Attack of:{player.attack} and Health of {player.health}')
	choice = input(f"{name}\n {char.help()} \n").lower()
	while choice not in char.move_list:
		choice = input(f"{name}\n {char.help()} \n").lower()
	return choice


def check_win(player_list):
	for player in player_list:
		if player['Char'].health == 0:
			return True
	return False


def game():
	player_list = choose_char()
	turn = first_turn(player_list)
	win = check_win(player_list)
	while not win:
		if turn == 0:
			other_char = 1
		elif turn == 1:
			other_char = 0

		info = player_list[turn]['Char'].info()
		attack = info['Attack']
		health = info['Health']
		name = player_list[turn]['Name']
		char = player_list[turn]['Char']
		other_char = player_list[other_char]['Char']

		choice = play(turn, player_list, attack, health, name, char)
		if choice == 'attack':
			func = getattr(char, 'basic_attack')
			func(other_char)

		elif choice in type(char).move_on_enm:
			func = getattr(char, f'{choice}')
			func(other_char)
		else:
			func = getattr(char, f'{choice}')
			func()

		if turn == 0:
			turn = 1
		elif turn == 1:
			turn = 0
		win = check_win(player_list)
	for player in player_list:
		if player['Char'].health > 0:
			winner = player['Name']
	return f'Winner is: {winner}'


print(game())

