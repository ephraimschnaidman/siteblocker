import time
from datetime import datetime as dt


hosts_temp="hosts_test_file" # test the program is working on the dummie file
hosts_path_unix="/etc/hosts"   #  root file in MAC/Linux operating systems.
#hosts_path_W="C:\Windows\System32\drivers\etc\hosts" # use this for Windows operating systems
redirect="127.0.0.1"
website_list=["wikipedia.org"," www.wikipedia.org"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print('Working hours...')
        with open(hosts_path_unix,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+ '\n')
    else:
        with open(hosts_path_unix,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("Non-working hours...")
    time.sleep(5)
