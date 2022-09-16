import numpy as np
import matplotlib.pyplot as plt

plt.style.use("science.mplstyle")

R = lambda theta: np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

fig = plt.figure(figsize=(10, 5))

K = np.array([(2*np.pi)/(3), (2*np.pi)/(3*np.sqrt(3))])
KK = np.array([(2*np.pi)/(3), -(2*np.pi)/(3*np.sqrt(3))])

#Brillouin Zone
BZ = []

for i in range(3):
    BZ.append(np.dot(R(i*2*np.pi/3), KK))
    BZ.append(np.dot(R(i*2*np.pi/3), K))

BZ.append(KK)
BZ = np.asarray(BZ)

d = [np.array([1/2, np.sqrt(3)/2]), np.array([1/2, -np.sqrt(3)/2]), np.array([-1, 0])]

f = lambda x,y: -1*sum([np.exp(-1j*(x*d[i][0]+ y*d[i][1])) for i in range(3)])

x,y = np.meshgrid(np.arange(-np.pi, np.pi, 0.005), np.arange(-np.pi, np.pi, 0.005))

E = np.sqrt(3 + 2*np.cos(np.sqrt(3)*y) + 4*np.cos(np.sqrt(3)*y/2)*np.cos(3*x/2))

ax = fig.add_subplot(1,1,1, projection='3d')

cp = ax.contourf(x, y, E, zdir="z", offset=-4, cmap="coolwarm")

ax.plot_surface(x,y, np.sqrt((x -K[0])**2 + (y-K[1])**2), color=(0.25,0.34,0.45))
ax.scatter(BZ[:,0], BZ[:,1], zs=-4, zdir='z', color="black")
ax.plot_surface(x,y, E, cmap="coolwarm")#color=(0.25,0.34,0.45))#cmap="gray")
ax.plot_surface(x,y, -E, cmap="coolwarm")


ax.plot(BZ[:,0], BZ[:,1], zs=-4, zdir='z', color="black")
#fig.colorbar(cp)

ax.text(0, 0, -4, r"$\Gamma$", (1,0,0))
ax.text(K[0]+0.25, K[1]-0.25, -4, r"$K$", (1,0,0))
ax.text(KK[0]+0.25, KK[1]-0.25, -4, r"$K'$", "x")

ax.set_xlim(-K[0] -0.5, K[0]+0.5)
ax.set_ylim(-K[1] -0.5, K[1]+0.5)
ax.set_zlim(-0.5,0.5)

ax.grid(False)

ax.set_zlabel("Energía (eV)")
ax.set_ylabel(r"$k_y$")
ax.set_xlabel(r"$k_x$")

ax.view_init(10, -56) 

fig.tight_layout()
fig.savefig("graphene4.pdf")
plt.show()
