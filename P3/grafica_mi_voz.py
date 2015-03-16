
#Ojo faltan los labels :)
from pylab import *
import scikits.audiolab as audiolab
from scipy.fftpack import fft, fftfreq

audio = 'alvis.wav'
a = audiolab.sndfile(audio, 'read')
tmp = a.read_frames(1e4)
float_tmp = a.read_frames(1e4, dtype = float32)
#Graficamos la senal de audio
plot(tmp[:])
title('Mi hermosa Voz')
savefig('mi_voz.png')
close()
