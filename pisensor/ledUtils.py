from sense_hat import SenseHat
from time import sleep
from random import randint
import random
#times of clock, 0 to 7 0 is 12oClock, 2 is 3oClock, 3 is 6oClock, 6 is 9oClock
r=(255,0,0)
o=(255,165,0)
y=(255,255,0)
g=(0,255,0)
b=(0,0,255)
i=(111,0,238)
v=(134,1,175)
k=(0,0,0)
w=(255,255,255)
gr=(100,100,100)
on=[k,k,k,gr,gr,k,k,k,k,k,k,gr,gr,k,k,k,k,k,k,gr,gr,k,k,k,k,k,k,gr,gr,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k]
tw=[k,k,k,k,k,k,k,gr,k,k,k,k,k,k,gr,k,k,k,k,k,k,gr,k,k,k,k,k,k,gr,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k]
thr=[k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,gr,gr,gr,gr,k,k,k,k,gr,gr,gr,gr,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k]
fur=[k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,gr,k,k,k,k,k,k,k,k,gr,k,k,k,k,k,k,k,k,gr,k,k,k,k,k,k,k,k,gr]
fiv=[k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,gr,gr,k,k,k,k,k,k,gr,gr,k,k,k,k,k,k,gr,gr,k,k,k,k,k,k,gr,gr,k,k,k]
sx=[k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,gr,k,k,k,k,k,k,gr,k,k,k,k,k,k,gr,k,k,k,k,k,k,gr,k,k,k,k,k,k,k]
svn=[k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,gr,gr,gr,gr,k,k,k,k,gr,gr,gr,gr,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k]
egt=[gr,k,k,k,k,k,k,k,k,gr,k,k,k,k,k,k,k,k,gr,k,k,k,k,k,k,k,k,gr,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k]
pixmap=[on,tw,thr,fur,fiv,sx,svn,egt]
sense=SenseHat()
#sense.set_pixel(0,0,r)
#sense.set_pixel(0,1,o)
#sense.set_pixel(0,2,y)
#sense.set_pixel(0,3,g)
#sense.set_pixel(0,4,b)
#sense.set_pixel(0,5,i)
#sense.set_pixel(0,6,v)
#sense.set_pixel(0,7,gr)
#sense.set_pixel(1,0,w)
def sparkle(time):
	while True:
		num1=randint(0,255)
		num2=randint(0,255)
		num3=randint(0,255)
		color=(num1,num2,num3)
		space1=randint(0,7)
		space2=randint(0,7)
		sense.set_pixel(space1,space2,color)
		sleep(time)
	return
def clock(time):
	ans=time%8
	sense.set_pixels(pixmap[ans])
	return
def lightAll(col):
    for i in range(8):
        for j in range(8):
            sense.set_pixel(i,j,col)
def matrix(secs):
    pixmp=[k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k,k]
    mat=(0,150,0)
    while True:
        for i in range(8):
            pixmp[0]=k
            pixmp[1]=k
            pixmp[2]=k
            pixmp[3]=k
            pixmp[4]=k
            pixmp[5]=k
            pixmp[6]=k
            pixmp[7]=k
            for cl in range(8):
                if random.uniform(0,1)<=.25:
                    pixmp[cl]=mat
                else:
                    pixmp[cl]=k
                sense.set_pixels(pixmp)
            sleep(secs)
            for j in range(6,-1,-1):
                pixmp[((j+1)*8)]=k
                pixmp[((j+1)*8)+1]=k
                pixmp[((j+1)*8)+2]=k
                pixmp[((j+1)*8)+3]=k
                pixmp[((j+1)*8)+4]=k
                pixmp[((j+1)*8)+5]=k
                pixmp[((j+1)*8)+6]=k
                pixmp[((j+1)*8)+7]=k
                for col in range(8):
                    pixmp[((j+1)*8)+col]=pixmp[((j)*8)+col]
