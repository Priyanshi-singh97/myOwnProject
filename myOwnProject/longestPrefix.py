a="aabacbebebe"
b=list(a)

for i in range(len(b)):
    j=b[i]
    k=b[i+1]
    if j and k in b:
        print(j,k)
    