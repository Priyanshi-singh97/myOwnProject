import json
import pytz
from datetime import datetime, timedelta, date,timezone
import datetime
import schedule
import time
import requests 
 
from Extra_Methods import DateRange
from Firebase_Events import Firebase_Events
 

 

import smtplib
from email.mime.text import MIMEText as text
Event_list=['Campaign_Notification_Click_through','BannerClickThrough','Banner_Click_through','notification_clicked','splash_open','app_open']

 
#date_from = datetime.datetime.strptime('2020-07-10'   , '%Y-%m-%d').date()
date_from = datetime.datetime.strptime(str(((datetime.date.today()) - datetime.timedelta(days = 1)).strftime('%Y-%m-%d')),"%Y-%m-%d").date()  

current_date = datetime.datetime.strptime(str(((datetime.date.today()) - datetime.timedelta(days = 1)).strftime('%Y-%m-%d')),"%Y-%m-%d").date()  
getDates = DateRange.GetDateRange_Ascending (date_from, current_date)




def StartMail(time): 
    try:
 
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login("dlptest@techtreeit.com", "TechTree@123")
        m = text("CA app analitics data download started on " + time + "")
        #recipients = ['anbalaghan.r@techtreeit.com', 'saurabh.vashistha@techtreeit.com','neeraj.shukla@techtreeit.com']
        recipients = ['anbalaghan.r@techtreeit.com','arivazhagan.r@techtreeit.com']
        m['Subject'] = ' CA BigQuery Daily Data Import JOB: BigQuery Download Started at ' + time;
        m['From'] = 'dlptest@techtreeit.com'
        m['To'] = ", ".join(recipients)
 
 
        server.sendmail("dlptest@techtreeit.com", recipients,m.as_string())
    except :
        pass 

def EndMail(time): 
    try:
 
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login("dlptest@techtreeit.com", "TechTree@123")
        m = text("CA app analitics data download ended on " + time + "")
        #recipients = ['anbalaghan.r@techtreeit.com', 'saurabh.vashistha@techtreeit.com','neeraj.shukla@techtreeit.com']
        recipients = ['anbalaghan.r@techtreeit.com','arivazhagan.r@techtreeit.com']
        m['Subject'] = 'CA BigQuery Daily Data Import JOB: BigQuery Download Ended at ' + time;
        m['From'] = 'dlptest@techtreeit.com'
        m['To'] = ", ".join(recipients)
 
 
        server.sendmail("dlptest@techtreeit.com", recipients,m.as_string())
    except :
        pass 


def ExceptionMail(time, Exception): 
    try:
 
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login("dlptest@techtreeit.com", "TechTree@123")
        m = text("BigQuery Daily Data Import Is Exception occurred at " + time + "" + "\n" + Exception)
        #recipients = ['anbalaghan.r@techtreeit.com', 'saurabh.vashistha@techtreeit.com','devops.blr@techtreeit.com']
        recipients = ['anbalaghan.r@techtreeit.com']
        m['Subject'] = 'CA BigQuery Daily Data Import JOB: Error at ' + time;
        m['From'] = 'dlptest@techtreeit.com'
        m['To'] = ", ".join(recipients)
 
 
        server.sendmail("dlptest@techtreeit.com", recipients,m.as_string())
    except :
        pass

 
def StartImportFromFirebase():
 #date_from = datetime.datetime.strptime('2021-12-15'   , '%Y-%m-%d').date()
 date_from = datetime.datetime.strptime(str(((datetime.date.today()) - datetime.timedelta(days = 1)).strftime('%Y-%m-%d')),"%Y-%m-%d").date()  
 


 current_date = datetime.datetime.strptime(str(((datetime.date.today()) - datetime.timedelta(days = 1)).strftime('%Y-%m-%d')),"%Y-%m-%d").date()  
 getDates = DateRange.GetDateRange_Ascending (date_from, current_date)
 for dt in getDates:  

    datefor = dt.strftime("%Y%m%d")
    print(datefor)    
    try:
        #StartMail(str((datetime.datetime.now()).strftime("%d-%b-%Y %H:%M:%S.%f")))
        for event_name in Event_list:
   
            
            Firebase_Events().StartImport(datefor,event_name)
        #EndMail(str((datetime.datetime.now()).strftime("%d-%b-%Y %H:%M:%S.%f")))
    except Exception as Error:
          test=""
        #ExceptionMail(str((datetime.date.today()).strftime("%d-%b-%Y %H:%M:%S.%f")), Error)
StartImportFromFirebase()    

#schedule.every().days.at("09:57").do(StartImportFromFirebase) 
#while True:
#    #print("Tik")
#    schedule.run_pending()
#    time.sleep(1)   
  
