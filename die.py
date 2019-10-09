from dist_transformer import DiscreteDist

class Die(object):

    def __init__(self, sides):
        self.dist = DiscreteDist([1/sides]*sides)
        self.n = sides
    
    def __str__(self):
        return str(self.dist)

    # returns the probability distribution for the greatest of 2 trials of the distribution
    def advantage(self):
        out = DiscreteDist([0.0]*len(self))
        l = len(self.dist)
        for i in range(l):
            for j in range(l):
                if i >= j:
                    out[i] += self.dist[i]*self.dist[j]
                elif j > i:
                    out[j] += self.dist[i]*self.dist[j]
        return out

    # returns the probability distribution for the lowest of 2 trials of the distribution
    def disadvantage(self):
        out = DiscreteDist([0.0]*len(self.dist))
        l = len(self.dist)
        for i in range(l):
            for j in range(l):
                if i >= j:
                    out[i] += self.dist[i]*self.dist[j]
                elif j > i:
                    out[j] += self.dist[i]*self.dist[j]
        return out
    
