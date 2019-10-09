# DiscreteDist is a class that extends list with changes to magic methods such that mathematical operations behave like they do on discrete probability distributions.
# I wrote this to work on dice, so it only supports ptobability distributions with a sample space in the set of natural numbers
class DiscreteDist(list):

    def __add__(self, other):
        total_size = len(self) + len(other)
        out = [0.0] * total_size
        for j in range(total_size):
            for k in range(total_size):
                try:
                    other_index = j-k-1
                    if other_index < 0:
                        continue
                    out[j] += self[k]*other[other_index]
                except:
                    pass
        return DiscreteDist(out)
    
    def __iadd__(self, other):
        return self + other
    
    def __mul__(self, other):
        out = DiscreteDist(self)
        if other > 1:
            for i in range(1,other):
                out += self
        return DiscreteDist(out)
    
    def __imul__(self, other):
        return self * other

    # returns the probability distribution for the greatest of 2 trials of the distribution
    def best_of_2(self):
        out = DiscreteDist([0.0]*len(self))
        l = len(self)
        for i in range(l):
            for j in range(l):
                if i >= j:
                    out[i] += self[i]*self[j]
                elif j > i:
                    out[j] += self[i]*self[j]
        return out

    # returns the probability distribution for the lowest of 2 trials of the distribution
    def worst_of_2(self):
        out = DiscreteDist([0.0]*len(self))
        l = len(self)
        for i in range(l):
            for j in range(l):
                if i >= j:
                    out[i] += self[i]*self[j]
                elif j > i:
                    out[j] += self[i]*self[j]
        return out