import numpy as np

def k_path(points, h):

	k = []
	for p1, p2 in zip(points[:-1], points[1:]):
	
		kx=np.linspace(p1[0],p2[0],h)
		ky=np.linspace(p1[1],p2[1],h)
        
		k.append(np.array(list(zip(kx,ky))))
    
	return np.concatenate(k)

## Semenoff

def d_S(k):

	m = 0.2
	d1 = np.array([np.sqrt(3)/2, 1/2])
	d2 = np.array([-np.sqrt(3)/2, 1/2])
	d3 = np.array([0,-1])
	
	delta = [d1, d2, d3]
	a1 = d3-d1 ; a2 = d3-d2
	
	f = lambda k: sum([np.exp(1j*(k.dot(delta[i]))) for i in range(3)])
	
	g = np.array([f(k).real, f(k).imag, m])
	
	return g/np.linalg.norm(g)
	
def d_H(k, phi, m):

	d1 = np.array([np.sqrt(3)/2, 1/2])
	d2 = np.array([-np.sqrt(3)/2, 1/2])
	d3 = np.array([0,-1])
	
	t1 = 1; t2 = 1
	
	delta = [d1, d2, d3]
	a1 = d3-d1 ; a2 = d3-d2 ; a3 = d1-d2 
	
	a = [a1, -a2, a3]
	
	f = lambda k: t1*sum([np.exp(1j*(k.dot(delta[i]))) for i in range(3)])
	h = lambda k: sum([np.exp(1j*(k.dot(a[i]))) for i in range(3)])
	
	g = np.array([f(k).real, f(k).imag, m + 2*t2*np.sin(phi)*h(k).imag])
	
	return g/np.linalg.norm(g)
	
if __name__ == "__main__":

	K = np.array([4*np.pi/(3*np.sqrt(3)), 0])
	KK = np.array([-4*np.pi/(3*np.sqrt(3)), 0])
	F = np.array([0, 0])	
	M = (1/2)*K
	
	path = [F, KK, M, K, F]
	kpath = k_path(path, 101)

	import matplotlib.pyplot as plt	
	#from mpl_toolkits import mplot3d
	
	plt.style.use("../science.mplstyle")
	
	ax = plt.figure().add_subplot(projection='3d')
	
	
	
	def sphere(r):
	
		u = np.linspace(0, 2*np.pi, 50)
		v = np.linspace(0, np.pi, 50)
		x = r*np.outer(np.cos(u), np.sin(v))
		y = r*np.outer(np.sin(u), np.sin(v))
		z = r*np.outer(np.ones(np.size(u)), np.cos(v))
		
		return x,y,z
 
	x,y,z = sphere(0.98)
	#ax.plot_surface(x, y, z)
	
	for m in [-0.2, 0, 0.2]:
	
		for phi in [-np.pi/2, 0, np.pi/2]:
	
			X, Y, Z = [], [], []
			for i in range(len(kpath)):
	
				x, y, z = d_H(kpath[i], phi,m)
				X.append(x) ; Y.append(y) ; Z.append(z)
	
			ax.plot(X, Y, Z, linewidth=1)
		
			del X, Y, Z	
	plt.show()
