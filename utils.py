from typing import List

import requests

from requests import Response


BASE_URL = f"https://pokeapi.co/api/v2/pokemon/"


class NoSuccessApiCode(Exception):
    def __init__(self, status_code, text):
        self.status = status_code
        self.text = text
        self.msg = f'Something went wrong... Response code: {self.status} - {self.text}'

    def __str__(self):
        return self.msg


def get_pokeapi_data(pokemon_id: int) -> dict:
    url = BASE_URL + f'{pokemon_id}'
    response = requests.get(url)
    status = response.status_code
    if status != 200:
        raise NoSuccessApiCode(response.status_code, response.text)
    return response.json()


def extract_pokemon_moves(data: dict) -> list:
    moves = data["moves"]
    moves_names = [move["move"]["name"] for move in moves]
    return sorted(moves_names)


def display_pokemon_moves(pokemon_id: int, moves_names: list):
    print(f'Sorted moves for pokemon with ID {pokemon_id}:' + '\n')
    for i, name in enumerate(moves_names, 1):
        print(f'{i}. {name}')


def serialize_pokemon_moves(data: dict) -> List[dict]:
    moves = data["moves"]
    moves_names: List[dict] = [
        {"move_name": move["move"]["name"]} for move in moves
    ]
    return sorted(moves_names, key=lambda x: x["move_name"])