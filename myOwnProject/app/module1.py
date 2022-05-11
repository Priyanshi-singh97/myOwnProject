from datetime import datetime, timedelta,date
from django.http import JsonResponse
from django.shortcuts import render 
from django import forms
from app import db_connection

#class pizza()



def insert_api(request):
        try:
            #print(request.POST)   {% csrf_token %} 
            #print(request.GET)   
            if (request.method=='GET'):

                return render(request, "if_else.html")
                "you are fool"
           
            if(request.method=='POST'):
                try:
                    value1=request.POST['fname']
                    value2=request.POST['Phone_No']
                    value3=request.POST['ID']

                    db=db_connection.connection()
                    #cursor()-allow to execute statement in given connection or address
                    myconnection= db.cursor()
                    myconnection.execute("insert into Emp_Details(Name,Phone_No,ID) value ('"+value1+"','"+value2+"','"+value3+"');")


                    db.commit()

                    #commit()-allow to save statement what we want execute

                    fetch_data= myconnection.fetchall()
                    #fetchall-allow to fetch data from connection when we want
                    db.close()
                    #close-finaly once this operation is done will close the connection
                    return render(request, "search.html")
                except Exception as fool:
                     pass
                       


        except Exception as fool:
            pass

def search_api(request):
    try:
        if (request.method=="GET"):
            return render(request, "search.html")
        if (request.method=="POST"):
             try:
                 value=request.POST['search']
             except Exception as fool:
                pass
             

             db=db_connection.connection()
             myconnection= db.cursor()
             qry="(select * from Emp_Details where ID=1;)"
             myconnection.execute(qry)

             #myconnection.execute("insert into Emp_Details(ID) value ('"+value+"');")


             db.commit()
             fetch_data= myconnection.fetchall()
             
             db.close()
             return render(request, "search.html")
    except Exception as ex:
        []
