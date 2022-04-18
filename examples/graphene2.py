#!/usr/bin/env python

# Toy graphene model

# Copyright under GNU General Public License 2010, 2012, 2016
# by Sinisa Coh and David Vanderbilt (see gpl-pythtb.txt)

from __future__ import print_function
from pythtb import * # import TB model class
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("science.mplstyle")

# figure for bandstructure
fig = plt.figure(figsize=(10, 5))

# define lattice vectors
lat=[[1.0,0.0],[0.5,np.sqrt(3.0)/2.0]]
# define coordinates of orbitals
orb=[[1./3.,1./3.],[2./3.,2./3.]]

# generate list of k-points following a segmented path in the BZ
# list of nodes (high-symmetry points) that will be connected
path=[[0.,0.],[2./3.,1./3.],[.5,.5], [2/3, 1/3] , [0.,0.]]
# labels of the nodes
label=(r'$\Gamma $',r'$K$', r'$M$', r"$K'$" , r'$\Gamma $')
# total number of interpolated k-points along the path
nk=121

for m, n in zip(np.arange(0, 1.25, 0.25), range(1,5)):

	# make two dimensional tight-binding graphene model
	my_model=tb_model(2,2,lat,orb)

	# set model parameters
	t=-1.0

	# set on-site energies
	my_model.set_onsite([-m,m])
	# set hoppings (one for each connected pair of orbitals)
	# (amplitude, i, j, [lattice vector to cell containing j])
	my_model.set_hop(t, 0, 1, [ 0, 0])
	my_model.set_hop(t, 1, 0, [ 1, 0])
	my_model.set_hop(t, 1, 0, [ 0, 1])
	
	# call function k_path to construct the actual path
	(k_vec,k_dist,k_node)=my_model.k_path(path,nk, report=False)
	
	# obtain eigenvalues to be plotted
	evals=my_model.solve_all(k_vec)
	
	ax = fig.add_subplot(2, 2, n)
	
	if m==0:
	
		k_vec0, k_dist0, k_node0 = k_vec, k_dist, k_node
		evals0 = evals
		
		ax.plot(k_dist0,evals0[0], color="blue")
		ax.plot(k_dist0,evals0[1], color="blue")
		ax.set_ylabel("Energía (eV)")
		
	else:
	
		# plot first and second band
		ax.plot(k_dist0,evals0[0], color="gray")
		ax.plot(k_dist0,evals0[1], color="gray")
		ax.plot(k_dist,evals[0], color="blue")
		ax.plot(k_dist,evals[1], color="blue")
		
	
	for i in range(len(k_node)):
		ax.axvline(x=k_node[i],linewidth=0.5, color='k')

	ax.set_xlim(k_node[0],k_node[-1])
	ax.set_xticks(k_node)
	ax.set_xticklabels(label)
	
	if n==3: ax.set_ylabel("Energía (eV)")
	
	del my_model, ax


# make an PDF figure of a plot
fig.tight_layout()
fig.savefig("graphene3.pdf")

plt.show()

