try:
    print("how many number you want to add")
    num = int(input('plz enter your number:'))
   
    num3=[]
    for i in range(num):

        if i<=num:

            num3.append(i)
        else:
            print('plz enter small number ')
except Exception as df:
    []