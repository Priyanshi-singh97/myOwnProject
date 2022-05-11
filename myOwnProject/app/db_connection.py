import pymysql


class db_connect():
    def connection():

        host='127.0.0.1'
     
        user='Priyanshi'
        password='12345'
        dbname='priya'
   
        port=3306
        connection=pymysql.connect(host=host,user=user,password=password,database=dbname,port=port,cursorclass=pymysql.cursors.DictCursor)
        return connection
