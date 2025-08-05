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
        print("2. Exit")
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
            print("Exiting console...")
            break
        else:
            print("Invalid choice. Please try again.")

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
                g.away_score, g.home_score, g.week_number
            FROM game AS g
            JOIN team AS home_team ON g.home_team_id = home_team.team_id
            JOIN team AS away_team ON g.away_team_id = away_team.team_id
            JOIN season AS s ON s.season_id = g.season_id
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
        return f"{weekNumber}: {awayTeam} {game[4]} vs {game[5]} {homeTeam}"
    else:
        return f"{weekNumber}: {awayTeam} vs {homeTeam}"

def main():
    connection = connect_to_database()
    if connection:
        console_loop(connection)
        connection.close()

if __name__ == "__main__":
    main()
