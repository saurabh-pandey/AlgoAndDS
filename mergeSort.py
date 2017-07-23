def merge(A, B, C):
    i = j = k = 0
    while ( i < len(A)):
        if ( (j < len(B)) and (k < len(C)) ):
            if (B[j] < C[k]):
                A[i] = B[j]
                j += 1
            else:
                A[i] = C[k]
                k += 1
            i = i + 1
        elif (j < len(B)):
            A[i:] = B[j:]
            i = len(A)
        elif (k < len(C)):
            A[i:] = C[k:]
            i = len(A)

def sort(A):
    if (len(A) < 2):
        return
    
    mid = len(A)/2
    B = A[:mid]
    C = A[mid:]
    sort(B)
    sort(C)
    merge(A, B, C)
