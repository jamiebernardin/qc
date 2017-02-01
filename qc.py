from sympy import Matrix, sqrt, Symbol
from ten_prod import ten_prod
from numpy import sqrt

 # single qubit quantum states


s0 = Matrix([[1], [0]])
s1 = Matrix([[0], [1]])

# Pauli gates

I = Matrix([[1, 0], [0, 1]])
X = Matrix([[0, 1], [1, 0]])
Y = Matrix([[0, 1], [-1, 0]])
Z = Matrix([[1, 0], [0, -1]])

# Hadamard gate

H = 1/sqrt(2)*Matrix([[1, 1], [1, -1]])

# 1 qubit Hadamard states

h0 = 1/sqrt(2)*(s0 + s1)
h1 = 1/sqrt(2)*(s0 - s1)

# two qubit states

# standard basis

s00 = ten_prod(s0, s0)
s10 = ten_prod(s1, s0)
s01 = ten_prod(s0, s1)
s11 = ten_prod(s1, s1)

s000 = ten_prod(s00, s0)
s001 = ten_prod(s00, s1)
s011 = ten_prod(s01, s1)
s010 = ten_prod(s01, s0)
s101 = ten_prod(s10, s1)
s100 = ten_prod(s10, s0)
s111 = ten_prod(s11, s1)
s110 = ten_prod(s11, s0)

# bell states

b00 = (s00 + s11)/sqrt(2)
b01 = (s01 + s10)/sqrt(2)
b10 = (s00 - s11)/sqrt(2)
b11 = (s01 - s10)/sqrt(2)

# some operators

Cnot = ten_prod(ten_prod(s0, s0.T), I) + ten_prod(ten_prod(s1, s1.T), X)

# symbolic state for teleportation

a = Symbol('a')
b = Symbol('b')
phi = a*s0 + b*s1

t1 = ten_prod(Cnot, I)
t2 = ten_prod(H, ten_prod(I, I))

alice = t2*t1*ten_prod(phi,b00)

bob00 = (s001.T).dot(alice)*s1 + (s000.T).dot(alice)*s0
bob01 = (s011.T).dot(alice)*s1 + (s010.T).dot(alice)*s0
bob10 = (s101.T).dot(alice)*s1 + (s100.T).dot(alice)*s0
bob11 = (s111.T).dot(alice)*s1 + (s110.T).dot(alice)*s0

# 00 bit received apply I
I*bob00 == phi
# 01 bit received apply X
X*bob01 == phi
# 10 bit received apply Z
Z*bob10 == phi
# 00 bit received apply Y
Y*bob11 == phi



