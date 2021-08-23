a,b,c,x,y=(int(i) for i in input().split())
if(a+b+c) !=(x+y):
    print("NO")
elif x<min(a,b,c) or y<min(a,b,c):
    print("NO")
else:
    print("YES")