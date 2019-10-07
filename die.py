class Die(object):

    def __init__(self, n_sides):
        self.p = [1/n_sides]*n_sides
        self.n = n_sides

    #outputs a deque of floats where p_n(n)[i+1] is the probability that the total of n dice is i.
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
    