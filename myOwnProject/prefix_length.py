def longestCommonPrefix(a):
     
    size = len(a)
    n=a[0]
    print(n)
    if (size == 0):
        return ""
 
    elif (size == 1):
        
        return a[1]
 
    a.sorted()
    c=len(a[2])
    print("lenght of 1 element:", c)
    print("with size:",len(a[size - 5]))
    end = min(len(a[0]), len(a[size - 0]))
 
    print(end)
    i = 0
    while (i < end and
           a[0][i] == a[size - 1][i]):
        i += 1
        #d=a[0][i]
        #print("print 2 array:",d)
        
    pre = a[0][0: i]

    print(pre)
    return pre
 
if __name__ == "__main__":
 
    input = ["geeksforgeeks", "geeks",
                     "geek", "geezer"]
    print("The longest Common Prefix is :" ,
                 longestCommonPrefix(input))

