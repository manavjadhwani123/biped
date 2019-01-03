import smartServo as sServo
import constants as k
import time 
import numpy as np
from inverse_kine_v3 import calculateangles
def homeposn(l,o,c,p,e,f,g,h):
        sServo.writeRawAngle(k.servoId[0],l)
        sServo.writeRawAngle(k.servoId[1],o)
        sServo.writeRawAngle(k.servoId[2],c)
        sServo.writeRawAngle(k.servoId[3],p)
        sServo.writeRawAngle(k.servoId[4],e)
        sServo.writeRawAngle(k.servoId[5],f)
        sServo.writeRawAngle(k.servoId[6],g)
        sServo.writeRawAngle(k.servoId[7],h)
def speedset(j):
        for i in range(0,8):
            sServo.setSpeed(k.servoId[i],j)
if __name__=="__main__":
    sServo.init()
    servoList = []
    for i in range(0,8):
        servo = sServo.SmartServo(ID=k.servoId[i],dirVector=k.dirVector[i],fixedPoint=k.FixedPoints[i],enableTorque=True)
        servoList.append(servo)
    while True:
        speedset(350)
        # homeposn(190+00,200+00,512-00,500-00,480+00,760-0,500-00,500-00) #Home position
        # time.sleep(0.08)

        # homeposn(k.FixedPoints[0]+00,k.FixedPoints[1]+200,k.FixedPoints[2]-300,k.FixedPoints[3]-100,k.FixedPoints[4]+00,k.FixedPoints[5]-220,k.FixedPoints[6]-300,k.FixedPoints[7]-100) #Home position
        # time.sleep(0.08)
        # homeposn(k.FixedPoints[0]+00,k.FixedPoints[1]+200,k.FixedPoints[2]-300,k.FixedPoints[3]-100,k.FixedPoints[4]+00,k.FixedPoints[5]-320,k.FixedPoints[6]-350,k.FixedPoints[7]-100) #Step height
        # time.sleep(0.08)
        # homeposn(k.FixedPoints[0]+00,k.FixedPoints[1]+200,k.FixedPoints[2]-300,k.FixedPoints[3]-100,k.FixedPoints[4]+00,k.FixedPoints[5]-120,k.FixedPoints[6]-250,k.FixedPoints[7]-100)  #forward push
        # time.sleep(0.08)
        # homeposn(k.FixedPoints[0]+00,k.FixedPoints[1]+200,k.FixedPoints[2]-300,k.FixedPoints[3]-100,k.FixedPoints[4]+00,k.FixedPoints[5]-120,k.FixedPoints[6]-200,k.FixedPoints[7]-100)  # down3k.Fixek.FixedPoints[4]intsk.FixedPoints[5]    ,k.FixedPoints[6]# homk.FixedPoints[7]sn(k.FixedPoints[0]+00,k.FixedPoints[1]+200,k.FixedPoints[2]-300,k.FixedPoints[3]-100,k.FixedPoints[4]+00,k.FixedPoints[5]-120,k.FixedPoints[6]-200,k.FixedPoints[7]-200) # end eff in normal pos
        # time.sleep(0.08)
        # homeposn(k.FixedPoints[0]+00,k.FixedPoints[1]+200,k.FixedPoints[2]-300,k.FixedPoints[3]-100,k.FixedPoints[4]+00,k.FixedPoints[5]-150,k.FixedPoints[6]-200,k.FixedPoints[7]-200)
        # time.sleep(0.08)
        # homeposn(k.FixedPoints[0]+00,k.FixedPoints[1]+200,k.FixedPoints[2]-300,k.FixedPoints[3]-100,k.FixedPoints[4]+00,k.FixedPoints[5]-220,k.FixedPoints[6]-200,k.FixedPoints[7]-100)  # home position
        # time.sleep(0.08)
        # homeposn(k.FixedPoints[0]+00,k.FixedPoints[1]+300,k.FixedPoints[2]-450,k.FixedPoints[3]-150,k.FixedPoints[4]+00,k.FixedPoints[5]-220,k.FixedPoints[6]-200,k.FixedPoints[7]-100)  #right step height
        # time.sleep(0.08)
        # homeposn(k.FixedPoints[0]+00,k.FixedPoints[1]+60,k.FixedPoints[2]-350,k.FixedPoints[3]-100,k.FixedPoints[4]+00,k.FixedPoints[5]-220,k.FixedPoints[6]-200,k.FixedPoints[7]-100)  #  forward push
        # time.sleep(0.08)
        # homeposn(k.FixedPoints[0]+00,k.FixedPoints[1]+60,k.FixedPoints[2]-250,k.FixedPoints[3]-200,k.FixedPoints[4]+00,k.FixedPoints[5]-220,k.FixedPoints[6]-200,k.FixedPoints[7]-100)  # down
        # time.sleep(0.08)
        # homeposn(k.FixedPoints[0]+00,k.FixedPoints[1]+70,k.FixedPoints[2]-300,k.FixedPoints[3]-200,k.FixedPoints[4]+00,k.FixedPoints[5]-220,k.FixedPoints[6]-200,k.FixedPoints[7]-100)
        # time.sleep(0.08)
        # homeposn(k.FixedPoints[0]+00,k.FixedPoints[1]+150,k.FixedPoints[2]-300,k.FixedPoints[3]-200,k.FixedPoints[4]+00,k.FixedPoints[5]-220,k.FixedPoints[6]-200,k.FixedPoints[7]-100)
        # time.sleep(0.08)

        l,o,c,p=calculateangles(23.3,0,1.8)
        l=l*1024/300
        o=o*1024/300
        c=c*1024/300
        p=p*1024/300
        e,f,g,h=calculateangles(23.3,0,1.8)
        e=e*1024/300
        f=f*1024/300
        g=g*1024/300
        h=h*1024/300
        homeposn(k.FixedPoints[0]+l,k.FixedPoints[1]+o,k.FixedPoints[2]-c,k.FixedPoints[3]-p,k.FixedPoints[4]+e,k.FixedPoints[5]-f,k.FixedPoints[6]-g,k.FixedPoints[7]-h)
