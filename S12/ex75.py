import numpy as np
from scipy.sparse import dok_matrix
from scipy.sparse.linalg import spsolve
from scipy.linalg import solve_banded


def poissonSolve0(nx, ny):
    n = nx*ny
    h = 2/(ny-1)
    A = np.zeros((n, n))
    B = np.zeros(n)
    for i in range(n):
        A[i, i] = 1
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            index = i + j*nx
            A[index, index] = 4.0
            A[index, index-1] = -1.0
            A[index, index+1] = -1.0
            A[index, index-nx] = -1.0
            A[index, index+nx] = -1.0
            B[index] = 1
    A /= h*h
    return np.linalg.solve(A, B).reshape(ny, nx)


def poissonSolve1(nx, ny):
    n = nx*ny
    h = 2/(ny-1)
    A = np.eye(n)
    B = np.zeros(n)
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            index = i + j*nx
            A[index, index] = 4.0
            A[index, index-1] = -1.0
            A[index, index+1] = -1.0
            A[index, index-nx] = -1.0
            A[index, index+nx] = -1.0
            B[index] = 1
    A /= h*h
    return np.linalg.solve(A, B).reshape(ny, nx)


def convergence():
    nx = ny = 2
    error = np.zeros(4)
    Uref = 0   # rempl par slt analytique
    for iRef in range(4):
        nx = 2*nx
        ny = 2*ny
        U = poissonSolve1(nx, ny)
        error[iRef] = np.sqrt(np.amax((Uref - U)**2))
        print(' === Discretization nx = %4d : error = %15.7e ' %
              (nx, error[iRef]))
    order = np.log(abs(error[:-1]/error[1:]))/np.log(2)
    print('\n ===== Estimated order of convergence = %15.7e ' % np.mean(order))


def poissonSolveSparse(nx, ny):
    n = nx*ny
    h = 2/(ny-1)
    A = dok_matrix((n, n), dtype=np.float32)   # dok for assignation
    B = np.zeros(n)
    for i in range(n):
        A[i, i] = 1.0
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            index = i + j*nx
            A[index, index] = 4.0
            A[index, index-1] = -1.0
            A[index, index+1] = -1.0
            A[index, index-nx] = -1.0
            A[index, index+nx] = -1.0
            B[index] = 1
    A = A / (h*h)
    return spsolve(A.tocsr(), B).reshape(ny, nx)    # require a csr format


def poissonSolve_banded(nx, ny):
    n = nx*ny
    h = 2/(ny-1)
    h2 = h*h
    A = np.zeros((2*nx+1, n))
    A[nx, :] = 4.0/h2
    A[nx-1, 1:] = -1.0/h2
    A[0, nx:] = -1.0/h2
    A[nx+1, :-1] = -1.0/h2
    A[-1, 0:-nx] = -1.0/h2
    B = np.ones(n)

    # to_modif will be indices of the boundary points to set to 0
    to_modif = np.zeros(2*(nx+ny)-4, dtype=np.int32)
    nyx_arange = np.arange(ny) * nx
    to_modif[:ny] = nyx_arange                     # côté gauche
    to_modif[ny:2*ny] = nx - 1 + nyx_arange        # côté droit
    nx_arange = np.arange(1, nx-1)
    to_modif[2*ny: 2*ny+nx-2] = nx_arange            # côté bas
    to_modif[2*ny+nx-2:] = nx_arange + (ny - 1)*nx   # côté haut

    B[to_modif] = 0.0
    A[nx, to_modif] = 1.0/h2     # correct the main diagonal
    A[nx+1, to_modif-1] = 0      # first subdiago
    A[-1, to_modif-nx] = 0       # last subdiago
    to_modif[2*ny-1] = -1
    A[nx-1, to_modif+1] = 0      # first updiago
    to_modif[[ny-1, 2*ny-1]] = -nx
    to_modif[2*ny+nx-2:] = -nx
    A[0, to_modif+nx] = 0        # last updiago
    return solve_banded((nx, nx), A, B, overwrite_ab=True, overwrite_b=True).reshape(ny, nx)


def comparison():
    from timeit import default_timer as timer
    nx = ny = 500
    print(' === Considering n = %d' % (nx*ny))
    tic = timer()
    print(poissonSolve1(nx, ny))
    toc = timer() - tic
    print(' === Full solver : elapsed time is %f seconds.' % toc)
    tic = timer()
    poissonSolveSparse(nx, ny)
    toc = timer() - tic
    print(' === Sparse solver : elapsed time is %f seconds.' % toc)
    tic = timer()
    poissonSolve_banded(nx, ny)
    toc = timer() - tic
    print(' === Banded solver : elapsed time is %f seconds.' % toc)


convergence()
comparison()

"""
=== Considering n = 10000
 === Sparse solver : elapsed time is 2.864122 seconds.
 === Banded solver : elapsed time is 0.136980 seconds.


 === Considering n = 250000
 === Sparse solver : elapsed time is 96.720867 seconds.
 === Banded solver : elapsed time is 23.609905 seconds.
"""
