# SensorApp.py
#!/usr/bin/env python3
import time
from datetime import date
import ast
import numpy
import paho.mqtt.subscribe as subscribe
import json
from datetime import datetime
import tkinter as tk
import pygubu
from multiprocessing import Process, Pipe, Queue
import sys
#from os.path import exists
#from os import linesep
import os
#from queue import Queue
tim=date.today()
fil='out.json'

class SensorApp:
    def __init__(self):
        global par_run
        #global par_mgs
        
        #1: Create a builder
        self.builder = builder = pygubu.Builder()
        #self.rn=None #this is a Pipe
        #self.mgs=None #this is a Pipe
        #2: Load an ui file
        builder.add_from_file('sensorUI.ui')
        self.msgs=[]
        self.running=False
        #3: Create the mainwindow
        self.mainwindow = builder.get_object('toplevel1')
        self.strt_btn=builder.get_object('go')
        self.strt_btn['command']=self.start
        #the buttons
        self.i1tp=self.builder.get_object('id1_temp_p_txt')
        self.i1th=self.builder.get_object('id1_temp_h_txt')
        self.i1p=self.builder.get_object('id1_pressure_txt')
        self.i1h=self.builder.get_object('id1_humidity_txt')

        self.i2tp=self.builder.get_object('id2_temp_p_txt')
        self.i2th=self.builder.get_object('id2_temp_h_txt')
        self.i2p=self.builder.get_object('id2_pressure_txt')
        self.i3h=self.builder.get_object('id3_humidity_txt')

        self.i4tp=self.builder.get_object('id4_temp_p_txt')
        self.i4th=self.builder.get_object('id4_temp_h_txt')
        self.i7p=self.builder.get_object('id7_pressure_txt')
        self.i7h=self.builder.get_object('id7_humidity_txt')

        self.i5tp=self.builder.get_object('id5_temp_p_txt')
        self.i5th=self.builder.get_object('id5_temp_h_txt')
        self.i5p=self.builder.get_object('id5_pressure_txt')
        self.i11h=self.builder.get_object('id11_humidity_txt')

        self.i6tp=self.builder.get_object('id6_temp_p_txt')
        self.i6th=self.builder.get_object('id6_temp_h_txt')
        self.i6p=self.builder.get_object('id6_pressure_txt')
        self.i6h=self.builder.get_object('id6_humidity_txt')

        self.i8tp=self.builder.get_object('id8_temp_p_txt')
        self.i8th=self.builder.get_object('id8_temp_h_txt')
        self.i8p=self.builder.get_object('id8_pressure_txt')
        self.i13h=self.builder.get_object('id13_humidity_txt')
        
        self.i9tp=self.builder.get_object('id9_temp_p_txt')
        self.i9th=self.builder.get_object('id9_temp_h_txt')
        self.i9p=self.builder.get_object('id9_pressure_txt')
        self.i15h=self.builder.get_object('id15_humidity_txt')

        self.i10tp=self.builder.get_object('id10_temp_p_txt')
        self.i10th=self.builder.get_object('id10_temp_h_txt')
        self.i14p=self.builder.get_object('id14_pressure_txt')
        self.i14h=self.builder.get_object('id14_humidity_txt')

        self.i12tp=self.builder.get_object('id12_temp_p_txt')
        self.i12th=self.builder.get_object('id12_temp_h_txt')
        self.i12p=self.builder.get_object('id12_pressure_txt')
        self.i17h=self.builder.get_object('id17_humidity_txt')

        self.i16tp=self.builder.get_object('id16_temp_p_txt')
        self.i16th=self.builder.get_object('id16_temp_h_txt')
        self.i16p=self.builder.get_object('id16_pressure_txt')
        self.i16h=self.builder.get_object('id16_humidity_txt')

    def run(self):
        #self.rn=rn
        #self.mgs=mgs
        self.mainwindow.mainloop()        
    def start(self):
        self.running=True
        par_run.send(True)
        self.showData()
    def stop(self):
        self.running=False
        self.strt_btn['command']=self.start
        self.strt_btn['text']='start'
        par_run.send(False)

    def showData(self):
        global topics
        if self.running:
            if self.strt_btn['text']=='start':
                self.strt_btn['command']=self.stop
                self.strt_btn['text']='stop'
            #pl=par_mgs.poll()
            #print(pl)
            #if pl:
            #    self.msgs=par_run.recv()
            self.msgs=checkqueue()
            if len(self.msgs)>0:
                for msg in self.msgs:
                    if 'temp_p' in list(msg.items())[0][1]:
                        #print(list(msg.items())[0][1]['temp_p'])
                        c_val=list(msg.items())[0][1]['temp_p']
                        f_val=(c_val)*1.8+32
                        list(msg.items())[0][1]['temp_p']=f_val
                    if 'temp_h' in list(msg.items())[0][1]:
                        #print(list(msg.items())[0][1]['temp_h'])
                        c_val=list(msg.items())[0][1]['temp_h']
                        f_val=(c_val)*1.8+32
                        list(msg.items())[0][1]['temp_h']=f_val
                    if list(msg.items())[0][0]=='1':
                        self.i1tp.delete('1.0',tk.END)
                        self.i1tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        self.i1th.delete('1.0',tk.END)
                        self.i1th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        self.i1p.delete('1.0',tk.END)
                        self.i1p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        self.i1h.delete('1.0',tk.END)
                        self.i1h.insert('1.0',list(msg.items())[0][1]['humidity'])
                    
                    if list(msg.items())[0][0]=='2':
                        self.i2tp.delete('1.0',tk.END)
                        self.i2tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        self.i2th.delete('1.0',tk.END)
                        self.i2th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        self.i2p.delete('1.0',tk.END)
                        self.i2p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        #self.i2h.delete('1.0',tk.END)
                        #self.i2h.insert('1.0',list(msg.items())[0][1]['humidity'])
                    
                    if list(msg.items())[0][0]=='3':
                        #self.i3tp.delete('1.0',tk.END)
                        #self.i3tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        #self.i3th.delete('1.0',tk.END)
                        #self.i3th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        #self.i3p.delete('1.0',tk.END)
                        #self.i3p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        self.i3h.delete('1.0',tk.END)
                        self.i3h.insert('1.0',list(msg.items())[0][1]['humidity'])

                    if list(msg.items())[0][0]=='4':
                        self.i4tp.delete('1.0',tk.END)
                        self.i4tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        self.i4th.delete('1.0',tk.END)
                        self.i4th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        #self.i4p.delete('1.0',tk.END)
                        #self.i4p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        #self.i4h.delete('1.0',tk.END)
                        #self.i4h.insert('1.0',list(msg.items())[0][1]['humidity'])

                    if list(msg.items())[0][0]=='5':
                        self.i5tp.delete('1.0',tk.END)
                        self.i5tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        self.i5th.delete('1.0',tk.END)
                        self.i5th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        self.i5p.delete('1.0',tk.END)
                        self.i5p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        #self.i5h.delete('1.0',tk.END)
                        #self.i5h.insert('1.0',list(msg.items())[0][1]['humidity'])

                    if list(msg.items())[0][0]=='6':
                        self.i6tp.delete('1.0',tk.END)
                        self.i6tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        self.i6th.delete('1.0',tk.END)
                        self.i6th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        self.i6p.delete('1.0',tk.END)
                        self.i6p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        self.i6h.delete('1.0',tk.END)
                        self.i6h.insert('1.0',list(msg.items())[0][1]['humidity'])
                    
                    if list(msg.items())[0][0]=='7':
                        #self.i7tp.delete('1.0',tk.END)
                        #self.i7tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        #self.i7th.delete('1.0',tk.END)
                        #self.i7th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        self.i7p.delete('1.0',tk.END)
                        self.i7p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        self.i7h.delete('1.0',tk.END)
                        self.i7h.insert('1.0',list(msg.items())[0][1]['humidity'])

                    if list(msg.items())[0][0]=='8':
                        self.i8tp.delete('1.0',tk.END)
                        self.i8tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        self.i8th.delete('1.0',tk.END)
                        self.i8th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        self.i8p.delete('1.0',tk.END)
                        self.i8p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        #self.i8h.delete('1.0',tk.END)
                        #self.i8h.insert('1.0',list(msg.items())[0][1]['humidity'])

                    if list(msg.items())[0][0]=='9':
                        self.i9tp.delete('1.0',tk.END)
                        self.i9tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        self.i9th.delete('1.0',tk.END)
                        self.i9th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        self.i9p.delete('1.0',tk.END)
                        self.i9p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        #self.i9h.delete('1.0',tk.END)
                        #self.i9h.insert('1.0',list(msg.items())[0][1]['humidity'])

                    if list(msg.items())[0][0]=='10':
                        self.i10tp.delete('1.0',tk.END)
                        self.i10tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        self.i10th.delete('1.0',tk.END)
                        self.i10th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        #self.i10p.delete('1.0',tk.END)
                        #self.i10p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        #self.i10h.delete('1.0',tk.END)
                        #self.i10h.insert('1.0',list(msg.items())[0][1]['humidity'])

                    if list(msg.items())[0][0]=='11':
                        #self.i11tp.delete('1.0',tk.END)
                        #self.i11tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        #self.i11th.delete('1.0',tk.END)
                        #self.i11th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        #self.i11p.delete('1.0',tk.END)
                        #self.i11p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        self.i11h.delete('1.0',tk.END)
                        self.i11h.insert('1.0',list(msg.items())[0][1]['humidity'])

                    if list(msg.items())[0][0]=='12':
                        self.i12tp.delete('1.0',tk.END)
                        self.i12tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        self.i12th.delete('1.0',tk.END)
                        self.i12th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        self.i12p.delete('1.0',tk.END)
                        self.i12p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        #self.i12h.delete('1.0',tk.END)
                        #self.i12h.insert('1.0',list(msg.items())[0][1]['humidity'])

                    if list(msg.items())[0][0]=='13':
                        #self.i13tp.delete('1.0',tk.END)
                        #self.i13tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        #self.i13th.delete('1.0',tk.END)
                        #self.i13th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        #self.i13p.delete('1.0',tk.END)
                        #self.i13p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        self.i13h.delete('1.0',tk.END)
                        self.i13h.insert('1.0',list(msg.items())[0][1]['humidity'])

                    if list(msg.items())[0][0]=='14':
                        #self.i14tp.delete('1.0',tk.END)
                        #self.i14tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        #self.i14th.delete('1.0',tk.END)
                        #self.i14th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        self.i14p.delete('1.0',tk.END)
                        self.i14p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        self.i14h.delete('1.0',tk.END)
                        self.i14h.insert('1.0',list(msg.items())[0][1]['humidity'])

                    if list(msg.items())[0][0]=='15':
                        #self.i15tp.delete('1.0',tk.END)
                        #self.i15tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        #self.i15th.delete('1.0',tk.END)
                        #self.i15th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        #self.i15p.delete('1.0',tk.END)
                        #self.i15p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        self.i15h.delete('1.0',tk.END)
                        self.i15h.insert('1.0',list(msg.items())[0][1]['humidity'])

                    if list(msg.items())[0][0]=='16':
                        self.i16tp.delete('1.0',tk.END)
                        self.i16tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        self.i16th.delete('1.0',tk.END)
                        self.i16th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        self.i16p.delete('1.0',tk.END)
                        self.i16p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        self.i16h.delete('1.0',tk.END)
                        self.i16h.insert('1.0',list(msg.items())[0][1]['humidity'])

                    if list(msg.items())[0][0]=='17':
                        #self.i17tp.delete('1.0',tk.END)
                        #self.i17tp.insert('1.0',list(msg.items())[0][1]['temp_p'])
                        #self.i17th.delete('1.0',tk.END)
                        #self.i17th.insert('1.0',list(msg.items())[0][1]['temp_h'])
                        #self.i17p.delete('1.0',tk.END)
                        #self.i17p.insert('1.0',list(msg.items())[0][1]['pressure'])
                        self.i17h.delete('1.0',tk.END)
                        self.i17h.insert('1.0',list(msg.items())[0][1]['humidity'])
                    
                        
                self.msgs=[]
            self.mainwindow.after(1000,self.showData) #in miliseconds
