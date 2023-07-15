from cProfile import label
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from asyncio import mixins
from datetime import datetime
from time import sleep
from pygame import mixer
from threading import Thread


#window
window = Tk()
window.title("")
window.geometry('350x150')
window.configure(bg="white")

#frames
frame_line = Frame(window,width=400, height=5, bg='#566FC6')
frame_line.grid(row=0, column=0)

frame_body = Frame(window,width=400, height=290, bg='white')
frame_body.grid(row=1, column=0)

#conf frame body
img = Image.open('ic02.png')
# new_im = img.resize((80,80))
# new_im.save('ic02.png')
# im2 = Image.open('ic02.png')
img = ImageTk.PhotoImage(img)
# print(img.__sizeof__())
app_image = Label(frame_body, height=100, image=img, bg="white")
app_image.place(x=10, y =10)

name = Label(frame_body, text ='Alarm', height=1, font=('Ivy 18 bold'), bg='white')
name.place(x=107, y =10)

hour = Label(frame_body, text ='hour', height=1, font=('Ivy 10 bold'), bg='white', fg='blue')
hour.place(x=107, y =40)
c_hour =Combobox(frame_body, width=2, font=('arial 15'))
c_hour['values']=["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
c_hour.current(0)
c_hour.place(x=110, y = 58)

minute = Label(frame_body, text ='mins', height=1, font=('Ivy 10 bold'), bg='white', fg='blue')
minute.place(x=157, y =40)
c_minute =Combobox(frame_body, width=2, font=('arial 15'))
c_minute['values']=["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
 "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32","33","34","35",
 "36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
c_minute.current(0)
c_minute.place(x=160, y = 58)

sec = Label(frame_body, text ='secs', height=1, font=('Ivy 10 bold'), bg='white', fg='blue')
sec.place(x=207, y =40)
c_sec =Combobox(frame_body, width=2, font=('arial 15'))
c_sec['values']=["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
 "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32","33","34","35",
 "36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
c_sec.current(0)
c_sec.place(x=210, y = 58)

period = Label(frame_body, text ='per', height=1, font=('Ivy 10 bold'), bg='white', fg='blue')
period.place(x=257, y =40)
c_period =Combobox(frame_body, width=3, font=('arial 15'))
c_period['values']=('AM', 'PM')
c_period.current(0)
c_period.place(x=260, y = 58)

def activate_alarm():
    t=Thread(target=alarm)
    t.start()

def deactivate_alarm():
    print('Deactivated alarm: ', selected.get())
    mixer.music.stop()

selected = IntVar()

rad1= Radiobutton(frame_body, font = ('arial 10 bold'), value = 1, text='Activate', bg='white', command=activate_alarm, variable=selected)
rad1.place(x=125, y=95)


def sound_alarm():
    mixer.music.load('song_alarm.mp3')
    mixer.music.play()
    selected.set(0)

    rad2= Radiobutton(frame_body, font = ('arial 10 bold'), value = 2, text='Dectivate', bg='white', command=deactivate_alarm, variable=selected)
    rad2.place(x=187, y=95)

def alarm():
    while True:
        control = 1
        alarm_hour=c_hour.get()
        alarm_minute = c_minute.get()
        alarm_second=c_sec.get()
        alarm_period = c_period.get()
        alarm_period=str(alarm_period).upper()
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
mixer.init()

window.mainloop()