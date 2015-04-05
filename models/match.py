import math

class Match():
    """docstring for Match"""
    def __init__(self, teams):
        self.id = int(math.floor(random.random() * 10000000))
        self.teams = teams
        self.winner = None

    def get_winner(self):
        pass

    def get_score(self):
        pass

    def team_draw(self):
        pass
