import requests

DAD_JOKES_API_URL = 'https://icanhazdadjoke.com/'
DAD_JOKES_SEARCH = f'{DAD_JOKES_API_URL}search'

def main():
    jokes_list = search_for_dad_jokes('cow')
    print(jokes_list)
    return

def search_for_dad_jokes(search_term):
    """Gets a list of dad jokes that contain a search term

    Args:
        search_term (str): Search query for Dad Joke type. 

    Returns:
        str: List of Dad jokes, if successful. None if unsuccessful 
    """
    
    # Setup the header parameters
    header_params = {
        'Accept' : 'application/json',
    }

    # Setup the query string parameters
    query_str_params = {
        'term' : search_term
    }

    # Send the GET request to the Dad jokes API
    print(f'Searching Dad Jokes API for "{search_term}" jokes...', end='')
    resp_msg = requests.get(DAD_JOKES_API_URL, headers=header_params, params=query_str_params)
    if resp_msg.ok:
        print(' Success!')
        body_dict = resp_msg.json()
        jokes_list = [j['joke'] for j in body_dict['results']]
        return jokes_list
    else:
        print(' Fail.')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason: {resp_msg.text}')



def get_random_dad_joke():

    # Setup the header parameters
    header_params = {
        'Accept' : 'application/json',
    }

    # Send the GET request to the Dad jokes API
    print('Sending GET request to Dad Jokes API...', end='')
    resp_msg = requests.get(DAD_JOKES_API_URL, headers=header_params)
    
    # Check whether the GET request was succeful
    if resp_msg.ok:
        print(' Success!')
        joke_dict = resp_msg.json()
        return joke_dict['joke']
    else:
        print(' Fail.')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason: {resp_msg.text}')

if __name__ == '__main__':
    main()