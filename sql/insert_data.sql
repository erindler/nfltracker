-- Insert Teams with explicit IDs
INSERT INTO Team (team_id, name, conference, division, city) VALUES
(1, 'Browns', 'AFC', 'North', 'Cleveland'),
(2, 'Bengals', 'AFC', 'North', 'Cincinnati'),
(3, 'Ravens', 'AFC', 'North', 'Baltimore'),
(4, 'Steelers', 'AFC', 'North', 'Pittsburgh');

-- Insert Stadiums with explicit IDs
INSERT INTO Stadium (stadium_id, name, location) VALUES
(1, 'Cleveland Browns Stadium', 'Cleveland, OH'),
(2, 'Paycor Stadium', 'Cincinnati, OH'),
(3, 'M&T Bank Stadium', 'Baltimore, MD'),
(4, 'Acrisure Stadium', 'Pittsburgh, PA');

-- Insert Season entries for each team in 2025 with explicit IDs
INSERT INTO Season (season_id, team_id, year) VALUES
(1, 1, 2025),  -- Browns
(2, 2, 2025),  -- Bengals
(3, 3, 2025),  -- Ravens
(4, 4, 2025);  -- Steelers

-- Insert Games with explicit IDs
INSERT INTO Game (
    game_id, home_team_id, away_team_id, stadium_id, home_score, away_score,
    is_overtime, date_time, game_status, week_number, season_id
) VALUES
-- Week 1: Bengals @ Browns
(1, 1, 2, 1, NULL, NULL, FALSE, '2025-09-07 13:00:00', 'Scheduled', 1, 1),
-- Week 2: Browns @ Ravens
(2, 3, 1, 3, NULL, NULL, FALSE, '2025-09-14 13:00:00', 'Scheduled', 2, 1),
-- Week 3: Steelers @ Bengals
(3, 2, 4, 2, NULL, NULL, FALSE, '2025-09-21 13:00:00', 'Scheduled', 3, 2);

-- Insert Season entries for each team in 2024 with explicit IDs
INSERT INTO Season (season_id, team_id, year) VALUES
(5, 1, 2024),  -- Browns
(6, 2, 2024),  -- Bengals
(7, 3, 2024),  -- Ravens
(8, 4, 2024);  -- Steelers

-- Insert Games for the 2024 Season with explicit IDs, scores, and corrected week numbers
INSERT INTO Game (
    game_id, home_team_id, away_team_id, stadium_id, home_score, away_score,
    is_overtime, date_time, game_status, week_number, season_id
) VALUES
-- Week 1
(4, 1, 2, 1, 21, 17, FALSE, '2024-09-08 13:00:00', 'Completed', 1, 5),
(5, 3, 4, 3, 24, 20, FALSE, '2024-09-08 16:25:00', 'Completed', 1, 7),
-- Week 2
(6, 4, 1, 4, 14, 28, FALSE, '2024-09-15 13:00:00', 'Completed', 2, 8),
(7, 2, 3, 2, 17, 14, FALSE, '2024-09-15 16:25:00', 'Completed', 2, 6),
-- Week 3
(8, 1, 3, 1, 31, 27, FALSE, '2024-09-22 13:00:00', 'Completed', 3, 5),
(9, 4, 2, 4, 10, 13, FALSE, '2024-09-22 16:25:00', 'Completed', 3, 8),
-- Week 4
(10, 2, 1, 2, 20, 24, FALSE, '2024-09-29 13:00:00', 'Completed', 4, 6),
(11, 3, 4, 3, 17, 21, FALSE, '2024-09-29 16:25:00', 'Completed', 4, 7),
-- Week 5
(12, 1, 4, 1, 28, 14, FALSE, '2024-10-06 13:00:00', 'Completed', 5, 5),
(13, 2, 3, 2, 21, 24, FALSE, '2024-10-06 16:25:00', 'Completed', 5, 6);