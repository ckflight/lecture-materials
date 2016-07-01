# me vs. rudi
# the final showdown.
# tckf october 2015
from __future__ import division
import numpy as np
import pylab as pl
import scipy as sp

def plotSpectrum(y,Fs):
    # plots a single sided amplitude spectrum of y(y)

    n = len(y)
    k = np.arange(n)
    T = n/Fs
    frq = k/T
    frq = frq[range(int(n/2))]
    
    Y = sp.fft(y)/n
    Y = Y[range(int(n/2))]
    
    pl.plot(frq,abs(Y), 'r') # plotting the spectrum
    pl.xlabel('Freq (Hz)')
    pl.ylabel('|Y(freq)|')

if __name__ == "__main__":
    Fs = 150.0 #sampling rate
    Ts = 1.0/Fs #sampling interval
    t = np.arange(0,1,Ts) # time vector
    ff = 5.5
    y = np.sin(2*np.pi*ff*t)
    pl.figure()
    pl.subplot(2,1,1)
    pl.plot(t,y)
    pl.xlabel('time')
    pl.ylabel('amplitude')
    pl.subplot(2,1,2)
    plotSpectrum(y,Fs)
    pl.show()

    
