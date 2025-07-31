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

-- Insert Season entries for each team in 2025
INSERT INTO Season (team_id, year) VALUES
(1, 2025),  -- Browns
(2, 2025),  -- Bengals
(3, 2025),  -- Ravens
(4, 2025);  -- Steelers

-- Insert Games
INSERT INTO Game (
    home_team_id, away_team_id, stadium_id, home_score, away_score,
    is_overtime, date_time, game_status, week_number, season_id
) VALUES
-- Week 1: Bengals @ Browns
(1, 2, 1, NULL, NULL, FALSE, '2025-09-07 13:00:00', 'Scheduled', 1, 1),
-- Week 2: Browns @ Ravens
(3, 1, 3, NULL, NULL, FALSE, '2025-09-14 13:00:00', 'Scheduled', 2, 1),
-- Week 3: Steelers @ Bengals
(2, 4, 2, NULL, NULL, FALSE, '2025-09-21 13:00:00', 'Scheduled', 3, 2);