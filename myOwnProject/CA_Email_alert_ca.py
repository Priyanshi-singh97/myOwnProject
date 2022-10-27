
import pymysql
import pandas as pd
import os
import sys
import shutil
import xlsxwriter
import datetime
import schedule
import time
import logging
from datetime import date, timedelta
from operator import itemgetter
import boto3
from botocore.exceptions import ClientError
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from dateutil.relativedelta import relativedelta

logging.basicConfig(filename='CA_Email_alert_ca-log.log', 
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s-%(message)s')

def get_rp_reportserver_connection( env=None):
    try:
        env='Prod'
        logging.info('DB Connected')
        if(env == "Prod"):
            dbname = 'cadb'
            user = 'datainsights'
            password = 'Data$9751'
            host = 'localhost'
            #host = '15.207.8.100'
            port = 3306
            connection = pymysql.connect(host=host, database=dbname, user=user,
                                         password=password, port=port, cursorclass=pymysql.cursors.DictCursor)
            return connection
        elif(env == "UAT"):
            dbname = 'cadb'
            user = 'datainsights'
            password = 'Data$9751'
            host = 'localhost'
            port = 3306
            connection = pymysql.connect(host=host, database=dbname, user=user,
                                         password=password, port=port, cursorclass=pymysql.cursors.DictCursor)
            return connection

    except Exception as ex:
        logging.info('DB Connection Failed')
        return False

    
def get_sqldata_proc(procedure_name, *args, env=None):
    connection = get_rp_reportserver_connection(env)
    cusror = connection.cursor()
    cusror.callproc(procname=procedure_name, args=args)
    rows = cusror.fetchall()
    connection.close()

    return rows

def get_sqldata_query(query):
    try:
        connection = get_rp_reportserver_connection()
        cusror = connection.cursor()
        cusror.execute(query)
        rows = cusror.fetchall()
        connection.close()
        return rows
    except Exception as ex:
        connection.rollback()
        connection.close()



def sendMail(send_to=None,  subject=None, Content=None, data=None,tn_count=0, env=None):
    env="Prod"
    if(env == "Prod"):
        SENDER = "clubapparel@techtreeit.in"
        
        #SENDER = "loyalty@clubapparel.com"
        #For Production please use: FraudAlert@clubapparel.com
        RECIPIENT = "casupport@techtreeit.com"
        
        
        CC_RECIPIENT = ",".join(["notification.reporting@techtreeit.com"])
        aws_RECIPIENT = ["notification.reporting@techtreeit.com"]
    else:
        SENDER = "clubapparel@techtreeit.in"
        #For UAT please use: FraudAlertUAT@clubapparel.com
        #SENDER = "loyalty@clubapparel.com"
        RECIPIENT = "casupport@techtreeit.com"
        CC_RECIPIENT = ",".join(["notification.reporting@techtreeit.com"])
        aws_RECIPIENT = ["notification.reporting@techtreeit.com"]
        

    AWS_REGION = "us-east-1"
    CHARSET = "utf-8"
    SUBJECT = subject
    BODY_HTML= Content 
    if type(data)==list:
        try:
            df = pd.DataFrame(data)    #BODY_HTML = pdtable.to_html()
            BODY_HTML= Content + '<br/><br/>' + df.to_html(index=False)
        except Exception as Er :
            print(str(Er))
    
    msg = MIMEMultipart('mixed')
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER
    msg['To'] = RECIPIENT
    msg['CC'] = CC_RECIPIENT

    msg_body = MIMEMultipart('alternative')
    htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)
    msg_body.attach(htmlpart)       
    msg.attach(msg_body)

    client = boto3.client('ses', region_name=AWS_REGION,
                          aws_access_key_id='AKIAJWZCT2OHQCD3FP2A',
                          aws_secret_access_key='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'
                          )

    try:
            response = client.send_raw_email(
                Source=SENDER,
                Destinations=aws_RECIPIENT,
                RawMessage={
                    'Data': msg.as_string()
                }
            )
            if 'ErrorResponse' in response:
                print('Fail')
            print('Sent')
            logging.info('Email Sent')

    except ClientError as esdf:
            print('Fail')
            logging.info('Email Not Sent')


def get_AlertDate_and_email():
        print("test") 
        t = datetime.datetime.now()
        Today_date=t.strftime('%d-%m-%Y')
        _subject='CA Incremental db refreshed success : '+str(Today_date)+''
        report = get_sqldata_query("select * from cadb.rp_incremental_scriptr_call_log where DATE(CREATION_TIME) = date(now());") 
        report2 = get_sqldata_query("select STATUS from cadb.rp_incremental_scriptr_call_log where DATE(CREATION_TIME) = date(now()) and STORED_PROCEDURE_NAME='All_incremental_Proc_Run_Script';") 
        try:
            failUre_status2=None
            report2_value_read=report2[0]
            
            if report2_value_read['STATUS']=='SUCCESS':
                failUre_status2=True
                
            else:
             failUre_status2=False
        except Exception as Er:
            print('fail')
        failUre_status=True
        Success_count=0
        Failure_count=0
        for x in report:
           
            if x['STATUS']=='SUCCESS':
                Success_count=Success_count+1
            else:
                Failure_count=Failure_count+1
                failUre_status=False
              
          
        if len(report)>0:
            
            if (failUre_status ==True and failUre_status2==True):
                _content = 'Hi Team Db refresh completed successfully, please find the below table for status of each scheduled stored procedures.'
              
                sendMail(send_to='', subject=_subject, Content=_content, data=report,tn_count=len(report))
                print(report)
                logging.info('DB Refresh Successful')
            else:
                _subject2='CA Incremental db refreshed failed : '+str(Today_date)+''
                _content2 = 'Hi Team Db refresh failed, please check the scheduled stored procedure.<br/> Success Count:'+str(Success_count)+' <br/> Failure Count: '+str(Failure_count)+'.'
                sendMail(send_to='', subject=_subject2, Content=_content2,data=report,tn_count=len(report))
                logging.info('DB Refresh Failed')
        else:
            print('no data')
            

#schedule.every().day.at("07:30").do(get_AlertDate_and_email)
get_AlertDate_and_email()

#while True:
#    schedule.run_pending()
#    time.sleep(1)


