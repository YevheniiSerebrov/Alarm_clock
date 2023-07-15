from asyncio import mixins
from tkinter.ttk import *
from tkinter import *

from datetime import datetime
from time import sleep
from pygame import mixer

#window
window = Tk()
window.title("")
window.geometry('350x150')

def sound_alarm():
    mixer.music.load('song_alarm.mp3')
    mixer.music.play()

def alarm():
    while True:
        control = 1
        alarm_hour='05'
        alarm_minute = '07'
        alarm_second='30'
        alarm_period = 'PM'.upper()

        now = datetime.now()
        
        hour = now.strftime('%I')
        minute = now.strftime('%M')
        second = now.strftime('%S')
        period = now.strftime('%p')

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_second == second:
                            print("Time to take a break!")
                            sound_alarm()
        
        sleep(1)

# print((datetime.now()))
mixer.init()
# sound_alarm()
alarm()
# window.mainloop()

