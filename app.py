from typing import List

from flask import Flask
from flask import jsonify
from flask import request

from utils import NoSuccessApiCode
from utils import get_pokeapi_data
from utils import serialize_pokemon_moves

app = Flask(__name__)


@app.route('/pokemon/moves/<int:pokemon_id>', methods=['GET'])
def get_pokemon_moves(pokemon_id):

    # Extract API data
    try:
        data: dict = get_pokeapi_data(pokemon_id)
    except NoSuccessApiCode as response:
        return jsonify({"error": response.msg}), response.status
    # Transform data
    pokemon_moves: List[dict] = serialize_pokemon_moves(data)

    # Pagination
    offset = request.args.get('offset', default=0, type=int)
    limit = request.args.get('limit', default=10, type=int)
    moves_count: int = len(pokemon_moves)
    page_count: int = len(pokemon_moves) // limit
    returned_batch: list = pokemon_moves[offset: offset+limit]

    return jsonify(
        {
            "moves_count": moves_count,
            "page_count": page_count,
            "offset": offset,
            "limit": limit,
        },
        {"moves": returned_batch}
    )


if __name__ == '__main__':
    app.run()
