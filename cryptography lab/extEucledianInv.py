def modInverse(A, M):
 
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1
 
 

if __name__ == "__main__":
    A = 3
    M = 11
 
    
    print(modInverse(A, M))