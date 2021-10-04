import numpy as np
x=[1,2,3,4,5]
y=[1,3,5,7,9]
""" for i in range(n):
    x.append(input(str(i)+"번째 x값"))
    y.append(input(str(i)+"번째 y값")) """
avg_x=np.mean(x)
avg_y=np.mean(y)
vsum = 0 
for i in range(len(x)): 
    vsum = vsum + (y[i]-avg_y)*(x[i]-avg_x)
cov= vsum / len(x)
w=cov/np.var(x)
b=avg_y-avg_x*w
print(str(w)+"x+ "+str(b))



