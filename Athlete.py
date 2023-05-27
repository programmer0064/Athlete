class Athlete:

    def __init__(self, name, sport, age, team):
        self.name = name
        self.sport = sport
        self.age = age
        self.team = team

    def can_play_in_premier_league(self):
        if self.team == "Paris Saint Germain":
            return True
        else:
            return False
