from datetime import datetime

alarm = input("Please set your alarm like - HH:MM:SS: ")

alarmHour = alarm[0:2]
alarmMinutes = alarm[3:5]
alarmSeconds = alarm[6:8]
alarmPeriod = alarm[9:11].upper()

print("Setting alarm...")

while True:
    now = datetime.now()
    currentHour = now.strftime("%I")
    currentMinutes = now.strftime("%M")
    currentSeconds = now.strftime("%S")
    currentPeriod = now.strftime("%p")
    if(alarmPeriod == currentPeriod):
        if(alarmHour == currentHour):
            if(alarmMinutes == currentMinutes):
                if(alarmSeconds == currentSeconds):
                    print("Dryń dryń")
                    break