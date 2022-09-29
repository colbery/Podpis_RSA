from functools import partial
from os.path import abspath, dirname
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import scipy.stats
import wave
import struct
import math
import numpy as np
import os.path
from PIL import Image
from sys import path
path.insert(1, dirname(dirname(abspath(__file__))))
from scipy.io import wavfile

import datetime
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def entropy1(labels, base=None):
  value,counts = np.unique(labels, return_counts=True)
  norm_counts = counts / counts.sum()
  base = 2 if base is None else base
  return -(norm_counts * np.log(norm_counts)/np.log(base)).sum()

def wyswietlSbox(sbox, border=True):
    temp = ''
    if border:
        # kolumny
        temp += '     '
        for i in range(16):
            temp += '%02x' % i + ' '
        temp += '\n'

        for i in range(52):
            temp += '-'
        temp += '\n'

    # wiersze
    for i in range(16):
        if border:
            temp += '%02x' % i + ' | '

        # liczby
        for j in range(16):
            temp += '%02x' % sbox[16*i+j] + ' '
        temp += '\n'

    return temp.upper()
	
sbox1 = []
sbox2 = []
sbox3 = []
sbox4 = []
sbox5 = []
sbox6 = []
sbox7 = []
sbox8 = []
sbox9 = []
sbox10 = []
sbox11 = []
sbox12 = []
sbox13 = []
sbox14 = []
sbox15 = []
sbox16 = []
sbox17 = []
sbox18 = []
sbox19 = []
sbox20 = []
sbox21 = []
sbox22 = []
sbox23 = []
sbox24 = []
sbox25 = []
sbox26 = []
sbox27 = []
sbox28 = []
sbox29 = []
sbox30 = []
sbox31 = []
sbox32 = []
sbox33 = []
sbox34 = []
sbox35 = []
sbox36 = []
sbox37 = []
sbox38 = []
sbox39 = []
sbox40 = []
sbox41 = []
sbox42 = []
sbox43 = []
sbox44 = []
sbox45 = []
sbox46 = []
sbox47 = []
sbox48 = []
sbox49 = []
sbox50 = []

inputMatrix = []
outputMatrix = []
outputMultiple = []

