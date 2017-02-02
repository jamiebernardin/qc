from sympy import Matrix, sqrt, Symbol
from ten_prod import ten_prod
from numpy import sqrt

 # single qubit quantum states


q0 = Matrix([[1], [0]])
q1 = Matrix([[0], [1]])

# Pauli gates

I = Matrix([[1, 0], [0, 1]])
X = Matrix([[0, 1], [1, 0]])
Y = Matrix([[0, 1], [-1, 0]])
Z = Matrix([[1, 0], [0, -1]])

# Hadamard gate

H = 1/sqrt(2)*Matrix([[1, 1], [1, -1]])

# 1 qubit Hadamard states

h0 = 1/sqrt(2)*(q0 + q1)
h1 = 1/sqrt(2)*(q0 - q1)

# two qubit states

# standard basis

q00 = ten_prod(q0, q0)
q10 = ten_prod(q1, q0)
q01 = ten_prod(q0, q1)
q11 = ten_prod(q1, q1)

q000 = ten_prod(q00, q0)
q001 = ten_prod(q00, q1)
q011 = ten_prod(q01, q1)
q010 = ten_prod(q01, q0)
q101 = ten_prod(q10, q1)
q100 = ten_prod(q10, q0)
q111 = ten_prod(q11, q1)
q110 = ten_prod(q11, q0)

# bell states

b00 = (q00 + q11)/sqrt(2)
b01 = (q01 + q10)/sqrt(2)
b10 = (q00 - q11)/sqrt(2)
b11 = (q01 - q10)/sqrt(2)

# some operators

Cnot = ten_prod(ten_prod(q0, q0.T), I) + ten_prod(ten_prod(q1, q1.T), X)

# symbolic state for teleportation

a = Symbol('a')
b = Symbol('b')
phi = a*q0 + b*q1

t1 = ten_prod(Cnot, I)
t2 = ten_prod(H, ten_prod(I, I))

alice = t2*t1*ten_prod(phi,b00)

bob00 = 2*((q001.T).dot(alice)*q1 + (q000.T).dot(alice)*q0)
bob01 = 2*((q011.T).dot(alice)*q1 + (q010.T).dot(alice)*q0)
bob10 = 2*((q101.T).dot(alice)*q1 + (q100.T).dot(alice)*q0)
bob11 = 2*((q111.T).dot(alice)*q1 + (q110.T).dot(alice)*q0)

print 'bob receives 00 classical bits applies I operator:'
print I*bob00
print 'bob receives 01 classical bits applies X operator:'
print X*bob01
print 'bob receives 10 classical bits applies Z operator:'
print Z*bob10
print 'bob receives 00 classical bits applies Y operator:'
print Y*bob11



