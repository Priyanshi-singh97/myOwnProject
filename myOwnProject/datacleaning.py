mydict = { "short bread": "bread", 
           "black bread": "bread", 
           "banana cake": "cake", 
           "wheat bread": "bread" }

mystring = "wheat breads breakfast today"
try:
    for key in mydict:
        if key in mystring:
         print(mydict[key])
except Exception as gf:
    pass

