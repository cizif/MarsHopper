from sympy.solvers import solve
from sympy import Symbol

M = 0.04401
p = 50 * 10**5
V = 0.002
R = 8.3
T = 290
# m = M*(p*V/(R*T))

V_cell = 0.05
ro_sol = 1562.
ro_liq = 1101.

m_co2 = 50.
V_cell_gas = V_cell - m_co2/ro_sol
V_co2_l = m_co2/ro_liq

p0 = 600 * 10**3
T0 = 140  # -130 C

g = 3.711
# print V_co2_l
a = 0.36088
b = 42.840 / 10**6
x = Symbol("x")
# m = Symbol("m")
m = 30
Vi = Symbol("Vi")
eq = (p + a*(m/M)**2/Vi**2)*(Vi-b*m/M) - m/M * R * T
print solve(eq, Vi)
# print M*(p*V/(R*T))
print (m*R*T)/(p*M)

q_sub = 590 * 10**3
q_fus = 195 * 10**3

def get_energy(M_solid, V0):
    V_gas = V0 - M_solid/ro_sol

    p_triple = 518*(10**3)
    T_triple = 216.55
    m = Symbol("m")
    eq = (p_triple + a*(m/M)**2/V_gas**2)*(V_gas-b*m/M) - m/M * R * T_triple
    mass = M*(p_triple*V_gas )/(R*T_triple)
    mass = solve(eq,m)[0]
    Q = mass * q_sub
    print Q, q_fus*(M_solid-mass)
    return Q

# print get_energy(50, 0.05)