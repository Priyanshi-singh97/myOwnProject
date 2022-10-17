#num = [1, 7, 4, 3, 4, 8, 7]
def vb(num,n):
    for i in num:
        count=0
        for j in num:
            if i==j:
                print(i)
                count+=1
        if count==n:
            return i
    return -1


if __name__=="__main__":
    num = [1, 7, 4, 3, 4, 8, 7];
    n = 2
    print(vb(num, n))




