from models.team import Team

class Tournament:
    """docstring for Tournament"""
    def __init__(self, name):
        self.name = name
        self.matches = []
        self.current_match = None
        self.teams = []
        self.MAX_NUM_TEAMS = 5

    def start(self):
        pass

    def get_next_match(self):
        pass

    def enter_teams(self):
        # TODO: this is a sample; we'll get names from input
        for i in range(self.MAX_NUM_TEAMS):
            team = Team(str(i))
