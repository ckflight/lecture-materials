# blahhh
from __future__ import division
import scipy.io.wavfile as wav
import pylab as pl
import numpy as np

def voiceAnalyze(rate,data):
    rate, data = wav.read('rudi.wav')
    print rate
    print "datatatatat === %s" %data.T[0]

    something = np.abs(np.fft.fft(data.T[0]))**2
    timeStep = 1/8000
    freqs = np.fft.fftfreq(data.size, timeStep)
    idx = np.argsort(freqs)
    pl.figure()
    pl.plot(freqs, something)
    print max(something)
    pl.show()  

if __name__ == "__main__":
    rudiRate, rudiData = wav.read('rudi.wav') 
    #for item in rudiData:
    #    print rudiData
    tomRate, tomData = wav.read('tom.wav')
    voiceAnalyze(rudiRate, rudiData)
    voiceAnalyze(tomRate, tomData)
