import numpy as np
import matplotlib.pyplot as plt

plt.style.use("science.mplstyle")

fig = plt.figure(figsize=(10, 5))

d = [np.array([1/2, np.sqrt(3)/2]), np.array([1/2, -np.sqrt(3)/2]), np.array([-1, 0])]

f = lambda x,y: -1*sum([np.exp(-1j*(x*d[i][0]+ y*d[i][1])) for i in range(3)])

x,y = np.meshgrid(np.arange(-np.pi, np.pi, 0.005), np.arange(-np.pi, np.pi, 0.005))

E = np.sqrt(f(x,y)*np.conjugate(f(x,y)))

ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface(x,y, E.real)
ax.plot_surface(x,y, -E.real)

ax.grid(False)

ax.set_zlabel("Energía (eV)")
ax.set_ylabel(r"$k_y$")
ax.set_xlabel(r"$k_x$")

fig.tight_layout()
fig.savefig("graphene4.pdf")
plt.show()
