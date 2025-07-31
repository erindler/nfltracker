class Season:
    def __init__(self, season_id, team_id, year):
        self.season_id = season_id
        self.team_id = team_id
        self.year = year

    def __repr__(self):
        return f"Season({self.season_id}, Team({self.team_id}), Year: {self.year})"
