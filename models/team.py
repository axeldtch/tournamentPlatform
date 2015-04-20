class Team():
    """docstring for Team"""
    def __init__(self, name):
        self.id = int(math.floor(random.random() * 10000000))
        self.name = name
        self.num_losses = 0
        self.points = 0
        self.points_hist = []
        self.WINNER_POINTS = 3
        self.LOSER_POINTS = 2

    def add_winner_points(self):
        self.last_point_amt = self.WINNER_POINTS
        self.points += self.WINNER_POINTS
        self.points_hist.append(self.WINNER_POINTS)

    def add_loser_points(self):
        self.last_point_amt = self.LOSER_POINTS
        self.points += self.LOSER_POINTS
        self.points_hist.append(self.LOSER_POINTS)

    def undo_points(self):
        last_points_added = self.points_hist[-1]
        self.points -= last_points_added
        del self.points_hist[-1]

    def reset(self):
        self.points = 0
        self.points_hist = []
