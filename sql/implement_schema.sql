-- Team table
CREATE TABLE Team (
    team_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    conference VARCHAR(10),
    division VARCHAR(20),
    city VARCHAR(50)
);

-- Stadium table
CREATE TABLE Stadium (
    stadium_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
);

-- Season table: one row per season year
CREATE TABLE Season (
    season_id SERIAL PRIMARY KEY,
    year INTEGER NOT NULL UNIQUE
);

-- Game table
CREATE TABLE Game (
    game_id SERIAL PRIMARY KEY,
    home_team_id INTEGER NOT NULL REFERENCES Team(team_id) ON DELETE CASCADE,
    away_team_id INTEGER NOT NULL REFERENCES Team(team_id) ON DELETE CASCADE,
    stadium_id INTEGER REFERENCES Stadium(stadium_id) ON DELETE SET NULL,
    home_score INTEGER,
    away_score INTEGER,
    is_overtime BOOLEAN DEFAULT FALSE,
    date_time TIMESTAMP NOT NULL,
    game_status VARCHAR(20),
    week_number INTEGER,
    season_id INTEGER REFERENCES Season(season_id) ON DELETE SET NULL
);
