from PIL import ImageGrab
import cv2
import numpy as np
import pytesseract

def Screen_Grab():
    screenshot = ImageGrab.grab()
    screenshot = screenshot.convert('L')

    Health = screenshot.crop([751, 1053, 1062, 1054])
    Health = Health.point(lambda p: 255 if p < 40 else 0)

    Mana = screenshot.crop([750, 1068, 1064, 1069])
    Mana = Mana.point(lambda p: 255 if p < 40 else 0)

    A1_level = screenshot.crop([787, 1028, 826, 1034])
    A1_level = A1_level.point(lambda p: 255 if p > 100 else 0)
    A2_level = screenshot.crop([837, 1028, 877, 1034])
    A2_level = A2_level.point(lambda p: 255 if p > 100 else 0)
    A3_level = screenshot.crop([887, 1028, 927, 1034])
    A3_level = A3_level.point(lambda p: 255 if p > 100 else 0)
    Ult_level = screenshot.crop([937, 1028, 978, 1034])
    Ult_level = Ult_level.point(lambda p: 255 if p > 100 else 0)

    screenshot = screenshot.point(lambda p: 255 if p > 150 else 0)

    A1 = screenshot.crop([787, 985, 826, 1020])
    A2 = screenshot.crop([837, 985, 877, 1020])
    A3 = screenshot.crop([887, 985, 926, 1020])
    Ult = screenshot.crop([937, 985, 976, 1020])

    S1 = screenshot.crop([995,985,1025,1010])
    S2 = screenshot.crop([1034,985,1064,1010])

    return A1, A2, A3, Ult, A1_level, A2_level, A3_level, Ult_level, S1, S2, Health, Mana

def Data_Parse():

    A1, A2, A3, Ult, A1_level, A2_level, A3_level, Ult_level, S1, S2, Health, Mana = Screen_Grab()

    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

    try:
        result = np.array(A1)
        result = cv2.GaussianBlur(result, (3, 3), 0)
        result = 255 - result
        A1_val = pytesseract.image_to_string(result, lang='eng', config='--psm 6')

        A1_val = int(''.join([i for i in A1_val if i.isdigit()]))
    except:
        A1_val = 'Ready'
    try:
        result = np.array(A2)
        result = cv2.GaussianBlur(result, (3, 3), 0)
        result = 255 - result
        A2_val = pytesseract.image_to_string(result, lang='eng', config='--psm 6')
        if isinstance(A2_val, str):
            A2_val = int(''.join([i for i in A2_val if i.isdigit()]))
    except:
        A2_val = 'Ready'
    try:
        result = np.array(A3)
        result = cv2.GaussianBlur(result, (3, 3), 0)
        result = 255 - result
        A3_val = pytesseract.image_to_string(result, lang='eng', config='--psm 6')
        if isinstance(A3_val, str):
            A3_val = int(''.join([i for i in A3_val if i.isdigit()]))
    except:
        A3_val = 'Ready'
    try:
        result = np.array(Ult)
        result = cv2.GaussianBlur(result, (1, 1), 0)
        result = 255 - result
        Ult_val = pytesseract.image_to_string(result, lang='eng', config='--psm 6')
        if isinstance(Ult_val, str):
            Ult_val = int(''.join([i for i in Ult_val if i.isdigit()]))
    except:
        Ult_val = 'Ready'
    try:
        result = np.array(S1)
        result = cv2.GaussianBlur(result, (1, 1), 0)
        result = 255 - result
        S1_val = pytesseract.image_to_string(result, lang='eng', config='--psm 6')
        if isinstance(S1_val, str):
            S1_val = int(''.join([i for i in S1_val if i.isdigit()]))
    except:
        S1_val = 'Ready'
    try:
        result = np.array(S2)
        result = cv2.GaussianBlur(result, (1, 1), 0)
        result = 255 - result
        S2_val = pytesseract.image_to_string(result, lang='eng', config='--psm 6')
        if isinstance(S2_val, str):
            S2_val = int(''.join([i for i in S2_val if i.isdigit()]))
    except:
        S2_val = 'Ready'

    try:
        H_val = list(np.array(Health)[0]).index(255)
    except:
        H_val = len(np.array(Health)[0])
    try:
        M_val = list(np.array(Mana)[0]).index(255)
    except:
        M_val = len(np.array(Mana)[0])
    Health_percent = H_val / len(np.array(Health)[0])
    Mana_percent = M_val / len(np.array(Mana)[0])

    A1_level_val = len(cv2.findContours(np.array(A1_level), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0])
    A2_level_val = len(cv2.findContours(np.array(A2_level), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0])
    A3_level_val = len(cv2.findContours(np.array(A3_level), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0])
    Ult_level_val = len(cv2.findContours(np.array(Ult_level), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0])

    return A1_val, A2_val, A3_val, Ult_val, S1_val, S2_val, A1_level_val, A2_level_val, A3_level_val, Ult_level_val, Health_percent, Mana_percent
