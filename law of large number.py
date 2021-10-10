n,m,k = map(int,input().split())

arr= list(map(int,input().split()))

arr.sort()

sum=0
cnt=0
max_index=n-1

while (1):
    for i in range(k):
        if m == cnt:
            break
        sum+=arr[max_index]
        cnt+=1

    if m == cnt:
        break
    sum+=arr[max_index-1]
    cnt+=1

print(sum)
    
