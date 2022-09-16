import matplotlib.pyplot as plt
from pythtb import * 
import numpy as np

class solve():


class graphene:

	def __init__(self, t, m, spin = None):
	
		self.t  = t						#Hopping parameter
		self.m = m						#Relative mass parameters
		
		if isinstance(t, (list, tuple)):
		
			pass		
		
		elif isinstance(t, (int, float)):
		
			pass
		
		self.lattice = [[  1   ,        0     ],		#Vectors of honeycomb lattice
				[ 0.5  , np.sqrt(3)/2 ]]
		
		self.orbitals = [[ 1/3 , 1/3 ],				#Positions of orbitals
				 [ 2/3 , 2/3 ]]
				 
		if not spin:		 
				 
			self.model = tb_model(2, 2, lattice, orbitals)		 
		
		else:
		
			self.model = tb_model(2, 2, lattice, orbitals, spin)
				 
	def hamiltonnian(self):
	
		for i in range()
		
			
		
		else:
		
			pass
