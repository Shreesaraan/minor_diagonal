def minor_diagonal(rows,matrix):
    sum=0
    change=rows-1
    for i in range(rows):
        sum+=matrix[i][change]
        change-=1
    return sum
    

matrix=[]
rows=int(input("Number of Rows : "))
for i in range(rows):
    matrix.append(list(map(int,input().split())))
print(minor_diagonal(rows,matrix))