import sqlite3

def initalize_db():
    conn = sqlite3.connect('psom.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS player_stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name TEXT NOT NULL,
        points INTEGER,
        assists INTEGER,
        blocks INTEGER,
        rebounds INTEGER,
        steals INTEGER
    )
    ''')

    conn.commit()
    return conn, cursor


def sv_2_db(conn, cursor, player_stats):
    cursor.execute('''
    'INSERT INTO player_stats (player_name, points, assists, blocks, rebounds, steals)'
    VALUES (?, ?, ?, ?, ?, ?)'
    ''', (
        player_stats['player_name'],
        player_stats['points'],
        player_stats['assists'],
        player_stats['blocks'],
        player_stats['rebounds'],
        player_stats['steals']
    ))

    conn.commit()
    print(f"PSOM stats are updated for {player_stats['player_name']}")