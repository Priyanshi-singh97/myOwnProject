def lcm(num1,num2):
    if num1>num2:
        greatre_num=num1
    else:
        greatre_num=num2

    while(True):
            if ((greatre_num%num1==0) and (greatre_num%num2==0)):
                lcm=greatre_num
                #break
                greatre_num+=1
                print("LCM of", num1, "and", num2, "=", greatre_num)  
if __name__=='__main__':
    #input=5,20
    print("lcm is:", lcm(5,20))
