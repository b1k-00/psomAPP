# Import functions from other modules
from psom_db import initalize_db, sv_2_db
from scraper import psom_StatScraper

def main():
    # URL of the page to scrape
    url = "https://iblindonesia.com/profile/player/2270153?season=40351"  # Replace with actual URL
    player_name = "Travin Thibodeaux"  # Replace with actual player name
    
    # Set up the database
    conn, cursor = initalize_db()
    
    # Scrape the player statistics
    player_stats = psom_StatScraper(url, player_name)
    
    # Save to database if scraping was successful
    if player_stats:
        sv_2_db(conn, cursor, player_stats)
    
    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()