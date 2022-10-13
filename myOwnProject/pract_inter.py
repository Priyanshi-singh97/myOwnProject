from django.shortcuts import render
from rest_framework.views import APIView
import json 
from app import db_connection

class fdj(APIView):
    def post(self,request,format=None):
        try:
            josn_data=json.loads(json.dumps(request,data))
            id=josn_data['id']
            name=josn_data['name']
            conet=db_connection.db_connect.connection()

            myconnection= conet.cursor()
            myconnection.execute("insert into dfg(id,name) value ('"+id+"','"+name  +"');")

            db.commit()
            fetch_data= myconnection.fetchall()
                        #fetchall-allow to fetch data from connection when we want
            db.close()
        except Exception as df:
            pass