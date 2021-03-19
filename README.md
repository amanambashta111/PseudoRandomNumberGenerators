# PseudoRandomNumberGenerators
**The Linear Congruential Generator**
is given by Eq. 1
Xn+1 = (a * Xn + c) mod m                                           ....(1)
where X is the sequence of pseudo-random values 
m, 0 < m gives the PRNG space, 
a, 0 < a < m is multiplier,
c, 0 ≤ c < m is increment and 
x0 , 0 ≤ x0 < m the seed or start value.


**Blum Blum Shub** 
is given by Eq. 2
xn+1 = (xn* xn) mod M                                                 ...(2)
where M = p * q is the product of two large primes p and q. 
At each step of the algorithm, some output is derived from xn+1 ; the output is commonly either the bit parity of x n+1 or one or more
of the least significant bits of xn+1 . 
The seed x0 should be an integer that is co-prime to M (i.e.
p and q are not factors of x 0 ) and not 1 or 0.



**Linear-feedback shift register**
A linear-feedback shift register (LFSR) is a register of bits that performs discrete step operations that:
shifts the bits one position to the left and replaces the vacated bit by the exclusive or(xor) of the bit shifted off and the bit previously at a given tap position in the register.
A LFSR has three parameters that characterize the sequence of bits it produces: 
the number of bits n, 
the initial seed (the sequence of bits that initializes the register),
and the tap position tap.
