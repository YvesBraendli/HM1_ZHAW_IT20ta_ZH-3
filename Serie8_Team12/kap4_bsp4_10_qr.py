import numpy as np

#A = np.array([ [1, 2, -1], [4, -2, 6], [3, 1, 0] ], dtype=np.float64)
A = np.array([ [1, -2, 3], [-5, 4, 1], [2, -1, 3] ])

def householder(a):
    u = np.array(a, dtype=np.float64)
    u[0] += np.sign(a[0])*np.linalg.norm(a)
    u = u/np.linalg.norm(u)
    
    return np.eye(u.size) - 2*np.outer(u,u)
    
    
Q1 = householder(A[:,0])
A1 = Q1 @ A

print('Q1=',Q1)
print('A1=',A1)
print()

Q2 = np.eye(A.shape[0])
Q2[1:,1:] = householder(A1[1:,1])

R = Q2 @ A1

print('Q2=',Q2)
print('R=',R)
print()

Q = np.transpose(Q2 @ Q1)
print('Q=',Q)
print('Q*R=',Q @ R)
print()
