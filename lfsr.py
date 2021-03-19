class LFSR:

    #Constructor
    def __init__(self, bits, seed, tap):
        self.seed = seed
        self.bits = bits - 1
        self.tap = bits - tap 
        self.out = seed

    #For genration of random numbers
    def generate(self):
        tap_bit = (int) (self.out[self.tap])
        end_bit = (int) (self.out[0])
        self.out = self.out[1:]
        
        val = str(tap_bit^end_bit)
        self.out = self.out[0:]+val
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
