import requests
from bs4 import BeautifulSoup

def psom_StatScraper(url, player_name):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        return None

    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the statistics section
    score_div = soup.find('div', class_='player-statistic-score')
    if not score_div:
        print("Could not find score div")
        return None
    
    # Extract statistics values
    stat_values = []
    for h3 in score_div.find_all('h3'):
        try:
            value = int(h3.text.strip())
            stat_values.append(value)
        except ValueError:
            print(f"Invalid number found: {h3.text.strip()}")
            return None
    
    # Ensure exactly 5 statistics are found
    if len(stat_values) != 5:
        print(f"Expected 5 statistics, but found {len(stat_values)}")
        return None

    # Return formatted statistics
    return {
        'player_name': player_name,
        'points': stat_values[0],
        'assists': stat_values[1],
        'blocks': stat_values[2],
        'rebounds': stat_values[3],
        'steals': stat_values[4]
    }
