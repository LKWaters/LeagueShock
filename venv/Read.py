import pyautogui
import cv2
import numpy as np
import time


def parse():
    myScreenshot = pyautogui.screenshot()

    im = myScreenshot.crop((748,1041,1066,1055))
    im.save(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\Health.png')

    im = myScreenshot.crop((748,1056,1066,1070))
    im.save(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\Mana.png')


    im2 = myScreenshot.crop((786,982,823,1020))
    im2.save(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB1.png')

    im2l = myScreenshot.crop((786,1027,827,1035))
    im2l.save(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB1level.png')


    im3 = myScreenshot.crop((839,982,876,1020))
    im3.save(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB2.png')

    im3l = myScreenshot.crop((838,1027,879,1035))
    im3l.save(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB2level.png')


    im4 = myScreenshot.crop((890,982,927,1020))
    im4.save(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB3.png')

    im4l = myScreenshot.crop((888,1027,929,1035))
    im4l.save(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB3level.png')


    imu = myScreenshot.crop((942,982,979,1020))
    imu.save(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\ULT.png')

    imul = myScreenshot.crop((946,1027,987,1035))
    imul.save(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\ULTlevel.png')


    im5 = myScreenshot.crop((750,982,775,1008))
    im5.save(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\Passive.png')

    im6 = myScreenshot.crop((599,1030,607,1050))
    im6.save(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\CDR.png')

    im62 = myScreenshot.crop((607,1030,615,1050))
    im62.save(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\CDR2.png')



    Health = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\Health.png')
    lower_maskh = np.array([0,50,0])
    upper_maskh = np.array([255,255,255])
    thresholdH = cv2.inRange(Health, lower_maskh, upper_maskh)
    cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\Health.png', thresholdH)

    Mana = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\Mana.png')
    lower_maskm = np.array([98,48,0])
    upper_maskm = np.array([255,255,255])
    thresholdM = cv2.inRange(Mana, lower_maskm, upper_maskm)
    cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\Mana.png', thresholdM)


    AB1 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB1.png')
    lower_mask1 = np.array([150,150,150])
    upper_mask1 = np.array([255,255,255])
    threshold1 = cv2.inRange(AB1, lower_mask1, upper_mask1)
    cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB1.png',threshold1)
    AB1l = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB1level.png')
    lower_mask1l = np.array([39,74,83])
    upper_mask1l = np.array([138,202,213])
    threshold1l = cv2.inRange(AB1l, lower_mask1l, upper_mask1l)
    cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB1level.png',threshold1l)

    AB2 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB2.png')
    lower_mask2 = np.array([150,150,150])
    upper_mask2 = np.array([255,255,255])
    threshold2 = cv2.inRange(AB2, lower_mask2, upper_mask2)
    cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB2.png',threshold2)
    AB2l = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB2level.png')
    lower_mask2l = np.array([39,74,83])
    upper_mask2l = np.array([138,202,213])
    threshold2l = cv2.inRange(AB2l, lower_mask2l, upper_mask2l)
    cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB2level.png',threshold2l)


    AB3 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB3.png')
    lower_mask3 = np.array([150,150,150])
    upper_mask3 = np.array([255,255,255])
    threshold3 = cv2.inRange(AB3, lower_mask3, upper_mask3)
    cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB3.png',threshold3)
    AB3l = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB3level.png')
    lower_mask3l = np.array([39,74,83])
    upper_mask3l = np.array([138,202,213])
    threshold3l = cv2.inRange(AB3l, lower_mask3l, upper_mask3l)
    cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\AB3level.png',threshold3l)


    ULT = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\ULT.png')
    lower_masku = np.array([150,150,150])
    upper_masku = np.array([255,255,255])
    thresholdu = cv2.inRange(ULT, lower_masku, upper_masku)
    cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\ULT.png',thresholdu)
    ULTl = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\ULTlevel.png')
    lower_maskul = np.array([39,74,83])
    upper_maskul = np.array([138,202,213])
    thresholdul = cv2.inRange(ULTl, lower_maskul, upper_maskul)
    cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\ULTlevel.png',thresholdul)

    Passive = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\Passive.png')

    CDR = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\CDR.png')
    lower_maskcd = np.array([96,154,151])
    upper_maskcd = np.array([255,255,255])
    thresholdcd = cv2.inRange(CDR, lower_maskcd, upper_maskcd)
    cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\CDR.png',thresholdcd)


    CDR2 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\CDR2.png')
    lower_maskcd = np.array([96,154,151])
    upper_maskcd = np.array([255,255,255])
    thresholdcd2 = cv2.inRange(CDR2, lower_maskcd, upper_maskcd)
    cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\CDR2.png',thresholdcd2)



    s1 = 0
    s2 = 0
    s3 = 0
    ult = 0

    for y in range (0, 40):
        for z in range(0, 7):
            if(threshold1l[z,y] == 255):
                s1 = s1+1
            if(threshold2l[z,y] == 255):
                s2 = s2+1
            if(threshold3l[z,y] == 255):
                s3 = s3+1
            if(thresholdul[z,y] == 255):
                ult = ult+1

    s1 = round(s1/24)
    s2 = round(s2/24)
    s3 = round(s3/24)
    ult = round(ult/24)




    CDfinal = ':'

    zero = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\LinearCDR\0.png')
    one = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\LinearCDR\1.png')
    two = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\LinearCDR\2.png')
    three = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\LinearCDR\3.png')
    four = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\LinearCDR\4.png')
    five = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\LinearCDR\5.png')
    six = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\LinearCDR\6.png')
    seven = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\LinearCDR\7.png')
    eight = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\LinearCDR\8.png')
    nine = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\LinearCDR\9.png')
    test = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\CDR.png')
    test2 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\CDR2.png')

    dif0 = cv2.subtract(test, zero)
    dif1 = cv2.subtract(test, one)
    dif2 = cv2.subtract(test, two)
    dif3 = cv2.subtract(test, three)
    dif4 = cv2.subtract(test, four)
    dif5 = cv2.subtract(test, five)
    dif6 = cv2.subtract(test, six)
    dif7 = cv2.subtract(test, seven)
    dif8 = cv2.subtract(test, eight)
    dif9 = cv2.subtract(test, nine)

    dif02 = cv2.subtract(test2, zero)
    dif12 = cv2.subtract(test2, one)
    dif22 = cv2.subtract(test2, two)
    dif32 = cv2.subtract(test2, three)
    dif42 = cv2.subtract(test2, four)
    dif52 = cv2.subtract(test2, five)
    dif62 = cv2.subtract(test2, six)
    dif72 = cv2.subtract(test2, seven)
    dif82 = cv2.subtract(test2, eight)
    dif92 = cv2.subtract(test2, nine)

    b0, g0, r0 = cv2.split(dif0)
    b1, g1, r1 = cv2.split(dif1)
    b2, g2, r2 = cv2.split(dif2)
    b3, g3, r3 = cv2.split(dif3)
    b4, g4, r4 = cv2.split(dif4)
    b5, g5, r5 = cv2.split(dif5)
    b6, g6, r6 = cv2.split(dif6)
    b7, g7, r7 = cv2.split(dif7)
    b8, g8, r8 = cv2.split(dif8)
    b9, g9, r9 = cv2.split(dif9)

    b02, g02, r02 = cv2.split(dif02)
    b12, g12, r12 = cv2.split(dif12)
    b22, g22, r22 = cv2.split(dif22)
    b32, g32, r32 = cv2.split(dif32)
    b42, g42, r42 = cv2.split(dif42)
    b52, g52, r52 = cv2.split(dif52)
    b62, g62, r62 = cv2.split(dif62)
    b72, g72, r72 = cv2.split(dif72)
    b82, g82, r82 = cv2.split(dif82)
    b92, g92, r92 = cv2.split(dif92)

    if cv2.countNonZero(b0) < 5 and cv2.countNonZero(g0) < 5 and cv2.countNonZero(r0) < 5:
        CDfinal = CDfinal + '0'
    elif cv2.countNonZero(b1) < 10 and cv2.countNonZero(g1) < 10 and cv2.countNonZero(r1) < 10:
        CDfinal = CDfinal + '1'
    elif cv2.countNonZero(b2) < 5 and cv2.countNonZero(g2) < 5 and cv2.countNonZero(r2) < 5:
        CDfinal = CDfinal + '2'
    elif cv2.countNonZero(b3) < 5 and cv2.countNonZero(g3) < 5 and cv2.countNonZero(r3) < 5:
        CDfinal = CDfinal + '3'
    elif cv2.countNonZero(b4) < 10 and cv2.countNonZero(g4) < 10 and cv2.countNonZero(r4) < 10:
        CDfinal = CDfinal + '4'
    elif cv2.countNonZero(b5) < 10 and cv2.countNonZero(g5) < 10 and cv2.countNonZero(r5) < 10:
        CDfinal = CDfinal + '5'
    elif cv2.countNonZero(b6) < 10 and cv2.countNonZero(g6) < 10 and cv2.countNonZero(r6) < 10:
        CDfinal = CDfinal + '6'
    elif cv2.countNonZero(b7) < 10 and cv2.countNonZero(g7) < 10 and cv2.countNonZero(r7) < 10:
        CDfinal = CDfinal + '7'
    elif cv2.countNonZero(b8) < 10 and cv2.countNonZero(g8) < 10 and cv2.countNonZero(r8) < 10:
        CDfinal = CDfinal + '8'
    elif cv2.countNonZero(b9) < 10 and cv2.countNonZero(g9) < 10 and cv2.countNonZero(r9) < 10:
        CDfinal = CDfinal + '9'

    if cv2.countNonZero(b02) < 5 and cv2.countNonZero(g02) < 5 and cv2.countNonZero(r02) < 5:
        CDfinal = CDfinal + '0'
    elif cv2.countNonZero(b12) < 10 and cv2.countNonZero(g12) < 10 and cv2.countNonZero(r12) < 10:
        CDfinal = CDfinal + '1'
    elif cv2.countNonZero(b22) < 5 and cv2.countNonZero(g22) < 5 and cv2.countNonZero(r22) < 5:
        CDfinal = CDfinal + '2'
    elif cv2.countNonZero(b32) < 5 and cv2.countNonZero(g32) < 5 and cv2.countNonZero(r32) < 5:
        CDfinal = CDfinal + '3'
    elif cv2.countNonZero(b42) < 10 and cv2.countNonZero(g42) < 10 and cv2.countNonZero(r42) < 10:
        CDfinal = CDfinal + '4'
    elif cv2.countNonZero(b52) < 10 and cv2.countNonZero(g52) < 10 and cv2.countNonZero(r52) < 10:
        CDfinal = CDfinal + '5'
    elif cv2.countNonZero(b62) < 10 and cv2.countNonZero(g62) < 10 and cv2.countNonZero(r62) < 10:
        CDfinal = CDfinal + '6'
    elif cv2.countNonZero(b72) < 10 and cv2.countNonZero(g72) < 10 and cv2.countNonZero(r72) < 10:
        CDfinal = CDfinal + '7'
    elif cv2.countNonZero(b82) < 10 and cv2.countNonZero(g82) < 10 and cv2.countNonZero(r82) < 10:
        CDfinal = CDfinal + '8'
    elif cv2.countNonZero(b92) < 10 and cv2.countNonZero(g92) < 10 and cv2.countNonZero(r92) < 10:
        CDfinal = CDfinal + '9'


    zero2 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\0.png')
    zero2dash = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\0-.png')
    one2 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\1.png')
    two2 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\2.png')
    two2dash = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\2-.png')
    three2 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\3.png')
    three2dash = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\3-.png')
    three2dashdash = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\3--.png')
    four2 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\4.png')
    five2 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\5.png')
    five2dash = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\5-.png')
    six2 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\6.png')
    six2dash = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\6-.png')
    seven2 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\7.png')
    seven2dash = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\7-.png')
    eight2 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\8.png')
    eight2dash = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\8-.png')
    nine2 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\9.png')

    height, width = thresholdu.shape
    arr = []

    for i in range (0,width):
        count = 0
        for j in range (0,height):
            if thresholdu[j,i] == 255:
                count = count +1
        if count == 0:
            arr.append(i)

    numar = np.array(arr)
    total = ':'

    for k in range (len(numar)-1):
        if numar[k+1]> numar[k]+1:
            add = 0
            minus = 0
            if k+9 > width:
                add = width-1
                minus = width-10
            else:
                minus = numar[k]
                add = numar[k]+9
            number = thresholdu[0:height, minus:add]
            cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\temp.png', number)

            number = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\temp.png')

            dif03 = cv2.subtract(number, zero2)
            dif13 = cv2.subtract(number, one2)
            dif23 = cv2.subtract(number, two2)
            dif33 = cv2.subtract(number, three2)
            dif33dash = cv2.subtract(number, three2dash)
            dif33dashdash = cv2.subtract(number, three2dashdash)
            dif43 = cv2.subtract(number, four2)
            dif53 = cv2.subtract(number, five2)
            dif53dash = cv2.subtract(number, five2dash)
            dif63 = cv2.subtract(number, six2)
            dif63dash = cv2.subtract(number, six2dash)
            dif73 = cv2.subtract(number, seven2)
            dif83 = cv2.subtract(number, eight2)
            dif83dash = cv2.subtract(number, eight2dash)
            dif93 = cv2.subtract(number, nine2)

            b03, g03, r03 = cv2.split(dif03)
            b13, g13, r13 = cv2.split(dif13)
            b23, g23, r23 = cv2.split(dif23)
            b33, g33, r33 = cv2.split(dif33)
            b33d, g33d, r33d = cv2.split(dif33dash)
            b33dd, g33dd, r33dd = cv2.split(dif33dashdash)
            b43, g43, r43 = cv2.split(dif43)
            b53, g53, r53 = cv2.split(dif53)
            b53d, g53d, r53d = cv2.split(dif53dash)
            b63, g63, r63 = cv2.split(dif63)
            b63d, g63d, r63d = cv2.split(dif63dash)
            b73, g73, r73 = cv2.split(dif73)
            b83, g83, r83 = cv2.split(dif83)
            b83d, g83d, r83d = cv2.split(dif83dash)
            b93, g93, r93 = cv2.split(dif93)

            if cv2.countNonZero(b03) < 2 and cv2.countNonZero(g03) < 2 and cv2.countNonZero(r03) < 2:
                total = total + '0'
            elif cv2.countNonZero(b13) < 2 and cv2.countNonZero(g13) < 2 and cv2.countNonZero(r13) < 2:
                total = total + '1'
            elif cv2.countNonZero(b23) < 3 and cv2.countNonZero(g23) < 3 and cv2.countNonZero(r23) < 3:
                total = total + '2'
            elif cv2.countNonZero(b33) < 3 and cv2.countNonZero(g33) < 3 and cv2.countNonZero(r33) < 3:
                total = total + '3'
            elif cv2.countNonZero(b33d) < 2 and cv2.countNonZero(g33d) < 2 and cv2.countNonZero(r33d) < 2:
                total = total + '3'
            elif cv2.countNonZero(b33dd) < 1 and cv2.countNonZero(g33dd) < 1 and cv2.countNonZero(r33dd) < 1:
                total = total + '3'
            elif cv2.countNonZero(b43) < 2 and cv2.countNonZero(g43) < 2 and cv2.countNonZero(r43) < 2:
                total = total + '4'
            elif cv2.countNonZero(b53) < 5 and cv2.countNonZero(g53) < 5 and cv2.countNonZero(r53) < 5:
                total = total + '5'
            elif cv2.countNonZero(b53d) < 5 and cv2.countNonZero(g53d) < 5 and cv2.countNonZero(r53d) < 5:
                total = total + '5'
            elif cv2.countNonZero(b63) < 2 and cv2.countNonZero(g63) < 2 and cv2.countNonZero(r63) < 2:
                total = total + '6'
            elif cv2.countNonZero(b63d) < 2 and cv2.countNonZero(g63d) < 2 and cv2.countNonZero(r63d) < 2:
                total = total + '6'
            elif cv2.countNonZero(b73) < 2 and cv2.countNonZero(g73) < 2 and cv2.countNonZero(r73) < 2:
                total = total + '7'
            elif cv2.countNonZero(b83) < 7 and cv2.countNonZero(g83) < 7 and cv2.countNonZero(r83) < 7:
                total = total + '8'
            elif cv2.countNonZero(b83d) < 2 and cv2.countNonZero(g83d) < 2 and cv2.countNonZero(r83d) < 2:
                total = total + '8'
            elif cv2.countNonZero(b93) < 2 and cv2.countNonZero(g93) < 2 and cv2.countNonZero(r93) < 2:
                total = total + '9'






    height, width = threshold1.shape
    arr = []

    for i in range (0,width):
        count = 0
        for j in range (0,height):
            if threshold1[j,i] == 255:
                count = count +1
        if count == 0:
            arr.append(i)

    numar = np.array(arr)
    total1 = ':'

    for k in range (len(numar)-1):
        if numar[k+1]> numar[k]+1:
            add = 0
            minus = 0
            if numar[k]+9 > width:
                add = width-numar[k]
                minus = 9-add
            else:
                add = 9
            number = threshold1[0:height, numar[k] - minus:numar[k]+add]
            cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\temp.png', number)

            number1 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\temp.png')

            dif03 = cv2.subtract(number1, zero2)
            dif13 = cv2.subtract(number1, one2)
            dif23 = cv2.subtract(number1, two2)
            dif33 = cv2.subtract(number1, three2)
            dif33dash = cv2.subtract(number1, three2dash)
            dif33dashdash = cv2.subtract(number1, three2dashdash)
            dif43 = cv2.subtract(number1, four2)
            dif53 = cv2.subtract(number1, five2)
            dif53dash = cv2.subtract(number1, five2dash)
            dif63 = cv2.subtract(number1, six2)
            dif63dash = cv2.subtract(number1, six2dash)
            dif73 = cv2.subtract(number1, seven2)
            dif83 = cv2.subtract(number1, eight2)
            dif83dash = cv2.subtract(number1, eight2dash)
            dif93 = cv2.subtract(number1, nine2)

            b03, g03, r03 = cv2.split(dif03)
            b13, g13, r13 = cv2.split(dif13)
            b23, g23, r23 = cv2.split(dif23)
            b33, g33, r33 = cv2.split(dif33)
            b33d, g33d, r33d = cv2.split(dif33dash)
            b33dd, g33dd, r33dd = cv2.split(dif33dashdash)
            b43, g43, r43 = cv2.split(dif43)
            b53, g53, r53 = cv2.split(dif53)
            b53d, g53d, r53d = cv2.split(dif53dash)
            b63, g63, r63 = cv2.split(dif63)
            b63d, g63d, r63d = cv2.split(dif63dash)
            b73, g73, r73 = cv2.split(dif73)
            b83, g83, r83 = cv2.split(dif83)
            b83d, g83d, r83d = cv2.split(dif83dash)
            b93, g93, r93 = cv2.split(dif93)

            if cv2.countNonZero(b03) < 5 and cv2.countNonZero(g03) < 5 and cv2.countNonZero(r03) < 5:
                total1 = total1 + '0'
            elif cv2.countNonZero(b13) < 2 and cv2.countNonZero(g13) < 2 and cv2.countNonZero(r13) < 2:
                total1 = total1 + '1'
            elif cv2.countNonZero(b23) < 3 and cv2.countNonZero(g23) < 3 and cv2.countNonZero(r23) < 3:
                total1 = total1 + '2'
            elif cv2.countNonZero(b33) < 3 and cv2.countNonZero(g33) < 3 and cv2.countNonZero(r33) < 3:
                total1 = total1 + '3'
            elif cv2.countNonZero(b33d) < 2 and cv2.countNonZero(g33d) < 2 and cv2.countNonZero(r33d) < 2:
                total1 = total1 + '3'
            elif cv2.countNonZero(b33dd) < 1 and cv2.countNonZero(g33dd) < 1 and cv2.countNonZero(r33dd) < 1:
                total1 = total1 + '3'
            elif cv2.countNonZero(b43) < 2 and cv2.countNonZero(g43) < 2 and cv2.countNonZero(r43) < 2:
                total1 = total1 + '4'
            elif cv2.countNonZero(b53) < 2 and cv2.countNonZero(g53) < 2 and cv2.countNonZero(r53) < 2:
                total1 = total1 + '5'
            elif cv2.countNonZero(b53d) < 2 and cv2.countNonZero(g53d) < 2 and cv2.countNonZero(r53d) < 2:
                total1 = total1 + '5'
            elif cv2.countNonZero(b63) < 2 and cv2.countNonZero(g63) < 2 and cv2.countNonZero(r63) < 2:
                total1 = total1 + '6'
            elif cv2.countNonZero(b63d) < 2 and cv2.countNonZero(g63d) < 2 and cv2.countNonZero(r63d) < 2:
                total1 = total1 + '6'
            elif cv2.countNonZero(b73) < 2 and cv2.countNonZero(g73) < 2 and cv2.countNonZero(r73) < 2:
                total1 = total1 + '7'
            elif cv2.countNonZero(b83) < 2 and cv2.countNonZero(g83) < 2 and cv2.countNonZero(r83) < 2:
                total1 = total1 + '8'
            elif cv2.countNonZero(b83d) < 2 and cv2.countNonZero(g83d) < 2 and cv2.countNonZero(r83d) < 2:
                total1 = total1 + '8'
            elif cv2.countNonZero(b93) < 1 and cv2.countNonZero(g93) < 1 and cv2.countNonZero(r93) < 1:
                total1 = total1 + '9'







    height, width = threshold2.shape
    arr = []

    for i in range (0,width):
        count = 0
        for j in range (0,height):
            if threshold2[j,i] == 255:
                count = count +1
        if count == 0:
            arr.append(i)

    numar = np.array(arr)
    total2 = ':'

    for k in range (len(numar)-1):
        if numar[k+1]> numar[k]+1:
            add = 0
            minus = 0
            if numar[k]+9 > width:
                add = width-numar[k]
                minus = 9-add
            else:
                add = 9
            number = threshold2[0:height, numar[k] - minus:numar[k]+add]
            cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\temp.png', number)

            number2 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\temp.png')

            dif03 = cv2.subtract(number2, zero2)
            dif03dash = cv2.subtract(number2, zero2dash)
            dif13 = cv2.subtract(number2, one2)
            dif23 = cv2.subtract(number2, two2)
            dif23dash = cv2.subtract(number2, two2dash)
            dif33 = cv2.subtract(number2, three2)
            dif33dash = cv2.subtract(number2, three2dash)
            dif33dashdash = cv2.subtract(number2, three2dashdash)
            dif43 = cv2.subtract(number2, four2)
            dif53 = cv2.subtract(number2, five2)
            dif53dash = cv2.subtract(number2, five2dash)
            dif63 = cv2.subtract(number2, six2)
            dif63dash = cv2.subtract(number2, six2dash)
            dif73 = cv2.subtract(number2, seven2)
            dif73dash = cv2.subtract(number2, seven2dash)
            dif83 = cv2.subtract(number2, eight2)
            dif83dash = cv2.subtract(number2, eight2dash)
            dif93 = cv2.subtract(number2, nine2)

            b03, g03, r03 = cv2.split(dif03)
            b03d, g03d, r03d = cv2.split(dif03dash)
            b13, g13, r13 = cv2.split(dif13)
            b23, g23, r23 = cv2.split(dif23)
            b23d, g23d, r23d = cv2.split(dif23dash)
            b33, g33, r33 = cv2.split(dif33)
            b33d, g33d, r33d = cv2.split(dif33dash)
            b33dd, g33dd, r33dd = cv2.split(dif33dashdash)
            b43, g43, r43 = cv2.split(dif43)
            b53, g53, r53 = cv2.split(dif53)
            b53d, g53d, r53d = cv2.split(dif53dash)
            b63, g63, r63 = cv2.split(dif63)
            b63d, g63d, r63d = cv2.split(dif63dash)
            b73, g73, r73 = cv2.split(dif73)
            b73d, g73d, r73d = cv2.split(dif73dash)
            b83, g83, r83 = cv2.split(dif83)
            b83d, g83d, r83d = cv2.split(dif83dash)
            b93, g93, r93 = cv2.split(dif93)

            if cv2.countNonZero(b03) < 8 and cv2.countNonZero(g03) < 8 and cv2.countNonZero(r03) < 8:
                total2 = total2 + '0'
            elif cv2.countNonZero(b03d) < 4 and cv2.countNonZero(g03d) < 4 and cv2.countNonZero(r03d) < 4:
                total2 = total2 + '0'
            elif cv2.countNonZero(b13) < 8 and cv2.countNonZero(g13) < 8 and cv2.countNonZero(r13) < 8:
                total2 = total2 + '1'
            elif cv2.countNonZero(b23) < 4 and cv2.countNonZero(g23) < 4 and cv2.countNonZero(r23) < 4:
                total2 = total2 + '2'
            elif cv2.countNonZero(b23d) < 4 and cv2.countNonZero(g23d) < 4 and cv2.countNonZero(r23d) < 4:
                total2 = total2 + '2'
            elif cv2.countNonZero(b33) < 8 and cv2.countNonZero(g33) < 8 and cv2.countNonZero(r33) < 8:
                total2 = total2 + '3'
            elif cv2.countNonZero(b33d) < 8 and cv2.countNonZero(g33d) < 8 and cv2.countNonZero(r33d) < 8:
                total2 = total2 + '3'
            elif cv2.countNonZero(b33dd) < 8 and cv2.countNonZero(g33dd) < 8 and cv2.countNonZero(r33dd) < 8:
                total2 = total2 + '3'
            elif cv2.countNonZero(b43) < 4 and cv2.countNonZero(g43) < 4 and cv2.countNonZero(r43) < 4:
                total2 = total2 + '4'
            elif cv2.countNonZero(b53) < 8 and cv2.countNonZero(g53) < 8 and cv2.countNonZero(r53) < 8:
                total2 = total2 + '5'
            elif cv2.countNonZero(b53d) < 8 and cv2.countNonZero(g53d) < 8 and cv2.countNonZero(r53d) < 8:
                total2 = total2 + '5'
            elif cv2.countNonZero(b63) < 8 and cv2.countNonZero(g63) < 8 and cv2.countNonZero(r63) < 8:
                total2 = total2 + '6'
            elif cv2.countNonZero(b63d) < 4 and cv2.countNonZero(g63d) < 4 and cv2.countNonZero(r63d) < 4:
                total2 = total2 + '6'
            elif cv2.countNonZero(b73) < 8 and cv2.countNonZero(g73) < 8 and cv2.countNonZero(r73) < 48:
                total2 = total2 + '7'
            elif cv2.countNonZero(b73d) < 8 and cv2.countNonZero(g73d) < 8 and cv2.countNonZero(r73d) < 48:
                total2 = total2 + '7'
            elif cv2.countNonZero(b83) < 4 and cv2.countNonZero(g83) < 4 and cv2.countNonZero(r83) < 4:
                total2 = total2 + '8'
            elif cv2.countNonZero(b83d) < 4 and cv2.countNonZero(g83d) < 4 and cv2.countNonZero(r83d) < 4:
                total2 = total2 + '8'
            elif cv2.countNonZero(b93) < 4 and cv2.countNonZero(g93) < 4 and cv2.countNonZero(r93) < 4:
                total2 = total2 + '9'




    height, width = threshold3.shape
    arr = []

    for i in range (0,width):
        count = 0
        for j in range (0,height):
            if threshold3[j,i] == 255:
                count = count +1
        if count == 0:
            arr.append(i)

    numar = np.array(arr)
    total3 = ':'

    for k in range (len(numar)-1):
        if numar[k+1]> numar[k]+1:
            add = 0
            minus = 0
            if numar[k]+9 > width:
                add = width-numar[k]
                minus = 9-add
            else:
                add = 9
            number = threshold3[0:height, numar[k] - minus:numar[k]+add]
            cv2.imwrite(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\temp.png', number)

            number3 = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\save\temp.png')

            dif03 = cv2.subtract(number3, zero2)
            dif13 = cv2.subtract(number3, one2)
            dif23 = cv2.subtract(number3, two2)
            dif33 = cv2.subtract(number3, three2)
            dif33dash = cv2.subtract(number3, three2dash)
            dif33dashdash = cv2.subtract(number3, three2dashdash)
            dif43 = cv2.subtract(number3, four2)
            dif53 = cv2.subtract(number3, five2)
            dif53dash = cv2.subtract(number3, five2dash)
            dif63 = cv2.subtract(number3, six2)
            dif63dash = cv2.subtract(number3, six2dash)
            dif73 = cv2.subtract(number3, seven2)
            dif83 = cv2.subtract(number3, eight2)
            dif83dash = cv2.subtract(number3, eight2dash)
            dif93 = cv2.subtract(number3, nine2)

            b03, g03, r03 = cv2.split(dif03)
            b13, g13, r13 = cv2.split(dif13)
            b23, g23, r23 = cv2.split(dif23)
            b33, g33, r33 = cv2.split(dif33)
            b33d, g33d, r33d = cv2.split(dif33dash)
            b33dd, g33dd, r33dd = cv2.split(dif33dashdash)
            b43, g43, r43 = cv2.split(dif43)
            b53, g53, r53 = cv2.split(dif53)
            b53d, g53d, r53d = cv2.split(dif53dash)
            b63, g63, r63 = cv2.split(dif63)
            b63d, g63d, r63d = cv2.split(dif63dash)
            b73, g73, r73 = cv2.split(dif73)
            b83, g83, r83 = cv2.split(dif83)
            b83d, g83d, r83d = cv2.split(dif83dash)
            b93, g93, r93 = cv2.split(dif93)

            if cv2.countNonZero(b03) < 5 and cv2.countNonZero(g03) < 5 and cv2.countNonZero(r03) < 5:
                total3 = total3 + '0'
            elif cv2.countNonZero(b13) < 2 and cv2.countNonZero(g13) < 2 and cv2.countNonZero(r13) < 2:
                total3 = total3 + '1'
            elif cv2.countNonZero(b23) < 3 and cv2.countNonZero(g23) < 3 and cv2.countNonZero(r23) < 3:
                total3 = total3 + '2'
            elif cv2.countNonZero(b33) < 3 and cv2.countNonZero(g33) < 3 and cv2.countNonZero(r33) < 3:
                total3 = total3 + '3'
            elif cv2.countNonZero(b33d) < 2 and cv2.countNonZero(g33d) < 2 and cv2.countNonZero(r33d) < 2:
                total3 = total3 + '3'
            elif cv2.countNonZero(b33dd) < 1 and cv2.countNonZero(g33dd) < 1 and cv2.countNonZero(r33dd) < 1:
                total3 = total3 + '3'
            elif cv2.countNonZero(b43) < 2 and cv2.countNonZero(g43) < 2 and cv2.countNonZero(r43) < 2:
                total3 = total3 + '4'
            elif cv2.countNonZero(b53) < 2 and cv2.countNonZero(g53) < 2 and cv2.countNonZero(r53) < 2:
                total3 = total3 + '5'
            elif cv2.countNonZero(b53d) < 2 and cv2.countNonZero(g53d) < 2 and cv2.countNonZero(r53d) < 2:
                total3 = total3 + '5'
            elif cv2.countNonZero(b63) < 2 and cv2.countNonZero(g63) < 2 and cv2.countNonZero(r63) < 2:
                total3 = total3 + '6'
            elif cv2.countNonZero(b63d) < 2 and cv2.countNonZero(g63d) < 2 and cv2.countNonZero(r63d) < 2:
                total3 = total3 + '6'
            elif cv2.countNonZero(b73) < 2 and cv2.countNonZero(g73) < 2 and cv2.countNonZero(r73) < 2:
                total3 = total3 + '7'
            elif cv2.countNonZero(b83) < 2 and cv2.countNonZero(g83) < 2 and cv2.countNonZero(r83) < 2:
                total3 = total3 + '8'
            elif cv2.countNonZero(b83d) < 2 and cv2.countNonZero(g83d) < 2 and cv2.countNonZero(r83d) < 2:
                total3 = total3 + '8'
            elif cv2.countNonZero(b93) < 1 and cv2.countNonZero(g93) < 1 and cv2.countNonZero(r93) < 1:
                total3 = total3 + '9'

    check = cv2.imread(r'C:\Users\Leighton Waters\Desktop\WOWSC\League\SS\passivesave.png')

    difpassive = cv2.subtract(check, Passive)
    bp, gp, rp = cv2.split(difpassive)
    run = False

    if cv2.countNonZero(bp) < 1 and cv2.countNonZero(gp) < 1 and cv2.countNonZero(rp) < 1:
                run = True


    heightH, widthH = thresholdH.shape
    healthcount = 0
    manacount = 0

    for m in range(0, widthH):
        for n in range(heightH):
            if thresholdH [n,m] == 255:
                healthcount = healthcount+1
            if thresholdM [n,m] == 255:
                manacount = manacount+1


    return total1, total2, total3, total, CDfinal, s1, s2, s3 ,ult, run, healthcount, manacount



