import math

# Initialisation des variables
F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm

# poutre rectangulaire
b = 10  # en mm
h = 20  # en mm

# poutre carrée
a = 15  # en mm

# poutre ronde
d = 5  # en mm

# poutre creuse
D = 15  # en mm
d = 5  # en mm


# Calcul de la section optimale
#Calcul poutre rectangulaire
deltarectangle=(F*(L**3))/(3*E*((b*(h**3))/12))
#Calcul poutre carrée
deltacarre=(F*(L**3))/(3*E*((a**4)/12))
#Calcul poutre ronde
deltarond=(F*(L**3))/(3*E*((math.pi*(d**4)/64)))
#Calcul poutre creuse
deltacreux=(F*(L**3))/(3*E*((math.pi*((D**4)-(d**4)))/64))

#Trouver plus petit delta
if (deltarectangle<deltacarre) and (deltarectangle<deltarond) and (deltarectangle<deltacreux):
    print('Le type de fonction minimisant la deformation maximale est rectangle,avec une deformation de', deltarectangle,'mm')
elif (deltacarre<deltarectangle) and (deltacarre<deltarond) and (deltacarre<deltacreux):
    print('Le type de fonction minimisant la deformation maximale est carré,avec une deformation de', deltacarre,'mm')
elif (deltarond<deltarectangle) and (deltarond<deltacarre) and (deltarond<deltacreux):
    print('Le type de fonction minimisant la deformation maximale est rond,avec une deformation de', deltarond,'mm')
else:
    print('Le type de fonction minimisant la deformation maximale est creux,avec une deformation de', deltacreux,'mm')


