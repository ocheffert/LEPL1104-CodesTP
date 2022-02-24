#
# Tracer une courbe avec de NURBS
#
# Vincent Legat - 2018
# Ecole Polytechnique de Louvain
#

from numpy import *
import matplotlib.pyplot as plt


#
# -1- Définition récursive des B-splines
#     Simple application de la formule mais le code fonctionne avec un argument t
#     qui peut être un tableau
#

def b(t, T, i, p):
    if p == 0:
        return (T[i] <= t)*(t < T[i+1])
    else:
        u = 0.0 if T[i+p] == T[i] else (t-T[i]) / \
            (T[i+p] - T[i]) * b(t, T, i, p-1)
        u += 0.0 if T[i+p+1] == T[i +
                                  1] else (T[i+p+1]-t)/(T[i+p+1]-T[i+1]) * b(t, T, i+1, p-1)
        return u

#
# -2- Tracer une courbe de manière vectorielle.
#     Observer que python permet d'implémenter aisément la définition [T_start, T_end[ des NURBS
#     puisque le langage utilise exactement la même convention que celle de la définition
#     formelle du syllabus : so easy !
#


T = [0, 0, 0, 0, 1, 2, 2, 2, 2]
X = [0, 1, 2, 3, 4]
Y = [0, 3, 0, 3, 0]
p = 3
n = len(T)-1

t = arange(T[p], T[n-p], 0.001)

B = zeros((n-p, len(t)))
for i in range(0, n-p):
    B[i, :] = b(t, T, i, p)

#
# Quelles sont ses dimensions : c'est écrit juste au dessus !
# Quelle est la signification de n ?
#

x = X @ B
y = Y @ B
plt.plot(X, Y, '--r', X, Y, 'or', x, y, '-r')

#
# On change un point : seulement UNE PARTIE de la courbe est modifiée....
# Par contre avec des splines usuelles, TOUTE la courbe est modifiée : si, si !
# Voir l'exercice 26
#

X = [5, 1, 2, 3, 4]
Y = [5, 3, 0, 3, 0]
x = X @ B
y = Y @ B
plt.plot(X, Y, '--b', X, Y, 'ob', x, y, '-b')
plt.show()
