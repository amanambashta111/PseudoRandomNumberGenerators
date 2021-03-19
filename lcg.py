class linear_congruential_generator:

    #Constructor
    def __init__(self, seed, multiplier, m, increment):
        self.seed = seed
        self.multiplier = multiplier
        self.m = m
        self.increment = increment
        self.out = seed

    #For genration of random numbers
    def generate(self):
        self.out = (self.multiplier*self.out + self.increment)%self.m
        return self.out

    #For finding time period
    def time_period(self):
        self.out = self.seed
        time_period = 0
        while(True):
            time_period = time_period + 1
            self.generate()
            if self.out == self.seed:
                break
        
        return time_period

