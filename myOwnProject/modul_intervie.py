
a="""This is a test application for the interview. This test a sample python"""
 
b=a.split(" ")
print(b)
try:
    for i in b:
        for j in b:
            if i==j:
                print(i)
except Exception as df:
    []