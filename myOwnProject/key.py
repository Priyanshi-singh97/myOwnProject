#import pandas as pd
#x = []
#for n in range(4):
#    q = []
#    x.append(q)
#    #other stuff
#    for t in range(10):
#        #other stuff
#        q.append(t)

#from pprint import pprint       
##pprint(x)
#x1=x
#x2=x1[0]
##t1=pd.DataFrame(x2)
#ai="_".join(t1)
#print(ai)
#x3=x1[0]
#x4=x1[0]
#x5=x1[0]
#pprint(x1)


def calculateSq():
    try:
        n = 'a'
        
        
        result = map( calculateSq, n)
        print(result)
        return n*n
    except Exception as gh:
        print(gh)
calculateSq()