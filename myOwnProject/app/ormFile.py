from app.db_connection import db_connect
from django.db import models
class Student(models.Model):  
    try:
            username = models.CharField(max_length=20)  
            first_name = models.CharField(max_length=30)  
            last_name = models.CharField(max_length=30)  
            mobile = models.CharField(max_length=10)  
            email = models.EmailField()  
    except Exception as df:
        pass
   
  
    
