import pytest

from unittest.mock import patch

from utils import get_pokeapi_data, serialize_pokemon_moves
from utils import extract_pokemon_moves
from utils import NoSuccessApiCode


@pytest.mark.parametrize(
    "data, expected_result",
    [
        ("payload_with_moves", ["blaze", "pound", "smash"]),
        ("payload_with_no_moves", [])
    ],
    ids={
        "returns_list_in_alphabetical_order",
        "returns_empty_list_if_no_moves"
    }
)
def test_get_sorted_pokemon_moves(data, expected_result, request):
    data = request.getfixturevalue(data)
    moves = extract_pokemon_moves(data)
    assert moves == expected_result


@patch("utils.requests.get")
def test_api_return_data_if_success_code(mock_get, payload_with_moves):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = payload_with_moves

    pokemon_data = get_pokeapi_data(1)
    assert pokemon_data == payload_with_moves


@patch("utils.requests.get")
def test_api_throw_exception_if_no_success_code(mock_get):
    mock_get.return_value.status_code = 404

    with pytest.raises(NoSuccessApiCode):
        pokemon_data = get_pokeapi_data(1)
        assert not pokemon_data


@pytest.mark.parametrize(
    "data, expected_result",
    [
        ("payload_with_moves", [
            {'move_name': 'blaze'},
            {'move_name': 'pound'},
            {'move_name': 'smash'}
        ]),
        ("payload_with_no_moves", [])
    ],
    ids={
        "returns_move_objects_in_alphabetical_order",
        "returns_empty_move_obj_list_when_no_data"
    }
)
def test_serialize_moves(data, expected_result, request):
    data = request.getfixturevalue(data)
    serialized_moves = serialize_pokemon_moves(data)
    assert serialized_moves == expected_result



