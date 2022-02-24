#
# Listes et tableaux
# Cela semble très proche mais c'est vraiment différent !
#
# Vincent Legat - 2018
# Ecole Polytechnique de Louvain
#

from numpy import *


#
# -1- Quatre manières d'initialiser un truc avec 4 zeros : mais c'est différent
#

def printAll(string,A):
  print(" === A = %20s" % string,end='');
  print(" : A[2] = ",end=''); print(A[2],end='')
  print(" : A = ",end=''); print(A,end='')
  print(" : type(A) = ",end=''); print(type(A))
    
A = [0]*4;                    printAll("[0]*4",A)                     # On définit une liste avec 4 zéros
A = zeros(4);                 printAll("zeros(4)",A)                  # On définit un tableau avec 4 zéros
A = [0,0,0,0];                printAll("[0,0,0,0]",A)                 # On définit une liste 
A = array([0,0,0,0]);         printAll("array([0,0,0,0]",A)           # On définit un tableau 4
A = array([[0],[0],[0],[0]]); printAll("array([[0],[0],[0],[0]])",A)  # On définit un tableau 4,1

#
# -2- Les listes peuvent être automatiquement upgradées si nécessaires mais pas toujours....
#

print(" === Computing [1,2]*[1,2] ?"); 
C = array([1,2])*array([1,2]);    print(C)   # ok : on multiplie deux tableaux entre eux :-)
C = array([1,2])*[1,2];           print(C)   # ok : on upgrade la seconde liste à un tableau
C = [1,2]*array([1,2]);           print(C)   # ok : on upgrade la première liste à un tableau
#C = [1,2]*[1,2];                 print(C)   # ko .... on peut pas multiplier terme à terme deux listes :-(

print(" === Computing [1,2]@[1,2] ?");
C = array([1,2]) @ array([1,2]);  print(C)   # ok : on multiplie deux tableaux entre eux :-)
C = array([1,2]) @ [1,2];         print(C)   # ok : on upgrade la seconde liste à un tableau
C = [1,2] @ array([1,2]);         print(C)   # ok : on upgrade la première liste à un tableau
#C = [1,2] @ [1,2];               print(C)   # ko .... on peut pas multiplier terme à terme deux listes :-(

#
# La manière prudente est d'écrire systématiquement array() pour avoir des tableaux mais
# c'est plus long et moins joli....  Donc, le professeur ne le fait pas :-( sauf si indispensable !
#

#
# -3- Opérations par composantes et produits matriciels pour des tableaux
#

print(" === Defining [0,2,4,8] and [[0],[2],[4],[8]] and playing with :-)"); 
A = array([0,2,4,8]);             print(A)
B = array([[0],[2],[4],[8]]);     print(B)

C = shape(A);                     print(C)
C = shape(B);                     print(C)
C = A*A;                          print(C)
C = A*B;                          print(C)
C = B*A;                          print(C)
C = B*B;                          print(C)
C = A @ A;                        print(C)
C = B @ B.T;                      print(C)
C = B.T @ B;                      print(C)
C = A @ B;                        print(C)
C = B.T @ A;                      print(C)