def numbers(num,unit):
    if unit=='c':
        tmp=num
    elif unit=='f':
        tmp=(num*1.8)+32
    elif unit=='k':
        tmp=num+273.15
    else:
        tmp=num
    ones=int(tmp%10)
    tens=int((tmp-ones)/10)
    #print(tens)
    #print(ones)
    one=[(1,1),(0,2),(1,2),(1,3),(1,4),(0,5),(1,5),(2,5)]
    two=[(0,1),(1,1),(2,1),(2,2),(0,3),(1,3),(2,3),(0,4),(0,5),(1,5),(2,5)]
    three=[(0,1),(1,1,),(2,1),(2,2),(0,3),(1,3),(2,3),(2,4),(0,5),(1,5),(2,5)]
    four=[(0,1),(2,1),(0,2),(2,2),(0,3),(1,3),(2,3),(2,4),(2,5)]
    five=[(0,1),(1,1),(2,1),(0,2),(0,3),(1,3),(2,3),(2,4),(0,5),(1,5),(2,5)]
    six=[(0,1),(1,1),(2,1),(0,2),(0,3),(1,3),(2,3),(0,4),(2,4),(0,5),(1,5),(2,5)]
    seven=[(0,1),(1,1),(2,1),(0,2),(2,2),(2,3),(2,4),(2,5)]
    eight=[(0,1),(1,1),(2,1),(0,2),(2,2),(0,3),(1,3),(2,3),(0,4),(2,4),(0,5),(1,5),(2,5)]
    nine=[(0,1),(1,1),(2,1),(0,2),(2,2),(0,3),(1,3),(2,3),(2,4),(1,5),(2,5)]
    zero=[(0,1),(1,1),(2,1),(0,2),(2,2),(0,3),(2,3),(0,4),(2,4),(0,5),(1,5),(2,5)]
    nums=[zero,one,two,three,four,five,six,seven,eight,nine]
    lightAll((0,0,0))
    printNum(nums[tens],0)
    printNum(nums[ones],5)

def printNum(numList,shift):
    for tup in numList:
        sense.set_pixel(tup[0]+shift,tup[1],gr)
def heartbeat(timer):
    littleHeart=[(2,1),(4,1),(1,2),(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(4,3),(3,4)]
    bigHeart=[(1,1),(2,1),(4,1),(5,1),(0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(1,3),(2,3),(3,3),(4,3),(5,3),(2,4),(3,4),(4,4),(3,5)]
    while True:
        for tup in littleHeart:
            sense.set_pixel(tup[0],tup[1],(100,0,0))
        sleep(timer)
        for tup in bigHeart:
            sense.set_pixel(tup[0],tup[1],(100,0,0))
        sleep(timer)
        lightAll((0,0,0))
def flower(timer):
    topFlower=[(3,0),(4,0),(2,1),(3,1),(4,1),(5,1),(1,2),(3,2),(4,2),(6,2),(0,3),(1,3),(2,3),(5,3),(6,3),(7,3),(0,4),(1,4),(2,4),(5,4),(6,4),(7,4),(1,5),(3,5),(4,5),(6,5),(2,6),(3,6),(4,6),(5,6),(3,7),(4,7)]
    slantFlower=[(1,1),(2,1),(5,1),(6,1),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(2,3),(5,3),(2,4),(5,4),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(1,6),(2,6),(5,6),(6,6)]
    center=[(3,3),(4,3),(3,4),(4,4)]
    while True:
        for tup in topFlower:
            sense.set_pixel(tup[0],tup[1],(100,100,100))
        for tup in center:
            sense.set_pixel(tup[0],tup[1],(100,100,0))
        sleep(timer)
        lightAll((0,0,0))
        for tup in slantFlower:
            sense.set_pixel(tup[0],tup[1],(100,100,100))
        for tup in center:
            sense.set_pixel(tup[0],tup[1],(100,100,0))
        sleep(timer)
        lightAll((0,0,0))
def ladybug():
    ladybugHead=[(2,0),(5,0),(3,1),(4,1)]
    ladyBugBody=[(2,2),(3,2),(4,2),(5,2),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(2,7),(3,7),(4,7),(5,7)]
    dots=[(2,3),(4,3),(5,4),(3,6),(2,5),(5,6)]
    for tup in ladybugHead:
        sense.set_pixel(tup[0],tup[1],(48,48,48))
    for tup in ladyBugBody:
        sense.set_pixel(tup[0],tup[1],(100,0,0))
    for tup in dots:
        sense.set_pixel(tup[0],tup[1],(0,0,0))