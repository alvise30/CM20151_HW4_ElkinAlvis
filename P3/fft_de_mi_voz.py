
from pylab import *
import scikits.audiolab as audiolab
from scipy.fftpack import fft, fftfreq

#Funcion principal
def arm_principal(fft_x):
    d = abs(fft_x)
    temp = 0
    for element in d:
        if element > temp:
            temp = element    
    
    for i in range(10000):
        if abs(fft_x[i]) == temp:
            print 'A ' + str(freq[i]) + 'Hz se encuentra el armonico principal'       
            break

#Cargamos el audio
audio = 'prueba.wav'
a = audiolab.sndfile(audio, 'read')
tmp = a.read_frames(1e4)
float_tmp = a.read_frames(1e4, dtype = float32)

#Transformada de Fourier
n = 10000 # number of point in the whole interval
f = 1/3.16 #  frequency in Hz
dt = 1 / (f * n/4 ) #Entre 4 aun no se por q
t = linspace( 0, (n-1)*dt, n) 
y = tmp

#Grafica frecuencias
fft_x = fft(y)/n# FFT Normalized
freq = fftfreq(n,dt) # Recuperamos las frecuencias
plot(freq,abs(fft_x[:]),'m')
savefig('mivoz_fft.png')
close()

#Mostrar en pantalla el armonico principal
arm_principal(fft_x)
