def missing(a):
    #a=list(set(k))
    a.sort()
    
    b=[]
    
    l=a[0]
    v=a[-1]
    #print(l)
    for i in range(l,v):
            b.append(i)
            if i in a:
                pass
            else:
                print("missing:",i)
    print(b)


if __name__=="__main__":
    input=[1,2,2,4,6,8,7]
    print("missing no is:",missing(input))
        
        