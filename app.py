import os
import psycopg2
from team import Team

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

def main():
    connection = connect_to_database()
    if connection:
        console_loop(connection)
        connection.close()

if __name__ == "__main__":
    main()
