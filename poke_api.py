import requests
import sys

pokemon = sys.argv[1]
POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'
POKE_API_URL_search = f'{POKE_API_URL}{pokemon.lower()}'

def main():
    ability_list = search_for_pokemon(pokemon)
    ability_names = ', '.join(ability_list[:-1]).title() + ' and ' + ability_list[-1].title()
    num_abilities = len(ability_list)
    
    if pokemon.isnumeric:
        if num_abilities > 1:
           print(f'Pokedex #{pokemon.title()} has the abilities {ability_names}!')
        else: print(f'Pokedex #{pokemon.title()} has the ability {ability_names}!')
    else: 
        if num_abilities > 1:
           print(f'{pokemon.title()} has the abilities {ability_names}!')
        else: print(f'{pokemon.title()} has the ability {ability_names}!') 

def get_search_term():
    num_params = len(sys.argv)
    if num_params > 0:
        return sys.argv[1]
    else:
        print('Error: Missing Pokemon name or Pokedex ID')

def search_for_pokemon(pokemon):
    """Get a pokemon and it's abilities

    Args:
        pokemon (str): Search query for pokemon, as it's name or Pokedex ID

    Returns:
        str: Returns Pokemon name, and lists its abilities.
    """

    # Send the GET request to the Poke API
    resp_msg = requests.get(POKE_API_URL_search)
    if pokemon.isnumeric():
        print(f'Searching the Poke API for pokemon with pokedex #{pokemon}...', end='')
    else:
        print(f'Searching the Poke API for {pokemon.title()}...', end='')
    if resp_msg.ok:
        print(' Success!')
        poke_dict = resp_msg.json()
        abilities_dict = [a['ability']['name'] for a in poke_dict['abilities']]
        return abilities_dict
    else:
        print(' Fail.')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason: {resp_msg.text}')

if __name__ == '__main__':
    main()