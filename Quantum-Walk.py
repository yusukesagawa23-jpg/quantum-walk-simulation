import numpy as np
import matplotlib.pyplot as plt

p = np.zeros(201)


psi = np.zeros((201, 2), dtype=complex)
old_psi = np.zeros((201, 2), dtype=complex)


a = 1 / np.sqrt(2)
b = 1 / np.sqrt(2)
c = 1 / np.sqrt(2)
d = -1 / np.sqrt(2)


alpha = 1 / np.sqrt(2)
beta = 1j / np.sqrt(2)


psi[100, 0] = alpha
psi[100, 1] = beta

for t in range(100):

    
    old_psi[:] = psi[:]

  
    psi[:] = 0

   
    for x in range(-100, 101):

        idx = 100 + x

        if x == -100:
            
            psi[100 + (x + 1), 1] += c * old_psi[idx, 0]
            psi[100 + (x + 1), 1] += d * old_psi[idx, 1]

        elif x == 100:
            
            psi[100 + (x - 1), 0] += a * old_psi[idx, 0]
            psi[100 + (x - 1), 0] += b * old_psi[idx, 1]

        else:
            
            psi[100 + (x - 1), 0] += a * old_psi[idx, 0]
            psi[100 + (x - 1), 0] += b * old_psi[idx, 1]

           
            psi[100 + (x + 1), 1] += c * old_psi[idx, 0]
            psi[100 + (x + 1), 1] += d * old_psi[idx, 1]

for x in range(-100, 101):

    idx = 100 + x

    p[idx] = (
        abs(psi[idx, 0])**2
        + abs(psi[idx, 1])**2
    )

    print(f"p({x}) = {p[idx]:.10f}")

import matplotlib.pyplot as plt

x = np.arange(-100, 101)

plt.bar(x, p)
plt.xlabel("Position x")
plt.ylabel("Probability")
plt.title("Quantum Walk at t=100")
plt.show()           