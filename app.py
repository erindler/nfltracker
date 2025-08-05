import os
import psycopg2
from entities.team import Team

def connect_to_database():
    try:
        # Connect to the database
        connection = psycopg2.connect(
            host="localhost",
            port=5432,
            database="mynfltracker",
            user="postgres",
            password=os.getenv("POSTGRES_PASSWORD")
        )
        print("Connection to the database was successful!")
        return connection
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None

def console_loop(connection):
    while True:
        print("\nNFL Tracker Console")
        print("1. View a team's season schedule")
        print("2. View the league structure")
        print("3. Add a new game")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            teams = get_all_teams(connection)
            print("Select a team to view its season schedule:")
            for i, team in enumerate(teams):
                print(f"{i + 1}. {team.name}")
            team_input = input("Enter the number of the team: ")
            selected_team = teams[int(team_input) - 1]
            print(f"Selected Team: {selected_team.name} ({selected_team.city})")
            year = input("Enter the year for the schedule (e.g., 2023): ")
            for game in get_team_schedule_by_year(connection, selected_team.team_id, year):
                print(game)
        elif choice == "2":
            print("League Structure:")
            for team in get_all_teams(connection):
                print(f"{team.name} ({team.city}) - {team.conference} {team.division}")
        elif choice == "3":
            print("Add a new game:")
            teams = get_all_teams(connection)
            for i, team in enumerate(teams):
                print(f"{i + 1}. {team.name} ({team.city})")
            home_idx = int(input("Enter the number for the home team: ")) - 1
            away_idx = int(input("Enter the number for the away team: ")) - 1
            home_team = teams[home_idx]
            away_team = teams[away_idx]
            # List stadiums for selection
            stadiums = get_all_stadiums(connection)
            print("Select a stadium:")
            for i, stadium in enumerate(stadiums):
                print(f"{i + 1}. {stadium['name']} ({stadium['location']})")
            stadium_idx = int(input("Enter the number for the stadium: ")) - 1
            stadium_id = stadiums[stadium_idx]['stadium_id']
            home_score = input("Enter the home team score (or leave blank if not played): ")
            away_score = input("Enter the away team score (or leave blank if not played): ")
            is_overtime = input("Was the game overtime? (y/n): ").strip().lower() == 'y'
            date_time = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
            game_status = input("Enter the game status (Scheduled/Final): ")
            week_number = int(input("Enter the week number: "))
            # List seasons for selection
            seasons = get_all_seasons(connection)
            print("Select a season:")
            for i, season in enumerate(seasons):
                print(f"{i + 1}. {season['year']}")
            season_idx = int(input("Enter the number for the season: ")) - 1
            season_id = seasons[season_idx]['season_id']
            add_game(connection, home_team.team_id, away_team.team_id, stadium_id, home_score, away_score, is_overtime, date_time, game_status, week_number, season_id)
            print("Game added!")
        elif choice == "4":
            print("Exiting console...")
            break
        else:
            print("Invalid choice. Please try again.")
def get_all_stadiums(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT stadium_id, name, location FROM stadium;")
        stadiums = [
            {'stadium_id': row[0], 'name': row[1], 'location': row[2]}
            for row in cursor.fetchall()
        ]
        cursor.close()
        return stadiums
    except Exception as e:
        print(f"An error occurred while fetching stadiums: {e}")
        return []

def get_all_seasons(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT s.season_id, s.year
            FROM season s
            ORDER BY s.year DESC
        """)
        seasons = [
            {'season_id': row[0], 'year': row[1]}
            for row in cursor.fetchall()
        ]
        cursor.close()
        return seasons
    except Exception as e:
        print(f"An error occurred while fetching seasons: {e}")
        return []

def get_all_teams(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM team;")
        teams = [Team(*team) for team in cursor.fetchall()]
        cursor.close()
        return teams
    except Exception as e:
        print(f"An error occurred while fetching teams: {e}")
        return []
    
def get_team_schedule_by_year(connection, team_id, year):
    try:
        cursor = connection.cursor()
        query = """
            SELECT 
                away_team.city, away_team.name, home_team.city, home_team.name,
                g.away_score, g.home_score, g.week_number, st.name, st.location
            FROM game AS g
            JOIN team AS home_team ON g.home_team_id = home_team.team_id
            JOIN team AS away_team ON g.away_team_id = away_team.team_id
            JOIN season AS s ON s.season_id = g.season_id
            JOIN stadium AS st ON st.stadium_id = g.stadium_id
            WHERE (g.home_team_id = %s OR g.away_team_id = %s) AND s.year = %s;
        """
        cursor.execute(query, (team_id, team_id, year))
        games = cursor.fetchall()
        cursor.close()
        return [clean_score(game) for game in games]
    except Exception as e:
        print(f"An error occurred while fetching the schedule: {e}")
        return []

def clean_score(game):
    awayTeam = f"{game[0]} {game[1]}"
    homeTeam = f"{game[2]} {game[3]}"
    weekNumber = game[6] if game[6] is not None else "N/A"
    if game[4] is not None and game[5] is not None:
        return f"{weekNumber}: {awayTeam} {game[4]} vs {game[5]} {homeTeam} at {game[7]}, {game[8]}"
    else:
        return f"{weekNumber}: {awayTeam} vs {homeTeam} at {game[7]}, {game[8]}"

def add_game(connection, home_team_id, away_team_id, stadium_id, home_score, away_score, is_overtime, date_time, game_status, week_number, season_id):
    try:
        cursor = connection.cursor()
        # Get the next game_id
        cursor.execute("SELECT COALESCE(MAX(game_id), 0) + 1 FROM game;")
        next_game_id = cursor.fetchone()[0]
        query = """
            INSERT INTO game (game_id, home_team_id, away_team_id, stadium_id, home_score, away_score, is_overtime, date_time, game_status, week_number, season_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query, (
            next_game_id,
            home_team_id,
            away_team_id,
            stadium_id,
            int(home_score) if home_score else None,
            int(away_score) if away_score else None,
            is_overtime,
            date_time,
            game_status,
            week_number,
            season_id
        ))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"An error occurred while adding the game: {e}")

def main():
    connection = connect_to_database()
    if connection:
        console_loop(connection)
        connection.close()

if __name__ == "__main__":
    main()
