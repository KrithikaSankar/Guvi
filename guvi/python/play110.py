n=int(input())
k=input().strip()
a=k.split(" ")
ans=""
p=0
for x in a:
    p+=int(x)
for x in a:
    ans+=str(p+int(x))+" "
print(ans.strip())
