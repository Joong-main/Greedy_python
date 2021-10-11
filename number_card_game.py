row,col=map(int,input().split())

d=[]

for i in range(row):
    col_list=list(input().split())
    d.append(col_list)

min_val_list=[]

for i in range(row):
    min_val=int(d[i][0])
    for j in range(col):
        if int(d[i][j])< int(min_val):
            min_val=int(d[i][j])
    min_val_list.append(int(min_val))

min_val_list.sort()

print(min_val_list[-1])
