import datetime
import time
import playsoundm

print("Your alarm clock")
print("Set your time")
user=int(input("Hour: "))
user2=int(input("Minute: "))
user3=input("Set am/ pm: ")

def alarm():
    global user

    while (True):
        if user3=="pm":
            user=user+12
            while(True):
                if user==datetime.datetime.now().hour and user2==datetime.datetime.now().minute:
                    playsoundm.playsound('Gargling-Water-A5-www.fesliyanstudios.com.mp3')
                    time.sleep(2)
                    break

        else:
            while(True):
                if user == datetime.datetime.now().hour and user2 == datetime.datetime.now().minute:
                    a=playsoundm.playsound('Gargling-Water-A5-www.fesliyanstudios.com.mp3')
                    stop=int(input("1"))
                    print("stop",a)
                    time.sleep(2)
                    if stop==1:
                        break
                else:
                    continue

                    # print("Do you want to stop")
                    break



alarm()



