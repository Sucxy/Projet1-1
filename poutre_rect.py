import math

# Initialisation des variables

F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm
b = 10  # en mm
h = 20  # en mm
print F
# Calcul de l'inertie
I = (b*(h**3))/12
print(I)

# Calcul de la déformation maximale

delta_max = (F*(L**3))/(3*E*I)
print(delta_max)
