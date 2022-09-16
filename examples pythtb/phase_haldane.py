import numpy as np
import matplotlib.pyplot as plt

def k_path(points, h):

	k = []
	for p1, p2 in zip(points[:-1], points[1:]):
	
		kx=np.linspace(p1[0],p2[0],h)
		ky=np.linspace(p1[1],p2[1],h)
        
		k.append(np.array(list(zip(kx,ky))))
    
	return np.concatenate(k)

d1 = (1/2)*np.array([1, np.sqrt(3)])
d2 = (1/2)*np.array([1, -np.sqrt(3)])
d3 = np.array([-1,0])

d = [d1,d2,d3]

a1 = d1-d3
a2 = d2-d3

a = [a1,a2]

plt.style.use("science.mplstyle")

fig, ax = plt.subplots()

Hz = lambda phi, m,s: m + s*3*np.sqrt(3)*np.sin(phi)
gz = lambda phi, s: s*3*np.sqrt(3)*np.sin(phi)

m = np.linspace(-np.sqrt(3)*3,np.sqrt(3)*3,1001)
phi = np.linspace(-np.pi, np.pi,1001)

#plt.xlabel(r"$\phi$") ; plt.ylabel(r"$\frac{m}{t'}$")
ax.set_xticks([-np.pi, 0, np.pi])
ax.set_xticklabels([r"$-\pi$", r"$\phi$", r"$\pi$"])
ax.set_yticks([-np.sqrt(3)*3, 0, np.sqrt(3)*3])
ax.set_yticklabels([r"$-3 \sqrt{3}$", r"$\frac{m}{t'}$", r"$3 \sqrt{3} $"])

ax.text(-0.5, -3*np.sqrt(3) + 0.5, r"$C = 0$" )
ax.text(-0.5, +3*np.sqrt(3) - 0.5, r"$C = 0$" )
ax.text(-2*np.pi/3, 0, r"$C = -1$")
ax.text(np.pi/3, 0, r"$C = 1$")

ax.plot(phi, gz(phi, 1))
ax.plot(phi, gz(phi,-1) )
fig.tight_layout()
fig.savefig("phase_haldane.pdf")
plt.show()
