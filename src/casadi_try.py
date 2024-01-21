#!/usr/bin/env python

import casadi as casadi

s0 = casadi.SX.sym("a", 2, 3)  # シンボルaとして定義
s1 = casadi.SX(2, 3)
s2 = casadi.SX([[1, 2], [3, 4]])

print(s0)
print(s1)
print(s2)


M = casadi.SX(casadi.diag([2, 3, 4, 5]))
print(M)
print(M[1:3, :3])
M[0, :] = 2
print(M)

x = casadi.SX.sym('x')
y = casadi.SX.sym('y', 2, 2)
f = casadi.sqrt(x**2+10)
print(f)
print(casadi.sin(y)-x)
print(y * y)
print(y@y)
