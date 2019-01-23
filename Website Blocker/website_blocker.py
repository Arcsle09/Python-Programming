# -*- coding: utf-8 -*-
import time

from datetime import datetime as dt  

#host_temp = r"C:\Users\RAKESH\Desktop\Python Programming\Website Blocker\hosts"

host_path =r"C:\Windows\System32\drivers\etc\hosts"

#host_path ="C:\\Windows\\System32\\drivers\\etc\\hosts"

redirect = "127.0.0.1"

website_list = ["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,10):
        print("Working Hours..")
        with open(host_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + " " + website + "\n")
    else:
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("Fun Hours...")
    time.sleep(3)

