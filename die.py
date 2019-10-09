from dist_transformer import DiscreteDist

class Die(object):

    def __init__(self, sides):
        self.basic_dist = DiscreteDist([1/sides]*sides)
        self.n = sides