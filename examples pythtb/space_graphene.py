import matplotlib.pyplot as plt
import numpy as np

plt.style.use("science.mplstyle")

t=1

R = lambda theta: np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

#Points of higher symmetry
K = np.array([(2*np.pi)/(3), (2*np.pi)/(3*np.sqrt(3))])
KK = np.array([(2*np.pi)/(3), -(2*np.pi)/(3*np.sqrt(3))])

#Brillouin Zone
BZ = []

for i in range(3):
    BZ.append(np.dot(R(i*2*np.pi/3), KK))
    BZ.append(np.dot(R(i*2*np.pi/3), K))

BZ.append(KK)
BZ = np.asarray(BZ)

#Vectors of nearest neighbor
d = [(1/2)*np.array([1, np.sqrt(3)]), (1/2)*np.array([1, -np.sqrt(3)]), 
     -np.array([1,0])]

f = lambda kx,ky: -t*sum([np.exp(-1j*(d[i][0]*kx + d[i][1]*ky)) for i in range(3)])

x,y = np.meshgrid(np.arange(-np.pi, np.pi, .2), np.arange(-np.pi, np.pi, .2))
u = f(x,y).real
v = f(x,y).imag

fig, ax = plt.subplots()

ax.plot(BZ[:,0], BZ[:,1], color="gray")
ax.scatter(BZ[:,0], BZ[:,1], color="gray")

ax.quiver(x, y, u, v, color=(0.25,0.34,0.45))
#ax.quiverkey(q, X=0.3, Y=1.1, U=10,
 #            label='Quiver key, length = 10', labelpos='E')

ax.set_xlabel(r"$k_x$") ; ax.set_ylabel(r"$k_y$")

plt.show()
