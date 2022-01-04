import numpy as np

class model:

	def __init__(self, vectors, basis = None):
	
		pass
		
	def lattice(self, n1, n2):
	
		self.R = np.zeros(((2*n1 + 1)*(2*n2 + 1),2))
		
		for i in range(-n1, n1):
			for j in range(-n2, n2):
			
				self.R[k] = sum() 
			
		
	def reciprocal(self):
	
		pass

class graphene_model:

	def __init__(self, a = 1):

		self.a_1 = (a/2)*np.array([3, np.sqrt(3)]) 
		self.a_2 = (a/2)*np.array([3, -np.sqrt(3)]) 
		
		self.d1 = (a/2)*np.array([1, np.sqrt(3)])
		self.d2 = (a/2)*np.array([1, -np.sqrt(3)])
		self.d3 = -a*np.array([1, 0])
		
		self.b_1 = (2*np.pi/3*a)*np.array([1, np.sqrt(3)])
		self.b_2 = (2*np.pi/3*a)*np.array([1, -np.sqrt(3)])
		
		self.a = a
		
		self.basis = [0, self.d1, self.d2, self.d3]
		
		self.KK = lambda i,j: i*self.a_1 + j*self.a_2 
		
	def reciprocal_vectors(self):
	
		self.A = np.array([self.a_1, self.a_2])
		
		self.B = 2*np.pi*np.linalg.inv(self.A)
		
		self.b_1, self.b_2 = self.B.transpose()
 

	def lattice(self, n):

		self.R1 = np.zeros(((2*n+1)**2,2))
		self.R2 = np.zeros(((2*n+1)**2,2))
		k, l = 0, range(-n, n+1)

		for i in l:
			for j in l:

				self.R1[k] = i*self.a_1 + j*self.a_2 
				self.R2[k] = i*self.a_1 + j*self.a_2 + self.d3
				k+=1
				
		return self.R1, self.R2

	def reciprocal_lattice(self, n):

		self.K = np.zeros(((2*n+1)**2,2))
		k, l = 0, range(-n, n+1)

		for i in l:
			for j in l:

				self.K[k] = i*self.b_1 + j*self.b_2 
				k+=1
				
		return self.K
	
	def brillouin_zone(self):
	
		K = (2*np.pi/3, (2*np.pi)/(3*np.sqrt(3)))
		KP = (2*np.pi/3, -(2*np.pi)/(3*np.sqrt(3)))
			
		x = np.array([K[0], 0, -K[0], -KP[0], 0, KP[0]])  
		y = np.array([K[1], (2*np.sqrt(3)*np.pi)/3, K[1], KP[1], -(2*np.sqrt(3)*np.pi)/3, KP[1] ]) 
			
		return x, y
		
	def energy(self):
	
		kx, ky = np.arange(-np.pi,np.pi, 0.05), np.arange(-np.pi,np.pi, 0.05)

		KX, KY = np.meshgrid(kx,ky)

		f =  2*np.cos(np.sqrt(3)*KY*self.a) + (4*np.cos((np.sqrt(3)/2)*KY*self.a)*np.cos((3/2)*KX*self.a))

		E = lambda x: x*2.7*np.sqrt(3 + f) + 0.2*(2.7)*f
		
		return E, kx, ky
