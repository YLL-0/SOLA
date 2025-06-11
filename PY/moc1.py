import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Generiraj podatke o gibanju sklepov
t = np.linspace(0, 2 * np.pi, 100)
x = np.sin(t) * 1.5
y = np.cos(t) * 1.5
z = t / 2

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# Prikaži telo kot kinematično verigo
ax.plot(x, y, z, "b-", lw=2, label="Gibanje sklepov")
ax.scatter(x[::10], y[::10], z[::10], c="r", s=100, marker="o")

# Nastavitve grafa
ax.set_xlabel("X os (m)")
ax.set_ylabel("Y os (m)")
ax.set_zlabel("Čas (s)")
ax.set_title("3D Analiza gibanja sklepov")
ax.legend()

plt.tight_layout()
plt.savefig("biomechanics_3d.png", dpi=300)
plt.show()
