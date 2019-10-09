class DiscreteDist(object):

    def __init__(self, dist):
        self.dist = dist
    
    def __len__(self):
        return len(self.dist)
    
    def __add__(self, other):
        total_size = len(self) + len(other)
        out = [0] * total_size
        for j in range(total_size):
            for k in range(total_size):
                try:
                    other_index = j-k-1
                    if other_index < 0:
                        continue
                    out[j] += self.dist[k]*other.dist[other_index]
                except:
                    pass
        return DiscreteDist(out)

    def __mul__(self, other):
        out = self
        if other > 1:
            for i in range(other-1):
                out += self
        return DiscreteDist(out)
    
    def __rmul__(self, other):
        return self.__mul__(other)
                

    
    def __str__(self):
        return str(self.dist)


    def advantage(self):
        out = [0] * self.size
        for i in range(self.size):
            for j in range(self.size):
                if i > j:
                    out[i] += self.dist[i]*self.dist[j]
                if j >= i:
                    out[j] += self.dist[i]*self.dist[j]
        return DiscreteDist(out)

    def disadvantage(self):
        out = [0] * self.size
        l = len(self.dist)
        for i in range(self.size):
            for j in range(self.size):
                if i < j:
                    out[i] += self.dist[i]*self.dist[j]
                if j <= i:
                    out[j] += self.dist[i]*self.dist[j]
        return DiscreteDist(out)
