def simple():
    try:
        for i in range(10):
            if (i%2==0):
                yield i
    except Exception as df:
        []
for i in simple():
    print(i)
