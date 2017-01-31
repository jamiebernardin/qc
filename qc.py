from sympy import Matrix
from ten_prod import ten_prod


sqrt2 = 2**.5

 # single qubit quantum states


s0 = Matrix([[1], [0]])
s1 = Matrix([[0], [1]])

# Pauli gates

I = Matrix([[1, 0], [0, 1]])
X = Matrix([[0, 1], [1, 0]])
Y = Matrix([[0, -1j], [1j, 0]])
Z = Matrix([[1, 0], [0, -1]])

# Hadamard gate

H = 1/sqrt2*Matrix([[1, 1], [1, -1]])

# 1 qubit Hadamard states

h0 = 1/sqrt2*(s0 + s1)
h1 = 1/sqrt2*(s0 - s1)

# two qubit states

# standard basis

s00 = ten_prod(s0, s0)
s10 = ten_prod(s1, s0)
s01 = ten_prod(s0, s1)
s11 = ten_prod(s1, s1)

# bell basis

b00 = (s00 + s11)/sqrt2
b01 = (s01 + s10)/sqrt2
b10 = (s00 - s11)/sqrt2
b11 = (s01 - s10)/sqrt2

# other operators

Cnot = ten_prod(ten_prod(s0, s0.T), I) + ten_prod(ten_prod(s1, s1.T), X)


