import os
import psycopg2

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
        print("1. Query Data")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Placeholder for querying data
            print("Querying data...")
        elif choice == "2":
            print("Exiting console...")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    connection = connect_to_database()
    if connection:
        console_loop(connection)
        connection.close()

if __name__ == "__main__":
    main()
