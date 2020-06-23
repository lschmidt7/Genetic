import numpy as np

def CrossProduct(u,v):
    return [(u[0]*v[1]),-(u[1]*v[0])]

def DotProduct(u,v):
    return u[0]*v[0] + u[1]*v[1]

def SameSide(p1,p2, a,b):
    cp1 = CrossProduct(b-a, p1-a)
    cp2 = CrossProduct(b-a, p2-a)
    if(DotProduct(cp1, cp2) >= 0):
        return True
    else:
        return False

def PointInTriangle(p, a,b,c):
    p = np.array(p)
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    if SameSide(p,a, b,c) and SameSide(p,b, a,c) and SameSide(p,c, a,b):
        return True
    else:
        return False