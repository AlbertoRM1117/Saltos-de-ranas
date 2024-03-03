def solution(matriz):
    """
        Function that creates a solution to cross to the other side of 
        a matrix using the Fibonacci sequence
    """
    
    N = len(matriz)
    jumps =[-1] * (N+2)
    jumps[0]=0
    

    #We create the Fibonacci series
    fib = [0,1]
    while fib[-1] <= N + 1:
        fib.append(fib[-1] + fib[-2])
       

    #We iterate over the matrix
    for i in range(N +1):
        if jumps[i] !=-1:
            #We iterate the Fibonacci sequence to find out if it can be crossed 
            #to the other side of the river if it does
            # return the minimum number of humps to reach the shore, otherwise it will return -1
            for f in fib:
                jumps_next = i + f
                if jumps_next <= N+1:
                    if jumps_next == N+1:
                        return jumps[i] + 1
                    if matriz[jumps_next -1] == 1:
                        if jumps[jumps_next] == -1 or jumps[jumps_next] > jumps[i] + 1:
                            jumps[jumps_next] = jumps[i] +1
    return -1
    
#Example solution
result = [0,0,0,1,1,0,1,0,0,0,0]
print(solution(result))

