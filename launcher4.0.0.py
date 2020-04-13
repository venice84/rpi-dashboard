from tkinter import * #Tkinter for python 2x
import time # reads the time
import locale # time conversion
import logging # for logging
import threading # multi processes
from threading import Thread
import subprocess
from uptime import *
import paho.mqtt.client as mqtt

#start window
root = Tk() #call root window

#initialise var
up=''
time1=''

#log error
#logging.basicConfig(filename='launcher.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
#logger=logging.getLogger(__name__)

##chiudi = PhotoImage(file="chiudi.png") #PER METTERE IMMAGINE
chiudi ='CHIUDI'

#def window and locales
locale.setlocale(locale.LC_ALL, '') # translation months in correct utc format

#-------------------------TESTING WINDOW PARAMETERS----------------------------
#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("450x400+300+300")
#root.geometry('%sx%s' % (w, h))
#root.attributes("-fullscreen", True)  #fullscreen
#---------------------------------------------------------------------------

root.bind('<Escape>',lambda e: root.destroy()) # destroy main window with esc
root.configure(background='black') # black wallpaper
root.config(cursor="none") # no mouse pointer

################ MAIN WINDOW LEVEL ################


label_clock = Label(root, font=('DejaVu Sans', 100, 'bold'), fg='white',bg='black')
label_clock.grid(row=0, columnspan=3)

label_date = Label(root, font=('DejaVu Sans', 25), fg='white',bg='black')
label_date.grid(row=1,columnspan=3)

button_chiudi = Button(root, font=('DejaVu Sans', 8), borderwidth=1, fg='white',bg='black',relief="solid", text='v. 4.0 exit', command = root.destroy)
button_chiudi.grid(row=2,columnspan=3)

label_info0 = Label(root, font=('DejaVu Sans', 30), fg='white',bg='black', borderwidth=1, relief="solid", text="cpu")
label_info0.grid(row=3, column=0)

label_info1 = Label(root, font=('DejaVu Sans', 30), fg='white',bg='black', borderwidth=1, relief="solid", text="uptime")
label_info1.grid(row=3,column=1)

label_info2= Label(root, font=('DejaVu Sans', 30), fg='white',bg='black', borderwidth=1, relief="solid", text="disk")
label_info2.grid(row=4, column=0)

label_info3 = Label(root, font=('DejaVu Sans', 30), fg='white',bg='black', borderwidth=1, relief="solid", text="domani")
label_info3.grid(row=4,column=1)

#MQTT UPDATE CPU per visualizzare i messaggi mqtt 
def on_message_raspcpu(client, userdata, message):
    cpu='freq '+str(message.payload.decode("utf-8")+'%')
    label_info0.config(text=cpu)

#MQTT UPDATE DISK USAGE per visualizzare i messaggi mqtt
def on_message_disco_occ(client, userdata, message):
    disk='disk '+str(message.payload.decode("utf-8"))
    label_info2.config(text=disk)

#MQTT RAM USAGE per visualizzare i messaggi mqtt
def on_message_ram_occ(client, userdata, message):
    ram='ram '+str(message.payload.decode("utf-8")+'%')
    label_info3.config(text=ram)
    
#MQTT DEFAULT definizioni iniziali per connettersi
broker_address="192.168.x.x"
user = "user"
password = "password"
client = mqtt.Client("Python") #create new instance
client.username_pw_set(user, password=password)

#MQTT DEFINE TOPICS ogni lettura va in un callback differente in base al topic (anche se ascolto tutto)
client.message_callback_add('raspcpu', on_message_raspcpu)
client.message_callback_add('disco_occ', on_message_disco_occ)
client.message_callback_add('ram_occ', on_message_ram_occ)
client.connect(broker_address) #connect to broker per far comparire i messaggi
client.loop_start()

#ascolto tutto - posso anche filtrare solo una sotto categoria
client.subscribe("#")

##########processo numero 2 - aggiorna l'uptime##########
def update_uptime():
    up='   upt '+str(round(uptime()/86400,2))+'gg'
    label_info1.config(text=up)
    #print(time.strftime('%S')) #x check
    root.after(6000, update_uptime) #crea il loop


##########processo numero 1 - aggiorna l'orario##########
def update_time():
    global time1
    ora_ora = time.strftime('%H:%M')
    data_ora = time.strftime('%d %B %Y', time.localtime())
    
    label_clock.config(text=ora_ora)
    label_date.config(text=data_ora)
    #print(time.strftime('%S')) #x check
    root.after(6000, update_time) #crea il loop


#multiprocessing
if __name__ == '__main__':
    T1=Thread(target = update_time)
    T2=Thread(target = update_uptime)
    T1.setDaemon(True)
    T2.setDaemon(True)
    T1.start()
    T2.start()
root.mainloop()
