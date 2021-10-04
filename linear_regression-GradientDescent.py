import numpy as np
import random
from sympy import symbols,diff,Add,Mul,Rational,sympify
x=[1,2,3,4,5]
y=[2,5,7,8,9]
wvar=random.random()
bvar=random.random()
w,b=symbols('w b',imaginary=True)
cost=0
for i in range(len(x)):
    cost=cost+(y[i]-(x[i]*w+b))**2
cost=cost/len(x)
gradient_w=diff(cost,w)
gradient_b=diff(cost,b)
n=int(input("iteration: "))
lr=input("learning rate: ")

print(gradient_w,gradient_b)
for i in range(n):
    wvar=Add(sympify(wvar),-Mul(Sympify(lr),gradient_w.subs({w:wvar,b:bvar})))
    bvar=Add(sympify(bvar),-Mul(Sympify(lr),gradient_b.subs({w:wvar,b:bvar})))
    if(i%100==0):
        print(i)
    

print('{0:.3g}'.format(wvar)+"x+ "+'{0:.3g}'.format(bvar)+"b")
