## This repository contains two tasks:
1. CLI python script to extract pokemon moves by ID from _PokeApi.co_ 
2. API with HTTP endpoint to extract pokemon moves by ID from _PokeApi.co_

## To clone project type in your terminal:
`git-clone https://github.com/Wiktor90/Pokemony.git`

## Set up your local env:
1. Go to repo directory `cd Pokemony` and create virtual environment for example like below:

    `python -m venv venv`


2. Next activate your `venv` (command depends on your OS) and install dependencies:

   `pip install -r requirements.txt`
---------------------------------------------

## Script Usage:
1. Script is in the file `get_pokemon_moves.py`
2. Script takes one integer as require argument: _pokemon ID_
3. To call script you need to type `-id` flag as example below
### Run:
* python: `python get_pokemon_moves.py -id 1`
* bash: `.\get_pokemon_moves.py -id 3`

### Example Output in the terminal:
```
Sorted moves for pokemon with ID 22:

1. aerial-ace
2. agility
3. air-cutter
...
68. work-up
```
------------------------------------
## API Usage:
It is Flask app with one HTTP endpoint.
### Run:
`flask run`

Flask app is running on `http://127.0.0.1:5000` by default.

If for some reasons your **port 5000** is occupied you can run:

`flask run --port 5001` -> then app is running on `http://127.0.0.1:5001`

### Endpoint:
registered: `@app.route('/pokemon/moves/<int:pokemon_id>', methods=['GET'])`


example curl:
```
curl --location --request GET 'http://127.0.0.1:5000/pokemon/moves/1'
```
### Pagination:
* `limit` - default value: 10
* `offset` - default value: 0
* `moves_count` - total objects amount in a response
* `page_count` - available pages per current limit
```
    {
        "limit": 10,
        "moves_count": 77,
        "offset": 0,
        "page_count": 7
    },
```
You can change `limit` value or navigate from page to page using `offset` in classical `query_param` way:
`http://127.0.0.1:5000/pokemon/moves/2?limit=20&offset=10`

### Example Response:
```
[
    {
        "limit": 10,
        "moves_count": 133,
        "offset": 0,
        "page_count": 13
    },
    {
        "moves": [
            {
                "move_name": "aerial-ace"
            },
            {
                "move_name": "aqua-tail"
            },
            {
                "move_name": "attract"
            },
            {
                "move_name": "avalanche"
            },
            {
                "move_name": "beat-up"
            },
            ... 
    }
]
```
--------------------------------------
### Run Tests:
Running all tests: `pytest tests`