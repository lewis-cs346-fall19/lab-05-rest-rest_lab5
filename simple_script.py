#! /usr/bin/python3
import os
import json
import cgi
import cgitb
import MySQLdb
if "PATH_INFO" in os.environ:
    pathinfo = os.environ["PATH_INFO"]
    if pathinfo == "/jsontest":
        print("Content-type: application/json")
        print("Status: 200 OK")
        print()
        randomObject = [4, 17, None, {"a" : 0, "b" : 1, "c" : 2}, "Halloween", 33, "school"]
        randomObject_json = json.dumps(randomObject, indent = 2)
        print(randomObject_json)
    else:
        print("Content-Type: text/html")
        print("Status: 200 OK")
        print()
        if pathinfo == "/form":
            print('This is a form' )
            form=cgi.FieldStorage()
            sql_variable=form.getvalue("dog")
            db = MySQLdb.connect('lab4.cixhqu4w47kx.us-east-1.rds.amazonaws.com', 'masteruser', 'Madeuppassword', 'dogs')
            cursor=db.cursor()
            sql = "INSERT INTO dogs (name) VALUES ("+"'"+sql_variable+"'"+")"
            cursor.execute(sql)
            db.commit()
            db.close()
            new_id = cursor.lastrowid
            cursor.close()
            print(sql_variable)
        else:
            print("This is the default page")
            print("<br>")
            print("Your PATH_INFO is " + pathinfo)
else:
    print("Status: 302 Redirect")
    print("Location: simple_script.py/")
    print()