def matrixmul(a:list[list[int|float]],b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    c=[]
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            row.append(sum(
                a[i][k]*b[k][j] 
                for k in range(len(a[0]))
            ))
        c.append(row)
    return c