from __future__ import print_function
from pythtb import * # import TB model class
import numpy as np
import matplotlib.pyplot as plt

# define lattice vectors
lat=[[1.0,0.0],[0.5,np.sqrt(3.0)/2.0]]
# define coordinates of orbitals
orb=[[1./3.,1./3.],[2./3.,2./3.]]

# make two dimensional tight-binding graphene model
my_model=tb_model(2,2,lat,orb)

# set model parameters
delta=0.0
t=-2.7

# set on-site energies
my_model.set_onsite([-delta,delta])
# set hoppings (one for each connected pair of orbitals)
# (amplitude, i, j, [lattice vector to cell containing j])
my_model.set_hop(t, 0, 1, [ 0, 0])
my_model.set_hop(t, 1, 0, [ 1, 0])
my_model.set_hop(t, 1, 0, [ 0, 1])

# print tight-binding model
my_model.display()
    
# generate list of k-points following a segmented path in the BZ
# list of nodes (high-symmetry points) that will be connected
path=[[0.,0.],[2./3.,1./3.],[.5,.5], [2/3, 1/3] , [0.,0.]]
# labels of the nodes
label=(r'$\Gamma $',r'$K$', r'$M$', r"$K'$" , r'$\Gamma $')
# total number of interpolated k-points along the path
nk=121

# call function k_path to construct the actual path
(k_vec,k_dist,k_node)=my_model.k_path(path,nk)
# inputs:
#   path, nk: see above
#   my_model: the pythtb model
# outputs:
#   k_vec: list of interpolated k-points
#   k_dist: horizontal axis position of each k-point in the list
#   k_node: horizontal axis position of each original node

print('---------------------------------------')
print('starting calculation')
print('---------------------------------------')
print('Calculating bands...')

# obtain eigenvalues to be plotted
evals=my_model.solve_all(k_vec)

#plt.style.use("seaborn")
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

d = [np.array([1/2, np.sqrt(3)/2]), np.array([1/2, -np.sqrt(3)/2]), np.array([-1, 0])]

f = lambda x,y: -1*sum([np.exp(-1j*(x*d[i][0]+ y*d[i][1])) for i in range(3)])

x,y = np.meshgrid(np.arange(-np.pi, np.pi, 0.005), np.arange(-np.pi, np.pi, 0.005))

E = np.sqrt(3 + 2*np.cos(np.sqrt(3)*y) + 4*np.cos(np.sqrt(3)*y/2)*np.cos(3*x/2))

fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1, projection='3d')

ax1.plot(BZ[:,0], BZ[:,1], zs=-4, zdir='z', color="black")
ax1.scatter(BZ[:,0], BZ[:,1], zs=-4, zdir='z', color="black")
ax1.plot_surface(x,y, E, color=(0.25,0.34,0.45))#cmap="gray")
ax1.plot_surface(x,y, -E, color=(0.25,0.34,0.45))

ax1.text(0, 0, -4, r"$\Gamma$", (1,0,0))
ax1.text(K[0]+0.25, K[1]-0.25, -4, r"$K$", (1,0,0))
ax1.text(KK[0]+0.25, KK[1]-0.25, -4, r"$K'$", "x")

ax1.set_zlim(-4,4)

ax1.grid(False)

ax1.set_zlabel("Energía (eV)")
ax1.set_ylabel(r"$k_y$")
ax1.set_xlabel(r"$k_x$")

ax1.view_init(10, -56) 

ax2 = fig.add_subplot(1, 2, 2)

ax2.set_xlim(k_node[0],k_node[-1])
ax2.set_xticks(k_node)
ax2.set_xticklabels(label)

for n in range(len(k_node)):
  ax2.axvline(x=k_node[n],linewidth=0.5, color='k')

ax2.set_ylabel("Energía (eV)")
ax2.plot(k_dist,evals[0], color="gray")
ax2.plot(k_dist,evals[1], color="gray")


fig.tight_layout()
fig.savefig("BandStructure.pdf")

plt.show()
