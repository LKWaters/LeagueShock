import Read
import time
import random
import serial
import plotly.graph_objects as go
import numpy as np

var = 0
var2 = 0
var3 = 0
var4 = 0
count = 0
hithook = 0
misshook = 0
lantern = 0
flay = 0
ultct = 0
timeplot = 0.5
z = 1
run = True
Healtharr = []
Manaarr = []
timer = []
hithookarr = []
hithookarrx = []
misshookarr = []
misshookarrx = []
lanternarr = []
lanternarrx = []
flayarr = []
flayarrx = []
ultarr = []
ultarrx = []

#ardData = serial.Serial('COM4',9600)


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

    Healtharr.append(Health)
    Manaarr.append(Mana)

    hookexpect = 0
    
    if lvl1>0:
        hookexpect = (hookcd -(hookmod*(lvl1-1))) *(1-int(cdr[1:len(cdr)])/100)

    if var == 0:
        if(len(ab1)>1):
            if(int(ab1[1:len(ab1)]) > hookexpect-3+var):
                if count > 1:
                    misshook = misshook+1
                    misshookarr.append(Mana)
                    temp = timer.pop()
                    timer.append(temp)
                    misshookarrx.append(temp+0.5)
                    count = -1
                    var = 5
                count = count+1
            else:
                if count > 0:
                    hithook = hithook+1
                    hithookarr.append(Mana)
                    temp = timer.pop()
                    timer.append(temp)
                    hithookarrx.append(temp+0.5)
                count = 0
    else:
        var = var-1


    if var2 == 0:
        if(len(ab2)>1):
            if int(ab2[1:len(ab2)]) == 6:
                lantern = lantern+1
                lanternarr.append(Mana)
                temp = timer.pop()
                timer.append(temp)
                lanternarrx.append(temp+0.5)
                var2  = 5
    else:
        var2 = var2-1

    if var3 == 0:
        if(len(ab3)>1):
            if int(ab3[1:len(ab3)]) == 4:
                flay = flay+1
                flayarr.append(Mana)
                temp = timer.pop()
                timer.append(temp)
                flayarrx.append(temp+0.5)
                var3 = 5
    else:
        var3 = var3-1

    if var4 == 0:
        if(len(ult)>1):
            if int(ult[1:len(ult)]) == 50:
                ultct = ultct+1
                ultarr.append(Mana)
                temp = timer.pop()
                timer.append(temp)
                ultarrx.append(temp+0.5)
                var4 = 5
    else:
        var4 = var4-1


    f=open(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\stats.csv', "w")
    f.write('missed hooks:' + str(misshook)+ ', hit hooks:' + str(hithook) + ', lanterns:' + str(lantern) + ', flays:' + str(flay) + ', Ults:' + str(ultct))
    f.write('\r\n'+str(np.array(Healtharr)))
    f.write('\r\n'+str(np.array(Manaarr)))
    f.close()
    timer.append(z*timeplot)
    z = z+1
    time.sleep(0.5)



del Healtharr[-1]
del Manaarr[-1]

fig = go.Figure()
fig.add_trace(go.Scatter(x = np.array(timer),y=np.array(Healtharr),name = 'Health', line = dict(color = 'red')))
fig.add_trace(go.Scatter(x = np.array(timer),y=np.array(Manaarr),name = 'Mana',  line = dict(color = 'blue')))
fig.add_trace(go.Scatter(x = misshookarrx, y=misshookarr,mode='markers', name='MissHook', line = dict(color = 'black', width = 8)))
fig.add_trace(go.Scatter(x = hithookarrx, y=hithookarr,mode='markers', name='HitHook', line = dict(color = 'white', width = 8)))
fig.add_trace(go.Scatter(x = lanternarrx, y=lanternarr,mode='markers', name='Lantern', line = dict(color = 'purple', width = 8)))
fig.add_trace(go.Scatter(x = flayarrx, y=flayarr,mode='markers', name='Flay', line = dict(color = 'orange', width = 8)))
fig.add_trace(go.Scatter(x = ultarrx, y=ultarr,mode='markers', name='ULT', line = dict(color = 'purple', width = 8)))
fig.show()
