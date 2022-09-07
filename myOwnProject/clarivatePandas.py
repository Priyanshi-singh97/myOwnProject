import pandas as pd
def df1():

    try:
        work={'Flower': 1, 'Fruit': 23, 'Age': 20,'Age1':     20,
          'Age2': 20,

          'Flower1': 'Rose1',
          
          
          
          }

        work1=pd.DataFrame(work)
        print(work1)
    except Exception as df:
        pass

df1()