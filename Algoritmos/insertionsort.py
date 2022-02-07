A = [5,4,3,2,1]
print(A)

length = len(A)
for j in range(1,length):
    key = A[j]
    i = j - 1
    while (i>-1 and A[i]>key):
	    A[i+1] = A[i]
	    i = i-1
    A[i+1] = key

	
print(A) 
