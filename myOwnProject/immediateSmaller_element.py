N = 5
Arr = [4, 2, 1, 5, 3]
def sm_fun(N,Arr):

    Arr1 = []
    N = 5
    Arr = [4, 2, 1, 5, 3]
    
    for i in range(len(Arr)):
       print(Arr[i],Arr[i+1])
       if Arr[i]<Arr[i+1]:
           Arr1.append(-1)
       elif Arr[i]>Arr[i+1]:
            Arr1.append(Arr[i+1])
    print(Arr1)
sm_fun(N,Arr)