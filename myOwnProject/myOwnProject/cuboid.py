try:
    #x = int(raw_input())
    #y = int(raw_input())
    #z = int(raw_input())
    #n = int(raw_input())
    x = 1
    y = 1
    z = 1
    n = 2
    output=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k==n:
                    continue
                else:
                    output.append([i,j,k])
    
    print(output)
except Exception as dg:
    pass
