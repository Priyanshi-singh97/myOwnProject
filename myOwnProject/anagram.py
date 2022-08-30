wk = {"act","god","cat","dog","tac"}
df=[]
df1=[]
for i in wk:
    df.append(i)
print(df)

for e in range(len(df)):
    e6=df[e]
    print(e6)
    e1=" ".join(e6)
    print(e1)
    e2=e1.split(" ")
    c=list(df[e])
    if e1 in c:
        print(e1)
   