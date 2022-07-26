import time
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from sense_hat import SenseHat
import json
import ledUtils as lu
with open('config.json','r') as fil:
    jo=json.load(fil)


mqtt_broker= jo['host'] #'192.168.0.11'
mqtt_port=1883
cnfg=jo['config']
kys=list(cnfg.keys())
numClients=jo['ids']
clients=[]
client_tops=[]
for i in range(len(cnfg.keys())):
    clnt=mqtt.Client(kys[i])
    clnt_top='{\''+kys[i]+'\':'
    clnt.connect(mqtt_broker,mqtt_port)
    clients.append(clnt)
    client_tops.append(clnt_top)

for i in range(numClients):
    clnt=mqtt.Client()

sense=SenseHat()
while True:
    temp_p=sense.get_temperature_from_pressure()
    temp_h=sense.get_temperature_from_humidity()
    humidity=sense.get_humidity()
    pressure=sense.get_pressure()
    compass=sense.get_compass()
    orientation=sense.get_compass_raw()
    data=[]
    data.append(temp_p)
    data.append(temp_h)
    data.append(pressure)
    data.append(humidity)
    data_dict={"temp_p":data[0],"temp_h":data[1],"pressure":data[2],"humidity":data[3]}
    dta=list(data_dict.items())
    iterator=0
    for j in range(len(clients)):
        #print(cnfg[kys[j]])#this value represents the number of sensors each client gets
        print(time.strftime("%Y/%m/%d-%H:%M:%S",time.gmtime(time.time())))
        c_json={}
        for k in range(cnfg[kys[j]]):
            c_json.update({dta[iterator][0]:dta[iterator][1]})
            iterator=iterator+1
	    #print(client_tops[j]+str(c_json)+'}')
        clients[j].publish(client_tops[j],str(c_json)+',\'time\': '+str(time.time())+'}')
    avgTemp=(temp_p+temp_h)/2
    lu.numbers(avgTemp,'f')
    time.sleep(30)


