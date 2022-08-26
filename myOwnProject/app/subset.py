import itertools
xs = ['a', 'b', 'c']
#xs = [1, 2, 3]
try:
    for i in range(0, len(xs) + 1):  # to get all lengths: 0 to 3
        for subset in itertools.combinations(xs, i):
            print(list(subset))
except Exception as df:
    print(df)
