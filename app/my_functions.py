import string
import random 
import json
import datetime
import requests

def get_random_string(length):
    letters = string.printable
    result_str = ''.join(random.choice(letters) for i in range(length))
    return(result_str)


def get_move(move_id_or_name):
    r = requests.get(f'https://pokeapi.co/api/v2/move/{move_id_or_name}')
    return r.json()

def getpoke(move_id_or_name):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{move_id_or_name}/')
    return r.json()