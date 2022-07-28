import Utils
from tkinter import *
import matplotlib
import serial
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame

Stop_val = False

def Stream():
    global Stop_val
    Stop_val = False
    shock = 0

    Health_l = []
    Mana_l = []

    y = []
    z = []
    n = []

    mana_prev = 2
    A1_prev = 'Ready'
    A2_prev = 'Ready'
    A3_prev = 'Ready'
    Ult_prev = 'Ready'

    while not Stop_val:
        A1_val, A2_val, A3_val, Ult_val, S1_val, S2_val, A1_level_val, A2_level_val, A3_level_val, Ult_level_val, Health_percent, Mana_percent = Utils.Data_Parse()

        A1_level_text = ''
        for x in range(0, A1_level_val):
            A1_level_text = A1_level_text + '*'
        A2_level_text = ''
        for x in range(0, A2_level_val):
            A2_level_text = A2_level_text + '*'
        A3_level_text = ''
        for x in range(0, A3_level_val):
            A3_level_text = A3_level_text + '*'
        Ult_level_text = ''
        for x in range(0, Ult_level_val):
            Ult_level_text = Ult_level_text + '*'

        le1.config(text=A1_level_text)
        le2.config(text=A2_level_text)
        le3.config(text=A3_level_text)
        le4.config(text=Ult_level_text)

        a1.config(text=A1_val)
        a2.config(text=A2_val)
        a3.config(text=A3_val)
        a4.config(text=Ult_val)

        s1.config(text=S1_val)
        s2.config(text=S2_val)

        h1.config(text=Health_percent)
        m1.config(text=Mana_percent)

        Health_l.append(Health_percent)
        Mana_l.append(Mana_percent)

        data1 = {'Health': Health_l, 'Mana': Mana_l}
        color_dict = {'Health': '#c63b39', 'Mana': '#3456cb'}

        if not A1_val == 'Ready':
            if A1_prev == 'Ready' and Mana_percent < mana_prev:
                z.append(len(Mana_l))
                n.append('A1')
                y.append(Mana_percent)
        A1_prev = A1_val
        if not A2_val == 'Ready':
            if A2_prev == 'Ready' and Mana_percent < mana_prev:
                z.append(len(Mana_l))
                n.append('A2')
                y.append(Mana_percent)
        A2_prev = A2_val
        if not A3_val == 'Ready':
            if A3_prev == 'Ready' and Mana_percent < mana_prev:
                z.append(len(Mana_l))
                n.append('A3')
                y.append(Mana_percent)
        A3_prev = A3_val
        if not Ult_val == 'Ready':
            if Ult_prev == 'Ready' and Mana_percent < mana_prev:
                z.append(len(Mana_l))
                n.append('Ult')
                y.append(Mana_percent)
        Ult_prev = Ult_val

        mana_prev = Mana_percent

        figure1 = plt.Figure(figsize=(6, 4), dpi=70)
        figure1.patch.set_facecolor('#5865F2')
        ax1 = figure1.add_subplot(111)
        df1 = DataFrame(data1, columns=['Health', 'Mana'])
        df1.plot(stacked=False, kind='area', legend=True, ax=ax1, color=[color_dict.get(x, '#333333') for x in df1.columns])

        ax1.scatter(z, y)
        for i, txt in enumerate(n):
            ax1.annotate(txt, (z[i], y[i]))

        bar1 = FigureCanvasTkAgg(figure1, ws)
        bar1.get_tk_widget().grid(row=0, padx=10, columnspan=8)

        if var1.get() == 1:
            mod = (A1_level_val-1) * 2
            cd = 20 - mod
            try:
                if int(A1_val) == (cd-3) and not shock == 1:
                    shock = 1
                    ardData = serial.Serial('COM4', 9600)
                    ardData.write(b'1')
                    ardData.write(b'0')
            except:
                shock = 0

        ws.update()

def Stop():
    global Stop_val
    Stop_val = True

ws = Tk()
ws.title("Pavlov's Thresh")
ws.geometry("439x495")
ws['bg']='#5865F2'


figure1 = plt.Figure(figsize=(6,4), dpi=70)
figure1.patch.set_facecolor('#5865F2')
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, ws)
bar1.get_tk_widget().grid(row = 0, padx=10, columnspan=8)

var1 = IntVar()

c1 = Checkbutton(ws, text='Enable Shock',variable=var1, onvalue=1, offvalue=0, background='#5865F2')
c1.grid(row = 1, padx=10, pady=10,column=0, columnspan=2)

le1 = Label(text='', background='#5865F2')
le1.grid(row=2, column=0)
le2 = Label(text='', background='#5865F2')
le2.grid(row=3, column=0)
le3 = Label(text='', background='#5865F2')
le3.grid(row=4, column=0)
le4 = Label(text='', background='#5865F2')
le4.grid(row=5, column=0)

l1 = Label(text='Ability 1:', background='#5865F2')
l1.grid(row=2, column=1)
l2 = Label(text='Ability 2:', background='#5865F2')
l2.grid(row=3, column=1)
l3 = Label(text='Ability 3:', background='#5865F2')
l3.grid(row=4, column=1)
l4 = Label(text='Ultimate:', background='#5865F2')
l4.grid(row=5, column=1)

a1 = Label(text='', background='#5865F2')
a1.grid(row=2, column=2)
a2 = Label(text='', background='#5865F2')
a2.grid(row=3, column=2)
a3 = Label(text='', background='#5865F2')
a3.grid(row=4, column=2)
a4 = Label(text='', background='#5865F2')
a4.grid(row=5, column=2)

ls1 = Label(text='Summoner 1:', background='#5865F2')
ls1.grid(row=2, column=4)
ls2 = Label(text='Summoner 2:', background='#5865F2')
ls2.grid(row=3, column=4)

s1 = Label(text='', background='#5865F2')
s1.grid(row=2, column=5)
s2 = Label(text='', background='#5865F2')
s2.grid(row=3, column=5)

break1 = Label(text='', background='#5865F2')
break1.grid(row=6)

lh1 = Label(text='Health:', background='#5865F2')
lh1.grid(row=7, column=0)
h1 = Label(text='', background='#5865F2')
h1.grid(row=7, column=1)

lm1 = Label(text='Mana:', background='#5865F2')
lm1.grid(row=7, column=3)
m1 = Label(text='', background='#5865F2')
m1.grid(row=7, column=4)

Button(ws,text="Start",command=Stream).grid(row = 8, column=5, pady=10, columnspan=1)
Button(ws,text="Stop",command=Stop).grid(row = 8, column=6, pady=10, columnspan=1)

ws.mainloop()
