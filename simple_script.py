#! /usr/bin/python3
import os
import json
if "PATH_INFO" in os.environ:
    pathinfo = os.environ["PATH_INFO"]
    if pathinfo == "/jsontest":
        print("Content-Type: application/json")
        print("Status: 200 OK")
        print()
        randomObject = [4, 17, None, {"a" : 0, "b" : 1, "c" : 2}, "Halloween", 33, "school"]
        randomObject_json = json.dumps(randomObject, indent = 2)
        print(randomObject_json)
    else:
        print("Content-Type: text/html")
        print("Status: 200 OK")
        print()
        if pathinfo == "/correct":
            print("Welcome to the secret page")
        else:
            print("This is the default page")
            print("<br>")
            print("Your PATH_INFO is " + pathinfo)
else:
    print("Status: 302 Redirect")
    print("Location: simple_script.py/")
    print()
