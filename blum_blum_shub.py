class Blum_Blum_Shub:

    #Constructor
    def __init__(self, blum_seed):
        self.blum_seed = blum_seed
        self.p = 7
        self.q = 11
        self.M = self.p*self.q
        self.out = blum_seed


    #For genration of random numbers
    def generate(self, k):
        self.out = (self.out**2)%self.M
        return self.out

    #For finding time period
    def time_period(self, k):
        self.out = self.blum_seed
        time_period = 0
        while(True):
            time_period = time_period + 1
            self.generate(k)
            if self.out == self.blum_seed:
                break
        
        return time_period
