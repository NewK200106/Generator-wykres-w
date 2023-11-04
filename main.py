import matplotlib.pyplot as plt
import numpy as np

# Twoje dane
data = {
    'L1-N': [0.598, 0.356, 0.306, 0.000, 1.2, 0.7, 0.6, 1.9, 0.6, 2.0],
    'L2-N': [0.306, 0.599, 0.355, 0.000, 0.6, 1.3, 0.7, 0.6, 2.0, 1.9],
    # Dodaj resztę danych tutaj...
}

# Tworzenie wykresu
fig, ax = plt.subplots()

for label, values in data.items():
    ax.quiver([0], [0], [np.cos(values)], [np.sin(values)], angles='xy', scale_units='xy', scale=1, label=label)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xlabel('Re')
ax.set_ylabel('Im')
ax.legend()

plt.show()
