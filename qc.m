% single qubit quantum states

s0 = [1;0];
s1 = [0;1];

% Pauli gates

I = [1, 0; 0 1];
X = [0 1; 1 0];
Y = [0 -i; i 0];
Z = [1 0; 0 -1];

% Hadamard gate

H = 1/sqrt(2)*[1 1; 1 -1];

% 1 qubit Hadamard states

h0 = 1/sqrt(2)*(s0 + s1);
h1 = 1/sqrt(2)*(s0 - s1);

% two qubit states

% standard basis

s00 = ten_prod(s0, s0);
s10 = ten_prod(s1, s0);
s01 = ten_prod(s0, s1);
s11 = ten_prod(s1, s1);

% bell basis

b00 = (s00 + s11)/sqrt(2);
b01 = (s01 + s10)/sqrt(2);
b10 = (s00 - s11)/sqrt(2);
b11 = (s01 - s10)/sqrt(2);

