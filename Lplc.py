import numpy as np
def expansao_de_dominio(A):
    if A.shape[0] == 2:
        return A[0,0]*A[1,1] - A[0,1]*A[1,0]
    det = 0
    for line in range(A.shape[1]):
        submatriz = np.delete(A, 0, axis =0)
        submatriz = np.delete(submatriz, line, axis=1)
        det += (-1)** (line)* A[0, line] * expansao_de_dominio(submatriz)
    return det
entrada = input('Digite sua matriz em linhas(Ex: [1,2,3], [4,5,6]...)')
A_1 = np.array(eval(entrada))
A = eval(A_1.replace('^','**'))
det = expansao_de_dominio(A)
print(f'A determinante de sua matriz é {det}')
