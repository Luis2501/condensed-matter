import numpy as np
import matplotlib.pyplot as plt

a = 1.42
t = 2.7

d1 = (a/2)*np.array([1, np.sqrt(3)])
d2 = (a/2)*np.array([1, -np.sqrt(3)])
d3 = -a*np.array([1,0])

d = [d1,d2,d3]

K = np.array([(2*np.pi)/(3*a), (2*np.pi)/(3*a*np.sqrt(3))])
KK = np.array([(2*np.pi)/(3*a), -(2*np.pi)/(3*a*np.sqrt(3))])
M = np.array([K[0], 0])
F = np.array([0,0])

f = lambda kx,ky: -t*sum([np.exp(-1j*np.dot(d[i], np.array([kx,ky]))) for i in range(3)])

Argf = lambda kx,ky: np.arctan(f(kx,ky).imag/f(kx,ky).real)

E = lambda kx,ky: np.sqrt(f(kx,ky)*np.conjugate(f(kx,ky)))

c = np.linspace(0, 1, 1001)
FM = np.zeros((len(c), 2))
KM = np.zeros((len(c), 2))
MKK = np.zeros((len(c), 2))
KKF = np.zeros((len(c), 2))

for i in range(len(c)):

  FM[i] = c[i]*K
  KM[i] = c[i]*(M-K) + K
  MKK[i] = c[i]*(KK-M) + M
  KKF[i] = c[i]*(F-KK) + KK

Path = [FM, KM, MKK, KKF]

file = open("data.csv", "w")
#file1 = open("data2.csv", "w")

#file.write("t, Pi band, Pi* band \n")

for l in range(4):

	for i in range(len(c)):

		file.write(f"{c[i] + l}, {E(Path[l][i][0], Path[l][i][1]).real}, {c[i] + l}, {-E(Path[l][i][0], Path[l][i][1]).real} \n")
#		file1.write(f"{c[i] + l}, {-E(Path[l][i][0], Path[l][i][1]).real} \n ")

#file1.close()
file.close()

plt.style.use("seaborn")

for l in range(4):

	for i in range(len(c)):

		plt.plot(c+l, E(Path[l][:,0], Path[l][:,1]).real, color="black")
		plt.plot(c+l, -E(Path[l][:,0], Path[l][:,1]).real, color="black")


plt.show()
