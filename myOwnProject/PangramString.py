import string

def pang(str):

    pg_str="abcdefghijklmnopqrstuvwxyz"
    for i in pg_str:
         if i not in str.lower():
             return False
    return True

stringNw="the quick brown fox jumps over the lazy dog"
if (pang(stringNw))==True:
    print("yes")
else:
    print("no")