def checkqueue():
    global q
    my_mgs=[]
    while not q.empty():
        dta=q.get()
        my_mgs.append(dta)
    return my_mgs
def receiveData(rn,mgs,topics):
    msgs=None
    running=False

    broker="192.168.0.11"
    try:
        while True:
            pl=rn.poll()
            if pl:
                ans=rn.recv()
                if ans==True:
                    running=True
                elif ans==False:
                    running=False
            #running=True
            if running:
                print(".")
                msgs = subscribe.simple(topics=topics, hostname=broker, msg_count=8)
                pylds=[]
                for msg in msgs:
                    #print(msg.topic)
                    pyld=ast.literal_eval(msg.topic+msg.payload.decode())
                    mgs.put(pyld)
                    #msg_json=json.dump(pyld)
                    #print(pyld)# this is a json block.  send the payload to a recorder
                    pylds.append(pyld)
                timStr=str(time.strftime("%H:%M:%S",time.gmtime(time.time())))
                recordData({timStr:pylds}, date.today())
            else:
                print("paused data collection")
            time.sleep(1)
    except KeyboardInterrupt:
        print("stopped receiving data")
    finally:
        sys.exit()
                    
def recordData(dta, day):
    
    #print(day.strftime("%b-%d-%Y"))
    #if self.tim.strftime("%b-%d-%Y")==day.strftime("%b-%d-%Y"):
    #print(day.strftime("%b-%d-%Y"))
    fil=str(day.strftime("%b-%d-%Y"))+'_out.json'
    #print(fil)
    #if not exists(fil):
    #    with open(fil,'w') as jfil:
    #        json.dump({},jfil)
    #        jfil.close()
    #with open(fil,'r') as jfil:
    #    fil_dta=json.load(jfil)
    #    jfil.close()
    with open(fil,'a') as jfil:
        #timStr=str(time.strftime("%H:%M:%S",time.gmtime(time.time())))
        #fil_dta.update({timStr:dta})
        #jfil.seek(0)
        json.dump(dta,jfil)#, indent=4, sort_keys=True)
        jfil.write('\n')
    #jstring=json.dump(dta)
    #else:
    #    self.tim=day
    return
if __name__ == '__main__':
    global par_run
    #global par_mgs
    app = SensorApp()
    global q
    q=Queue()
    global topics
    topics=[
    "{\'1\':",
    "{\'2\':",
    "{\'3\':",
    "{\'4\':",
    "{\'5\':",
    "{\'6\':",
    "{\'7\':",
    "{\'8\':",
    "{\'9\':",
    "{\'10\':",
    "{\'11\':",
    "{\'12\':",
    "{\'13\':",
    "{\'14\':",
    "{\'15\':",
    "{\'16\':",
    "{\'17\':"
    ]
    par_run, chi_run=Pipe()
    #par_mgs, chi_mgs=Pipe()
    
    p=Process(target=receiveData,args=(chi_run,q,topics))
    p.start()
    
    app.run()
    p.join()