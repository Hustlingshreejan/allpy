import datetime
import  playsoundm

# mybirthdate=datetime.datetime(1999,2,25,19,30,12)
# print(mybirthdate)
# print(mybirthdate.strftime("%A, %B %d, %Y, %H:%M:%S"))
# print(mybirthdate.month)
# print(datetime.date.today())
# print(datetime.time())
# d=datetime.datetime.timestamp()
# print(d)

# print("In how much of interval of time do you want to get notification? ")




# timelist=(9,10,11,12,13,14,15,16,17,18)
# for hours in timelist:
#     if hours%2!=0:
#         print(hours)

def alarm():
    timelist = (9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
    for hours in timelist:
        if hours % 2 != 0:
            if hours == datetime.datetime.now().hour:
                playsoundm.playsound('Gargling-Water-A5-www.fesliyanstudios.com.mp3')
        else:
            continue

alarm()






