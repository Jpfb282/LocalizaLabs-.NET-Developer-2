def sum_binary(A,B):
    carry = 0
    C = [0 for j in range(0,len(A)+1)]
    for i in range(len(A)-1,-1,-1):
	    C[i+1] = (A[i]+B[i]+carry)%2
	    if (A[i]+B[i]+carry)>=2:
		    carry = 1
	    else:
		    carry = 0
    C[0] = carry
    return C


A=[1,0,0,1]
B=[0,1,1,0]
print(sum_binary(A,B))

A=[1,1,1,1]
B=[1,1,0,1]
print(sum_binary(A,B))
