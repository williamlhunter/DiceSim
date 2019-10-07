class Die(object):

    def __init__(self, n_sides):
        self.p = [1/n_sides]*n_sides
        self.n = n_sides

    #returns a list of floats where the value at each index is the probability of the sum at that index + 1 being rolled.
    def prob_n_dice_dist(self, rolls):
        if rolls == 1:
            return self.p
        else:
            prob_n_minus_1 = self.prob_n_dice_dist(rolls - 1)
            for i in range(self.n):
                prob_n_minus_1.append(0)
            l = len(prob_n_minus_1)
            for j in reversed(range(l)):
                if prob_n_minus_1[j] != 0:
                    for i in range(1,self.n+1):
                        prob_n_minus_1[i+j] += prob_n_minus_1[j] / self.n
                    prob_n_minus_1[j] = 0
            return prob_n_minus_1
    
    #returns a list of floats where the value at each index is the probability of rolling the index + 1 after rolling 2 dice and discarding the lowest.
    def advantage_dist(self):
        dist = [0]*self.n
        d_p = 1 / (self.n**2)
        for i in range(self.n):
            for j in range(self.n):
                if i > j:
                    dist[i] += d_p
                if j >= i:
                    dist[j] += d_p
        return dist

    #returns a list of floats where the value at each index is the probability of rolling the index + 1 after rolling 2 dice and discarding the highest.
    def disadvantage_dist(self):
        dist = [0]*self.n
        d_p = 1 / (self.n**2)
        for i in range(self.n):
            for j in range(self.n):
                if i > j:
                    dist[j] += d_p
                if j >= i:
                    dist[i] += d_p
        return dist