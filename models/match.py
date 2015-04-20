import math
import random

class Match():
    """docstring for Match"""
    def __init__(self):
        self.id = int(math.floor(random.random() * 10000000))
        self.teams = []
        self.winner = None
        self.score = {}
        self.turns = {}
        self.MAX_TURNS_PER_TEAM = 9
        self.current_turn = None

    def add_team(self, team):
        if len(teams) < 2:
            self.teams.append(team)

    def start(self):
        ids_list = []
        teams_dict = {}

        for team in teams:
            ids_list.append(team.id)
            teams_dict[team.id] = team

        self.current_turn = teams_dict[random.choice(ids_list)]

    def get_score(self):
        for team in teams:
            self.score[team.name] = team.points

        return self.score

    def team_draw(self):
        pass
