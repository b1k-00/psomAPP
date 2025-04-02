import requests
from bs4 import BeautifulSoup

def psom_StatScraper(url, player_name):

    response = requests.get(url)
    if response.status_code == 200:
        print(f"Failed to retireve page: {response.status_code}")
        return None
    
    #Parsing MYIBL HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    #Find stats div element
    stats_div = soup.find('div', class_='player_stats')
    if not stats_div:
        print("Failed to find stats")
        return None
    
    # Find the score elements
    score_div = stats_div.find('div', class_='player-statistic-score')
    if not score_div:
        print("Could not find score div")
        return None
    
    # Extract the statistics values
    stat_values = []
    for h3 in score_div.find_all('h3'):
        # Extract the number from the text
        value = int(h3.text.strip())
        stat_values.append(value)
    
    # Ensure we found all 5 statistics
    if len(stat_values) != 5:
        print(f"Expected 5 statistics, but found {len(stat_values)}")
        return None
    
    # Return a dictionary with the player's statistics
    return {
        'player_name': player_name,
        'points': stat_values[0],
        'assists': stat_values[1],
        'blocks': stat_values[2],
        'rebounds': stat_values[3],
        'steals': stat_values[4]
    }