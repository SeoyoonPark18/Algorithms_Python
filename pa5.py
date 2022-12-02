#Seoyoon Park

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    ans=[]

    m = len(matrix)
    n = len(matrix[0])
    k=0
    l=0
    total = m*n
    cnt=0

    while(k<m and l<n):
        if(cnt == total): break
        for i in range(m-1,k-1,-1):
            ans.append(matrix[i][n-1])
            cnt+=1
        n-=1

        if(cnt == total): break
        for i in range(n-1,l-1,-1):
            ans.append(matrix[k][i])
            cnt+=1
        k+=1

        if(cnt == total): break
        for i in range(k,m):
            ans.append(matrix[i][l])
            cnt+=1
        l+=1

        if(cnt == total): break
        for i in range(l,n):
            ans.append(matrix[m-1][i])
            cnt+=1
        m-=1

    return ans
 
