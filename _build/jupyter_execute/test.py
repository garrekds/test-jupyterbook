# Testing Making a Jupyter Book

Let's import what we need.

import numpy as np
import matplotlib.pyplot as plt

## Data

First we need some data, so let's make some test data. Here, we'll make a Lorentzian function and add some noise.

def lorentzian(omega, omega0, amp, gamma):
    return amp/np.pi * gamma / ((omega - omega0)**2 + gamma**2)

frequency = np.linspace(500, 3000, 100)  # cm-1

lor = lorentzian(frequency, 2000, 5.0, 100.0)
lor_noise = lor + np.random.normal(size=lor.size, scale=0.001)

fig, ax = plt.subplots()

ax.scatter(frequency, lor_noise)


plt.show()