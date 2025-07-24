class Game:
    def __init__(self, game_id, home_team, away_team, stadium, home_score, away_score, is_overtime, date_time, game_status, week_number):
        self.game_id = game_id
        self.home_team = home_team
        self.away_team = away_team
        self.stadium = stadium
        self.home_score = home_score
        self.away_score = away_score
        self.is_overtime = is_overtime
        self.date_time = date_time
        self.game_status = game_status
        self.week_number = week_number

    def __repr__(self):
        return (f"Game({self.game_id}, Home: Team({self.home_team.team_id}, {self.home_team.name}), "
                f"Away: Team({self.away_team.team_id}, {self.away_team.name}), Stadium: {self.stadium}, "
                f"Scores: {self.home_score}-{self.away_score}, Overtime: {self.is_overtime}, "
                f"Date: {self.date_time}, Status: {self.game_status}, Week: {self.week_number})")
