-- Insert Teams
INSERT INTO Team (name, conference, division, city) VALUES
('Browns', 'AFC', 'North', 'Cleveland'),
('Bengals', 'AFC', 'North', 'Cincinnati'),
('Ravens', 'AFC', 'North', 'Baltimore'),
('Steelers', 'AFC', 'North', 'Pittsburgh');

-- Insert Stadiums
INSERT INTO Stadium (name, location) VALUES
('Cleveland Browns Stadium', 'Cleveland, OH'),
('Paycor Stadium', 'Cincinnati, OH'),
('M&T Bank Stadium', 'Baltimore, MD'),
('Acrisure Stadium', 'Pittsburgh, PA');

-- Insert Games
INSERT INTO Game (
    home_team_id, away_team_id, stadium_id, home_score, away_score,
    is_overtime, date_time, game_status, week_number
) VALUES
-- Week 1: Bengals @ Browns
(1, 2, 1, NULL, NULL, FALSE, '2025-09-07 13:00:00', 'Scheduled', 1),
-- Week 2: Browns @ Ravens
(3, 1, 3, NULL, NULL, FALSE, '2025-09-14 13:00:00', 'Scheduled', 2),
-- Week 3: Steelers @ Bengals
(2, 4, 2, NULL, NULL, FALSE, '2025-09-21 13:00:00', 'Scheduled', 3);

-- Insert Season entries for each team in 2025
INSERT INTO Season (team_id, year) VALUES
(1, 2025),  -- Browns
(2, 2025),  -- Bengals
(3, 2025),  -- Ravens
(4, 2025);  -- Steelers

-- Link Games to the 2025 Season (Assumes Game IDs = 1, 2, 3 and Season IDs = 1-4)
-- You might want to verify these IDs or use RETURNING in code for dynamic inserts

-- Game 1: Week 1 - Browns vs Bengals
INSERT INTO SeasonGame (season_id, game_id) VALUES
(1, 1), -- Browns
(2, 1); -- Bengals

-- Game 2: Week 2 - Ravens vs Browns
INSERT INTO SeasonGame (season_id, game_id) VALUES
(1, 2), -- Browns
(3, 2); -- Ravens

-- Game 3: Week 3 - Bengals vs Steelers
INSERT INTO SeasonGame (season_id, game_id) VALUES
(2, 3), -- Bengals
(4, 3); -- Steelers
