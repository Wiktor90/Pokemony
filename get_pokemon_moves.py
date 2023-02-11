from argparse import ArgumentParser
from utils import NoSuccessApiCode
from utils import get_pokeapi_data
from utils import extract_pokemon_moves
from utils import display_pokemon_moves


def main():
    # CLI args handling
    parser = ArgumentParser(
        description="Extract pokemon moves by pokemon ID from PokeApi.co service"
    )
    parser.add_argument(
        "-id", dest="pokemon_id", type=int, required=True, help="Pokemon ID",
    )
    args = parser.parse_args()
    pokemon_id: int = args.pokemon_id

    # Extract
    try:
        data = get_pokeapi_data(pokemon_id)
    except NoSuccessApiCode as e:
        print(e)
        return

    # Transform
    pokemon_moves = extract_pokemon_moves(data)

    # Display
    display_pokemon_moves(pokemon_id, pokemon_moves)


if __name__ == "__main__":
    main()
