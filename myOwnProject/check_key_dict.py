def checkKey(dict, key):
    dict = {'a': 100, 'b':200, 'c':300}
    try:
            if key in dict:
                print("Present, ", end =" ")
                print("value =", dict[key])
            else:
                print("Not present")
    except Exception as df:
        []
key = 'b'
checkKey(dict, key)