class Team():
    """docstring for Team"""
    def __init__(self, name):
        self.id = int(math.floor(random.random() * 10000000))
        self.name = name
        self.num_losses = 0
        self.points = 0
        self.last_point_amt = 0

    def add_winner_points(self):
        pass

    def add_loser_points(self):
        pass

    def undo_points(self):
        pass
