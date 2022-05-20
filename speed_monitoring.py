import os
try:
  import speedtest
except ImportError:
  print("Trying to Install required module: speedtest")
  os.system('python -m pip install speedtest-cli')


import speedtest
import datetime
import csv
import os

counter = 0
s = speedtest.Speedtest()
while True:    
    if counter % 10 == 0:     
        with open('speed.csv', 'a', encoding="UTF8", newline='') as speedcsv:        
            csv_writer = csv.writer(speedcsv)        
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            downspeed = round((round(s.download()) / 1048576), 2)
            upspeed = round((round(s.upload()) / 1048576), 2)
            csv_writer.writerow([time_now, downspeed, upspeed])
            speedcsv.close()            
    else:
        response = os.system("ping 1.1.1.1")        
        with open('ping.csv','a', encoding="UTF8", newline='') as pingcsv:
            csv_writer = csv.writer(pingcsv)
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            csv_writer.writerow([time_now, response])
            pingcsv.close()
    counter += 1