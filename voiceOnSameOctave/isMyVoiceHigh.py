# we're trying to figure out if my voice is actually higher than carly's voice

from pylab import *
from scipy.io import wavfile

sampFreq, snd = wavfile.read('440_sine.wav')

print snd.dtype

snd = snd/2.**15

print snd.shape

rate= 5060.0/ sampFreq
print rate

s1 = snd[:,0]

timeArray = arange(0, 5060.0, 1)
timeArray = timeArray/sampFreq
timeArray = timeArray*1000 # scales to ms
graph = figure()
graph = plot(timeArray, s1, color='k')
ylabel('Amplitude')
xlabel('Time (ms)')
show()


