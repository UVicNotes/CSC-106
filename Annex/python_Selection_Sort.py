def selection_sort(A):
    m = len(A)
    cur_ind = m-1

    while cur_ind > 0:
        cur_max = -99999
        i = 0
        max_ind = 0
        while i <= cur_ind:
            if A[i] > cur_max:
                cur_max = A[i]
                max_ind = i
            i = i + 1
        tmp = A[cur_ind]
        A[cur_ind] = A[max_ind]
        A[max_ind] = tmp
        cur_ind = cur_ind - 1


A = [11,22,3,12,34,9]
print("A= "+str(A))
selection_sort(A)
print("A= "+str(A))
