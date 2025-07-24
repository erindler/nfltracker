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
    week_number INTEGER
);

-- Season table: tracks which teams participate in a given season
CREATE TABLE Season (
    season_id SERIAL PRIMARY KEY,
    team_id INTEGER NOT NULL REFERENCES Team(team_id) ON DELETE CASCADE,
    year INTEGER NOT NULL,
    UNIQUE(team_id, year) -- A team can only appear once per season year
);

-- SeasonGame table: links games to a season
CREATE TABLE SeasonGame (
    season_game_id SERIAL PRIMARY KEY,
    season_id INTEGER NOT NULL REFERENCES Season(season_id) ON DELETE CASCADE,
    game_id INTEGER NOT NULL REFERENCES Game(game_id) ON DELETE CASCADE,
    UNIQUE(season_id, game_id) -- Prevent duplicate links
);
