#class validate_pass(object):
#    def kftn(self,password):
#            #self.password=password
#            c=['$','@','#','%']
#            if len(password)<6:
#                pass
            
#            for i in password:
#                if i.isupper():
#                    pass
#                elif i.islower():
#                    pass
#                elif i.isdigit ():
#                    pass
#                elif i in c:
#                    pass
#                else:
#                    print("add special char")
                
#if __name__ == '__main__':
#    obj=validate_pass()
#    print(obj.kftn("priya"))
    

try:
    n=int(input())
    a=map(int,input().split())
    m=min(a)
    print(-1,[2*sum(a)])
except Exception as e:
    print(e)
