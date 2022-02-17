#
# Manipulation des listes :-)
# Comment retirer les zéros parasites du début d'une liste !
# Quasiment tous les étudiants n'y arrivent pas !
#
# [0,0,4,6,0,7] ==> [4,6,0,7]
# [0,0]         ==> []
#
# L'algorithme est bien :
# "tant que le premier éléement est non nul, le retirer..."
# Il faut donc bien utiliser "while" :-) :-)
#
# Vincent Legat - 2020
# Ecole Polytechnique de Louvain
#

#
# -1- La fonction avec plein de jolis prints pour comprendre :-)
#

def removeZerosVerbose(R):
    step = 0
    while (R != [] and abs(R[0]) <= 1e-8):
        step += 1
        print("     = %2d == R = " % step, end="")
        print(R)
        R.pop(0)

#
# -2- Le code final :-)
#


def removeZeros(R):
    while (R != [] and abs(R[0]) <= 1e-8):
        R.pop(0)

#
# -3- Les tests :-)
#


B = [[0, 0, 0, 0, 4, 6, 0, 7],
     [0, 0, 0],
     [4, 6, 8, 0, 0]]

for A in B:
    print("===============================================")
    print("   ====== Before ===", end="")
    print(A)
    removeZerosVerbose(A)
    print("   ====== After  ===", end="")
    print(A)

#
# Pourquoi est-ce que je redefinis ici B ?
# Retire la ligne et qu'observes-tu ?
#

B = [[0, 0, 0, 0, 4, 6, 0, 7],
     [0, 0, 0],
     [4, 6, 8, 0, 0]]

for A in B:
    print("===============================================")
    print("   ====== Before ===", end="")
    print(A)
    removeZeros(A)
    print("   ====== After  ===", end="")
    print(A)
