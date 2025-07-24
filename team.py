class Team:
    def __init__(self, team_id, name, conference, division, city):
        self.team_id = team_id
        self.name = name
        self.conference = conference
        self.division = division
        self.city = city

    def __repr__(self):
        return f"Team({self.team_id}, {self.name}, {self.conference}, {self.division}, {self.city})"
