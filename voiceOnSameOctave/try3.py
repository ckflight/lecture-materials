# blahhh

import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import fft
from pylab import *

fs, data = wavfile.read('440_sine.wav')
a = data
b = [(ele/2**8.)*2-1 for ele in a]
c = fft(b)
d = len(c)/2
k = arange(len(data))
T = len(data)/fs
print "sample time? is %s" %fs
frqLabel= k/T
print size(abs(c[:(d-1)])) 
print size(frqLabel)
plt.plot(frqLabel[:(d-1)], abs(c[:(d-1)]),'r')
plt.title('Frequency Spectrum of Voice')
plt.xlabel('change this later')
plt.ylabel('magnitude')
plt.show()

plt.plot(data)
plt.show()
