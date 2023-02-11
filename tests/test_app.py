from unittest.mock import patch

from flask import request


def test_api_return_404_if_pokemon_id_not_int(app_client):
    with app_client as client:
        pokemon_id = "invalid"
        response = client.get(f"/pokemon/moves/{pokemon_id}")
        assert response.status_code == 404


@patch("utils.requests.get")
def test_api_return_404_when_pokemon_id_not_found(mock_get, app_client):
    mock_get.return_value.status_code = 404
    mock_get.return_value.text = "Record Not Found"

    with app_client as client:
        too_big_id = 44444
        response = client.get(f"/pokemon/moves/{too_big_id}")
        assert response.status_code == 404
        assert "Record Not Found" in response.json["error"]


@patch("app.serialize_pokemon_moves")
@patch("app.get_pokeapi_data")
def test_api_return_200_with_proper_data(
        mock_data, mock_moves, app_client, serialized_moves,
):
    mock_data.return_value = {}
    mock_moves.return_value = serialized_moves

    with app_client as client:
        response = client.get(f"/pokemon/moves/1")
        assert response.status_code == 200

        response_moves: dict = response.json[1]
        assert response_moves["moves"] == serialized_moves
