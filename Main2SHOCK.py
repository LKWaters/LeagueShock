import Read
import time
import random
import serial
import numpy as np

var = 0
count = 0
run = True


ardData = serial.Serial('COM4',9600)


while(run):
    hookcd = 20
    lanterncd = 22
    flaycd = 9
    ultcd = 140

    hookmod = 2
    lanternmod = 2.5
    flaymod = 0
    ultmod = 20

    ab1, ab2, ab3, ult, cdr, lvl1, lvl2, lvl3, lvlult, run, Health, Mana = Read.parse()

    hookexpect = 0

    if lvl1>0:
        hookexpect = (hookcd -(hookmod*(lvl1-1))) *(1-int(cdr[1:len(cdr)])/100)

    if var == 0:
        if(len(ab1)>1):
            if(int(ab1[1:len(ab1)]) > hookexpect-3+var):
                if count > 1:
                    var = 5
                    print('miss')
                    ardData.write(b'1')
                    ardData.write(b'0')
                    count = -1
                count = count+1
            else:
                if count > 0:
                    print('hit')
                count = 0
    else:
        var = var-1

    time.sleep(0.5)
