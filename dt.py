import datetime
now = datetime.datetime.now()
print ("current date : ")
print (now.strftime("%d-%m-%y"))
print ("current time : ")
print (now.strftime("%H:%M:%S"))