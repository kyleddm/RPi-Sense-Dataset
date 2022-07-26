from fileinput import filename
import os
import numpy
import scipy
import pickle
import pandas
import json
import tqdm
#months=['Apr','May']#'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
year='2022'
days=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
postfix='_out.json'
cols=['id','temp_p','temp_h','pressure','humidity','date','time']
#myDf=pandas.DataFrame(columns=cols)
flnm=''
#This script reads in the individual json files from the mqtt output and sorts them by RPi, instead of the custom configuration used in the json files.
def postProcess(fl:list)->pandas.DataFrame:
    dataSet=pandas.DataFrame(columns=cols)
    filename=fl[0]
    date=fl[1]
    #print(fl)
    num_lines = sum(1 for line in open(filename,'r'))
    with open(filename,'r') as f:
        #line=f.readline()
        rp2_dict={}
        rp3_dict={}
        rp4_dict={}
        rp6_dict={}
        rp7_dict={}
        rp8_dict={}
        rp9_dict={}
        
        
        for i,line in enumerate(tqdm.tqdm(f, total=num_lines)):
            #print(i)
            jl=json.loads(line)
            #print(jl)
            timestamp=list(jl.keys())[0]#the timestamp
            #print(date)
            #print(timestamp)
            stuff=list(jl.values())[0]#the actual data, with the timestamp stripped
            #print(stuff)
            for sensor in stuff:
                id=list(sensor.keys())[0]
                data_dict={}
                
                #print(sensor[id])#this is a dictionary
                if id == '1':
                    #rpi1
                    data_dict=sensor[id]
                    data_dict['id']='1'
                    data_dict['date']=date
                    data_dict['time']=sensor['time']
                    dataSet=dataSet.append(data_dict,ignore_index=True)
                elif id == '2' or id == '3':
                    #rpi2
                    rp2_dict.update(sensor[id])
                    if 'temp_p' in rp2_dict and 'temp_h' in rp2_dict and 'humidity' in rp2_dict and 'pressure' in rp2_dict:
                        rp2_dict['id']='2'
                        rp2_dict['date']=date
                        rp2_dict['time']=sensor['time']#note, there is a fraction of a second difference between when one id posts data and another id posts data.  This mechanism will only count the latest timestamp
                        dataSet=dataSet.append(rp2_dict,ignore_index=True)
                        rp2_dict={}
                elif id == '4' or id == '7':
                    #rpi3
                    rp3_dict.update(sensor[id])
                    if 'temp_p' in rp3_dict and 'temp_h' in rp3_dict and 'humidity' in rp3_dict and 'pressure' in rp3_dict:
                        rp3_dict['id']='3'
                        rp3_dict['date']=date
                        rp3_dict['time']=sensor['time']#note, there is a fraction of a second difference between when one id posts data and another id posts data.  This mechanism will only count the latest timestamp
                        dataSet=dataSet.append(rp3_dict,ignore_index=True)
                        rp3_dict={}
                elif id == '5' or id == '11':
                    #rpi4
                    rp4_dict.update(sensor[id])
                    if 'temp_p' in rp4_dict and 'temp_h' in rp4_dict and 'humidity' in rp4_dict and 'pressure' in rp4_dict:
                        rp4_dict['id']='4'
                        rp4_dict['date']=date
                        rp4_dict['time']=sensor['time']#note, there is a fraction of a second difference between when one id posts data and another id posts data.  This mechanism will only count the latest timestamp
                        dataSet=dataSet.append(rp4_dict,ignore_index=True)
                        rp4_dict={}
                elif id == '6':
                    #rpi5
                    data_dict=sensor[id]
                    data_dict['id']='5'
                    data_dict['date']=date
                    data_dict['time']=sensor['time']
                    dataSet=dataSet.append(data_dict,ignore_index=True)
                elif id == '8' or id == '13':
                    #rpi6
                    rp6_dict.update(sensor[id])
                    if 'temp_p' in rp6_dict and 'temp_h' in rp6_dict and 'humidity' in rp6_dict and 'pressure' in rp6_dict:
                        rp6_dict['id']='6'
                        rp6_dict['date']=date
                        rp6_dict['time']=sensor['time']#note, there is a fraction of a second difference between when one id posts data and another id posts data.  This mechanism will only count the latest timestamp
                        dataSet=dataSet.append(rp6_dict,ignore_index=True)
                        rp6_dict={}
                elif id == '9' or id == '15':
                    #rpi7
                    rp7_dict.update(sensor[id])
                    if 'temp_p' in rp7_dict and 'temp_h' in rp7_dict and 'humidity' in rp7_dict and 'pressure' in rp7_dict:
                        rp7_dict['id']='7'
                        rp7_dict['date']=date
                        rp7_dict['time']=sensor['time']#note, there is a fraction of a second difference between when one id posts data and another id posts data.  This mechanism will only count the latest timestamp
                        dataSet=dataSet.append(rp7_dict,ignore_index=True)
                        rp7_dict={}
                elif id == '10' or id == '14':
                    #rpi8
                    rp8_dict.update(sensor[id])
                    if 'temp_p' in rp8_dict and 'temp_h' in rp8_dict and 'humidity' in rp8_dict and 'pressure' in rp8_dict:
                        rp8_dict['id']='8'
                        rp8_dict['date']=date
                        rp8_dict['time']=sensor['time']#note, there is a fraction of a second difference between when one id posts data and another id posts data.  This mechanism will only count the latest timestamp
                        dataSet=dataSet.append(rp8_dict,ignore_index=True)
                        rp8_dict={}
                elif id == '12' or id == '17':
                    #rpi9
                    rp9_dict.update(sensor[id])
                    if 'temp_p' in rp9_dict and 'temp_h' in rp9_dict and 'humidity' in rp9_dict and 'pressure' in rp9_dict:
                        rp9_dict['id']='9'
                        rp9_dict['date']=date
                        rp9_dict['time']=sensor['time']#note, there is a fraction of a second difference between when one id posts data and another id posts data.  This mechanism will only count the latest timestamp
                        dataSet=dataSet.append(rp9_dict,ignore_index=True)
                        rp9_dict={}
                elif id == '16':
                    #rip10
                    data_dict=sensor[id]
                    data_dict['id']='10'
                    data_dict['date']=date
                    data_dict['time']=sensor['time']
                    dataSet=dataSet.append(data_dict,ignore_index=True)
                #print(data_dict)
                
    return dataSet
    
def run(months:list):
    print(str(os.getcwd()))
    theDf=pandas.DataFrame(columns=cols)
    for month in months:
        for day in days:
            date=year+month+day
            filname=month+'-'+day+'-'+year+postfix
            if os.path.exists(filname):
                #print(filname)
                fl=[filname,date]
                #this is where the post-processing of the data will go
                theDf=theDf.append(postProcess(fl),ignore_index=True)
    theDf.to_pickle('raw/sensorData_'+''.join(months)+'_byPi.pkl',compression=None)
    return(theDf)

