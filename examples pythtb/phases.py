import matplotlib.pyplot as plt
import numpy as np

plt.style.use("science.mplstyle")
# figure for bandstructure

R = lambda theta: np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

K = np.array([(2*np.pi)/(3), (2*np.pi)/(3*np.sqrt(3))])
KK = np.array([(2*np.pi)/(3), -(2*np.pi)/(3*np.sqrt(3))])

#Brillouin Zone
BZ = []

for i in range(3):
    BZ.append(np.dot(R(i*2*np.pi/3), KK))
    BZ.append(np.dot(R(i*2*np.pi/3), K))

BZ.append(KK)
BZ = np.asarray(BZ)

d = [np.array([1/2, np.sqrt(3)/2]), np.array([1/2, -np.sqrt(3)/2]), -np.array([1, 0])]			#Matrix of the vectors delta

f = lambda x,y: -1*sum([np.exp(-1j*(x*d[i][0]+ y*d[i][1])) for i in range(3)])				#Geomtric structure f(k) 

p = 0.1

#x,y = np.meshgrid(np.arange(-2*np.pi, 2*np.pi, 0.005), np.arange(-2*np.pi, 2*np.pi, 0.005))		#Arrays for plot phase 
x,y = np.meshgrid(np.arange(K[0]-p, K[0]+p, 0.00005), np.arange(K[1]-p, K[1]+p, 0.00005))

#kx,ky = np.meshgrid(np.arange(-2*np.pi, 2*np.pi, 0.5), np.arange(-2*np.pi, 2*np.pi, 0.5))		#Arrays for plot vector field
kx,ky = np.meshgrid(np.arange(K[0]-p, K[0]+p, 0.01), np.arange(K[1]-p, K[1]+p, 0.01))

phi = np.arctan(f(x,y).imag/f(x,y).real)								#Phase

fig,ax=plt.subplots(1,1)										#Create figure

#cp = ax.contourf(x, y, phi, cmap="coolwarm") 								#Colors: coolwarm, RdGy, RdBu	
#fig.colorbar(cp) 

#ax.set_ylim(-2*np.pi, 2*np.pi) ; ax.set_xlim(-2*np.pi, 2*np.pi)

ax.quiver(kx,ky,f(kx,ky).real,f(kx,ky).imag)
#ax.plot(BZ[:,0], BZ[:,1], color="black")
#ax.scatter(BZ[:,0], BZ[:,1], color="black")
ax.set_ylabel(r'$k_y$') ; ax.set_xlabel(r'$k_x$')

fig.tight_layout()
fig.savefig("phases.pdf")

plt.show()


