N= int(input("Give the length of list: "))
max=0
list1=list(map(int,input().split()))
for i in range(N):
    count=1
    for j in range(i+1,N):
        if list1[i]== list1[j] :
            count+=1
        j+=1
    if max<count:
        max=count
        Dishtype=list1[i]
    i+=1 
print(Dishtype)