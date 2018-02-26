from datetime import datetime as dt
import time
host_temp = 'hosts'
# host_path = r"/private/etc/hosts"
host_path = 'hosts'
redirect = '121.0.0.1'
websites = ['www.facebook.com', 'facebook.com', 'google.com','www.google.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 19):
        #  Above will be in the format such as (2017,11,31,8 < 2017,11,31,? < 2017,11,31,21)
        print("working hours")
        with open(host_path, 'r+') as file:
            content = file.read()
            for list in websites:
                if list in content:
                    pass
                else:
                    file.write(redirect+" "+list+'\n')
    else:
        print("free time")
        with open(host_path, 'r+') as file:
            content = file.readlines()             # Convert each lines from the file into each list elements
            file.seek(0)                           # This puts the cursor to the first line of the file
            for line in content:
                if not any(site in line for site in websites):  # Print the line by checking the website doesnt exists
                    file.write(line)
            file.truncate()                        # Finally delete the old contents from the last line
    time.sleep(5)                                  # Looping every 5 secs



