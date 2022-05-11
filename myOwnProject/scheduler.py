import schedule 
try:
   
   def job():
        print("Hi priya u r so beutiful")
        #run the function job() every 2 seconds  
   schedule.every(2).seconds.do(job)  
   while True:  
          schedule.run_pending()  
except Exception as eg:
    pass








