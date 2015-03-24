
from pylab import *
import scikits.audiolab as audiolab
from scipy.fftpack import fft, fftfreq


#Cargamos el audio
input_signal, sampling_rate, enc = audiolab.wavread("alvis.wav") #entra por parametro el archivo grabado en script de C
time_array = np.arange(0, len(input_signal)/float(sampling_rate), 1/float(sampling_rate)) #establece el conteo del tiempo

#Transformada de Fourier
n = len(input_signal) #puntos por medicion
f = 100.0 #float(sampling_rate) # frecuencia Hz
dt = 1 / (f * n/32 ) #32 datos por frecuencia
fft_x = fft(input_signal)/(n)# FFT Normalized
freq = fftfreq(n,dt) # Recuperamos las frecuencias

#Grafica frecuencias
plot(freq,abs(fft_x),'m')
xlim(-20000,20000)
savefig('mivoz_fft.png')
close()

#Mostrar en pantalla el armonico principal
print 'El armonico principal se encuentra en: ' + str(freq[argmax(abs(fft_x))]) + 'Hz'
