import numpy as np
import matplotlib.pyplot as plt
plt.axis([-75,75,-50,50])
plt.axis('off')
plt.grid(False)
plt.scatter(0,0,s=25,color='r') #-------nucleus
r1=3
r2=16
dr=1
phi1=0
phi2=360.*np.pi/180.
dphi=2.*np.pi/180.
for r in np.arange(r1,r2,dr):
    for phi in np.arange(phi1,phi2,dphi):
        x=r*np.cos(phi)
        y=r*np.sin(phi)
        clr=(r-r1)/(r2-r1) #intensity decreases linearly
#from the nucleus
plt.scatter(x,y,s=5,color=(clr,clr,clr))
plt.text(20,20,'1s orbital')
plt.show()