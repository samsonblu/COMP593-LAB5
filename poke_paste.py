from pastebin_api import post_new_paste
from poke_api import search_for_pokemon
import sys

def main():
    pokemon = get_search_term()
    ability_list = search_for_pokemon(pokemon)
    if ability_list:
        title, body_text = get_paste_data(ability_list, pokemon)
        paste_url = post_new_paste(title, body_text, '1D')
        print(f'URL of new paste: {paste_url}')
    

def get_search_term():
    num_params = len(sys.argv)
    if num_params > 0:
        return sys.argv[1]
    else:
        print('Error: Missing Pokemon.')

def get_paste_data(ability_list, pokemon):

    title = f"{pokemon}'s Abilities"

    divider = '\n' 
    body_text = divider.join(ability_list)

    return title, body_text

if __name__ == '__main__':
    main()