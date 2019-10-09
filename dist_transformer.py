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