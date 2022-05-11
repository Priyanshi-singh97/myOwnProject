
def shout(text):
    return text.upper()
 
def whisper(text):
    return text.lower()
 
def greet(func):
    # storing the function in a variable
    try:
        greeting = func("Hi, I am created by a function passed as an argument.")
        print (greeting)
    except Exception as df:
        pass
    
   
 
greet(shout)
greet(whisper)