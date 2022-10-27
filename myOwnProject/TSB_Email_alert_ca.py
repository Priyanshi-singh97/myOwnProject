import pymysql
import pandas as pd
import os
import sys
import shutil
import xlsxwriter
import datetime
import schedule
import time
from datetime import date, timedelta
from operator import itemgetter
import boto3
from botocore.exceptions import ClientError
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from dateutil.relativedelta import relativedelta


def get_rp_reportserver_connection( env=None):
    try:
        env='SIT'
        
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
        elif(env == "SIT"):
            dbname = 'centria_dump'
            user = 'tsbdbuser'
            password = 'tstartbdbUsER#2022'
            host = 'tsb-db-sit.mysql.database.azure.com'
            port = 3306
            connection = pymysql.connect(host=host, database=dbname, user=user,
                                         password=password, port=port, cursorclass=pymysql.cursors.DictCursor)
            return connection

    except Exception as ex:
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
        
        RECIPIENT = "priyanshee.s@techtreeit.com"

        CC_RECIPIENT = ",".join(["shalu.gupta@techtreeit.com"])
        aws_RECIPIENT = ["shalu.gupta@techtreeit.com"]
    else:
        SENDER = "clubapparel@techtreeit.in"
        RECIPIENT = "priyanshee.s@techtreeit.com"

        CC_RECIPIENT = ",".join(["shalu.gupta@techtreeit.com"])
        aws_RECIPIENT = ["shalu.gupta@techtreeit.com"]
        

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

    except ClientError as esdf:
            print('Fail')


def get_AlertDate_and_email():
        print("test") 
        t = datetime.datetime.now()
        Today_date=t.strftime('%d-%m-%Y')
        yesterday = date.today() - timedelta(days=1)
        yesterday_date=yesterday.strftime('%d-%m-%Y')
        _subject='TSB Incremental ADF refreshed success : '+str(Today_date)+''
        report = get_sqldata_query("select * from rp_scheduled_procedure_call_log where DATE(CREATION_TIME) = DATE(NOW());") 
        report = get_sqldata_query("select * from rp_scheduled_procedure_call_log where DATE(CREATION_TIME) = DATE(NOW());") 
        
     
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
            
            if (failUre_status ==True):
                _content = 'Hi Team Db refresh completed successfully, please find the below table for status of each scheduled stored procedures.'
              
                sendMail(send_to='', subject=_subject, Content=_content, data=report,tn_count=len(report))
                print(report)
            else:
                _subject2='TSB Incremental ADF refreshed failed : '+str(Today_date)+''
                _content2 = 'Hi Team Db refresh failed, please check the scheduled stored procedure.<br/> Success Count:'+str(Success_count)+' <br/> Failure Count: '+str(Failure_count)+'.'
                sendMail(send_to='', subject=_subject2, Content=_content2,data=report,tn_count=len(report))
        else:
            print('no data')
            

#schedule.every().day.at("07:30").do(get_AlertDate_and_email)
get_AlertDate_and_email()

#while True:
#    schedule.run_pending()
#    time.sleep(1)


