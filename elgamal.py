import random

from params import p
from params import g

# Generate a random integer   a  in the range   1,…,q , where   q  is the order of   g .
# In our case,   q=(p−1)/2 , but if   q  is unknown, it suffices to generate   a  uniformly in the range   1,…,p , 
# because if   a  is generated uniformly at random from the range   1,…,p , then   amodq  will be almost uniformly 
# distributed in the range   0,…,q−1 .

def keygen():
    q = (p - 1)/2
    a = random.randint(1,q)
    h = pow(g, a, p)

    sk = a
    pk = h
    print(sk)
    return pk,sk

def encrypt(pk,m):
    q = (p - 1)/2
    r = random.randint(1,q)

    c1 = pow(g, r, p)
    c2 = (pow(pk, r, p) * (m % p)) % p
    return [c1,c2]

def decrypt(sk,c):

    print(c[0])

    m = 0
    return m