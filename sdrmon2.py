# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 04:28:19 2016

@author: lotter
Please look at baseline file required: Record basline for new device and fftbin size
Change directories to suite you file structure
"""

import time

import os

import numpy as np

import matplotlib.pyplot as plt

Fstart="350M"
Fstop="1G"
avg="1"
overlap="0"
fftbin="16"
gain="200"

cmd="rtl_power_fftw -B /home/lotter/sdr/baseline16.txt" +" -f "+Fstart+":"+Fstop+" -g "+gain+" -n "+avg+" -o "+overlap+" -b "+fftbin+" > /home/lotter/sdr/out.txt"




plt.ion()
my_dpi=96
fig = plt.figure(figsize=(1900/my_dpi, 1000/my_dpi), dpi=my_dpi)




os.system(cmd)
out=np.loadtxt("/home/lotter/sdr/out.txt", comments="#")
data=np.zeros([1,len(out)])
data[0,:]=out[:,1]

try:

    while True:
        ax = fig.add_subplot(211)
        ax.clear()
        plt.plot(out[:,0],out[:,1])
        plt.draw()
        os.system(cmd)
        out=np.loadtxt("/home/lotter/sdr/out.txt", comments="#")
        data=np.append(data,[out[:,1].T],axis=0)
        
        ay = fig.add_subplot(212)
        ay.clear()
        plt.imshow(data)
        plt.tight_layout()
        

except KeyboardInterrupt:

    print 'zapped!'
    print "saving"
    np.save("/home/lotter/sdr/data",[out[:,0],data])
    plt.savefig("/home/lotter/sdr/spectrum.png")
    



#os.system("rtl_power_fftw -f 100M:200M -o 80 -g 37 -n 10 -b 1024 > /home/lotter/sdr/temp/out.txt")

#

#

#out=np.loadtxt("/home/lotter/sdr/temp/out.txt", comments="#")

#

#plot(out[:,0],out[:,1])
