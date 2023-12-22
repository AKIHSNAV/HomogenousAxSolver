"""
    -> The number of vectors in null space is equal to the number of free variables in RREF .
    -> The solution is constructed in the following manner :-
        1 ) The length of each vector in the null space will be equal to the number of columns in the matrix.
        2 ) For a free variable we set its corresponding value to 1 and for the rest of the free variables their values to 0.
        3 ) On rest of the places we copy the entries multiplied by -1.
        4 ) Repeat step 2 and 3 for every free variable

 """

def read_file():
    f = open('math.txt', 'r')
    page = f.read()
    lines = page.split('\n')
    n = len(lines)
    m = len(lines[0])
    B = []
    for i in lines:
        a = i.split()
        temp = []
        for x in a:
            temp.append(int(x))
        B.append(temp)
    return B


def swap_row(i, j, T):  # swap ith and jth row
    temp_row = T[i]
    T[i] = T[j]
    T[j] = temp_row
    return T


def multiple_row(i, j, k, T):  # T[i]=T[i]+ kT[j]
    n = len(T)
    m = len(T[0])
    for z in range(m):
        T[i][z] = T[i][z] + (k * T[j][z])
        if abs(T[i][z]) < 1e-5:
            T[i][z] = 0
    return T


def scale_row(i, k, T):  # T[i] = kT[i]
    n = len(T)
    m = len(T[0])
    for z in range(m):
        T[i][z] = (k * T[i][z])
        if abs(T[i][z]) < 1e-5:
            T[i][z] = 0

    return T


def max_leading_entry(i, j, T):
    m, n = len(T), len(T[0])
    index = i
    for k in range(m):  # Calculate the index of the row with the absolute max leading entry
        if k < i :
            continue
        else:
            if abs(T[k][j]) > abs(T[index][j]):
                index = k
    return index


def rref(A):
    m, n = len(A), len(A[0])
    i = 0
    j = 0
    pivot_col = []  # List which contains the columns which have pivots
    while i < m and j < n:
        pivot = max_leading_entry(i, j, A)
        if A[pivot][j] == 0:        # If max leading entry is 0 then we skip the column
            j += 1
        else:
            pivot_col.append(j + 1)
            A = swap_row(i, pivot, A)  # swap the row with the max leading entry with the current row
            A = scale_row(i, 1 / A[i][j], A)  # Make the leading entry 1
            for k in range(m):
                if k == i:
                    continue
                else:
                    A = multiple_row(k, i, -1 * A[k][j], A)  # Make all the entries in col except the pivot  equal to 0
            i += 1
            j += 1
    return A, pivot_col


T = read_file()
print("Input Matrix: ", T)
RREF_T, pivot_col = rref(T)

print("Pivot Columns Numbers  : - ", pivot_col)
print("RREF : - ", RREF_T)

free_vectors = []
free_variables = []
final_ans = []
for i in range(1, len(T[0]) + 1):
    if i not in pivot_col:
        free_vectors.append([col[i - 1] for col in RREF_T])
        free_variables.append(i)

print("Free Variables :- ", free_variables)
print("Free Columns :- ", free_vectors)

for i in range(len(free_variables)):
    temp = [0] * len(RREF_T[0])
    p1 = 0

    for j in range(1, len(RREF_T[0]) + 1):
        if j in free_variables:
            temp[j - 1] = 0
        else:
            temp[j - 1] = -1 * free_vectors[i][p1]
            p1 += 1

    temp[free_variables[i] - 1] = 1
    final_ans.append(temp)

print("Null Space :- ", final_ans)
print('FINAL ANSWER in Parametric Form :-')
for i in (range(len(free_variables))):
    if i != len(free_variables) - 1:
        print(f" x{free_variables[i]}*{final_ans[i]} +", end="")
    else:
        print(f" x{free_variables[i]}*{final_ans[i]}", end="")