def trngVector(audio):
    waveFile = wave.open(audio, 'r')
    print(waveFile.getparams())
    length = waveFile.getnframes()
    forLen = 50000
    # print(length)
    samples_count = 0
    now = datetime.datetime.now()
    random.seed(now)
    wektor = []
    for i in range(0,forLen):
        waveData = waveFile.readframes(1)
        
        test = waveFile.readframes(1)
        number = test[0]
        if(i < 150):
            wektor.append(number)
        if 0 <= number <= 256:
            if(len(inputMatrix) != 45000):
                inputMatrix.append(number)
            if(len(sbox1) != 256):
                samples_count = samples_count+1
                sbox1.append(number)
            if(len(sbox1) == 256 and len(sbox2) != 256):
                sbox2.append(number)
            if(len(sbox2) == 256 and len(sbox3) != 256):
                sbox3.append(number)
            if(len(sbox3) == 256 and len(sbox4) != 256):
                sbox4.append(number)
            if(len(sbox4) == 256 and len(sbox5) != 256):
                sbox5.append(number)
            if(len(sbox5) == 256 and len(sbox6) != 256):
                sbox6.append(number)
            if(len(sbox6) == 256 and len(sbox7) != 256):
                sbox7.append(number)
            if(len(sbox7) == 256 and len(sbox8) != 256):
                sbox8.append(number)
            if(len(sbox8) == 256 and len(sbox9) != 256):
                sbox9.append(number)
            if(len(sbox9) == 256 and len(sbox10) != 256):
                sbox10.append(number)
            if(len(sbox10) == 256 and len(sbox11) != 256):
                sbox11.append(number)
            if(len(sbox11) == 256 and len(sbox12) != 256):
                sbox12.append(number)
            if(len(sbox12) == 256 and len(sbox13) != 256):
                sbox13.append(number)
            if(len(sbox13) == 256 and len(sbox14) != 256):
                sbox14.append(number)
            if(len(sbox14) == 256 and len(sbox15) != 256):
                sbox15.append(number)
            if(len(sbox15) == 256 and len(sbox16) != 256):
                sbox16.append(number)
            if(len(sbox16) == 256 and len(sbox17) != 256):
                sbox17.append(number)
            if(len(sbox17) == 256 and len(sbox18) != 256):
                sbox18.append(number)
            if(len(sbox18) == 256 and len(sbox19) != 256):
                sbox19.append(number)
            if(len(sbox19) == 256 and len(sbox20) != 256):
                sbox20.append(number)
            if(len(sbox20) == 256 and len(sbox21) != 256):
                sbox21.append(number)
            if(len(sbox21) == 256 and len(sbox22) != 256):
                sbox22.append(number)
            if(len(sbox22) == 256 and len(sbox23) != 256):
                sbox23.append(number)
            if(len(sbox23) == 256 and len(sbox24) != 256):
                sbox24.append(number)
            if(len(sbox24) == 256 and len(sbox25) != 256):
                sbox25.append(number)
            if(len(sbox25) == 256 and len(sbox26) != 256):
                sbox26.append(number)
            if(len(sbox26) == 256 and len(sbox27) != 256):
                sbox27.append(number)
            if(len(sbox27) == 256 and len(sbox28) != 256):
                sbox28.append(number)
            if(len(sbox28) == 256 and len(sbox29) != 256):
                sbox29.append(number)
            if(len(sbox29) == 256 and len(sbox30) != 256):
                sbox30.append(number)
            if(len(sbox30) == 256 and len(sbox31) != 256):
                sbox31.append(number)
            if(len(sbox31) == 256 and len(sbox32) != 256):
                sbox32.append(number)
            if(len(sbox32) == 256 and len(sbox33) != 256):
                sbox33.append(number)
            if(len(sbox33) == 256 and len(sbox34) != 256):
                sbox34.append(number)
            if(len(sbox34) == 256 and len(sbox35) != 256):
                sbox35.append(number)
            if(len(sbox35) == 256 and len(sbox36) != 256):
                sbox36.append(number)
            if(len(sbox36) == 256 and len(sbox37) != 256):
                sbox37.append(number)
            if(len(sbox37) == 256 and len(sbox38) != 256):
                sbox38.append(number)
            if(len(sbox38) == 256 and len(sbox39) != 256):
                sbox39.append(number)
            if(len(sbox39) == 256 and len(sbox40) != 256):
                sbox40.append(number)
            if(len(sbox40) == 256 and len(sbox41) != 256):
                sbox41.append(number)
            if(len(sbox41) == 256 and len(sbox42) != 256):
                sbox42.append(number)
            if(len(sbox42) == 256 and len(sbox43) != 256):
                sbox43.append(number)
            if(len(sbox43) == 256 and len(sbox44) != 256):
                sbox44.append(number)
            if(len(sbox44) == 256 and len(sbox45) != 256):
                sbox45.append(number)
            if(len(sbox45) == 256 and len(sbox46) != 256):
                sbox46.append(number)
            if(len(sbox46) == 256 and len(sbox47) != 256):
                sbox47.append(number)
            if(len(sbox47) == 256 and len(sbox48) != 256):
                sbox48.append(number)
            if(len(sbox48) == 256 and len(sbox49) != 256):
                sbox49.append(number)
            if(len(sbox49) == 256 and len(sbox50) != 256):
                sbox50.append(number)

    for i in range(0,1):
        outputMatrix.append(sbox1[16*random.randint(0, 15)+random.randint(0, 15)])

    for i in range(0,900):
        outputMultiple.append(sbox1[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox2[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox3[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox4[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox5[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox6[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox7[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox8[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox9[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox10[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox11[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox12[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox13[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox14[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox15[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox16[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox17[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox18[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox19[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox20[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox21[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox22[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox23[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox24[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox25[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox26[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox27[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox28[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox29[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox30[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox31[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox32[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox33[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox34[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox35[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox36[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox37[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox38[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox39[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox40[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox41[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox42[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox43[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox44[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox45[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox46[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox47[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox48[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox49[16*random.randint(0, 15)+random.randint(0, 15)])
        outputMultiple.append(sbox50[16*random.randint(0, 15)+random.randint(0, 15)])
       
    return outputMultiple