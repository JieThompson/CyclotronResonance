#!/usr/bin/env python3

from numpy import genfromtxt
import matplotlib.pyplot as plt

omega, B = genfromtxt('data.txt', delimiter=',', skip_header=1, unpack=True)
print("Omega:")
print(omega)

print("B:")
print(B)

fig = plt.figure()
fig.suptitle("Cyclotron Resonance")

ax = fig.add_subplot(111)
ax.set_xlabel("B[Tesla]")
ax.set_ylabel("Resonance Frequency[Radians]")

plt.scatter(B, omega)
plt.show()
