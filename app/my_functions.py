import string
import random 
import json
import datetime
import requests


def get_random_string(length):
    letters = string.printable
    result_str = ''.join(random.choice(letters) for i in range(length))
    return(result_str)


def populate_pokemon(database, model, model_2, json_file):
    with open(json_file) as file:
        file = json.loads(file.read())

    for line in file:
        line['owner_id'] = None
        line['moves'] = []
        moves = list(model_2.query.filter_by(type=line['type']))
        for move in moves:
            if len(line['moves']) < 4 and move not in line['moves']:
                line['moves'].append(random.choice(moves))
        new_poke = model(line)
        database.session.add(new_poke)
    database.session.commit()


def populate_moves(database, model, json_file):
    with open(json_file) as file:
        file = json.loads(file.read())
    for line in file:
        new_poke = {
            'id': line['id'],
            'acc': line['Acc.'],
            'power': line['Power'],
            'name' : line['Name'],
            'effect_type':line['Effect_type'],
            'effect_power': line['Effect_power'],
            'type': line['Type']
        }
        database.session.add(model(new_poke))
    database.session.commit()


def get_pokemon_from_row(pokemon):
    pokemon_dict = {
        'name': pokemon.name,
        'health': pokemon.health,
        'attack': pokemon.attack,
        'type': pokemon.type,
        'image_front': pokemon.image_front,
        'image_back': pokemon.image_back,
        'moves': pokemon.moves
    }
    return pokemon_dict
    # moves = db.relationship('Move', secondary=move_pokemon_table, backref='pokemon')

def get_moves_dict(pokemon):
    moves_dict = {}
    i=1
    for move in pokemon['moves']:
        move = {
            'acc': move.acc,
            'power': move.power,
            'name': move.name,
            'effect_type': move.effect_type,
            'effect_power': move.effect_power,
        }
        moves_dict[i] = move
        i+=1
    pokemon['moves'] = moves_dict
    return pokemon
