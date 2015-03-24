

from pylab import *
import scikits.audiolab as audiolab
from scipy.fftpack import fft, fftfreq

input_signal, sampling_rate, enc = audiolab.wavread("alvis.wav") #entra por parametro el archivo grabado en script de C
time_array = np.arange(0, len(input_signal)/float(sampling_rate), 1/float(sampling_rate)) #establece el conteo del tiempo


fig = plt.figure() #grafica la voz
plt.plot(time_array[0:len(input_signal)], input_signal[0:len(input_signal)])
plt.title("Grafica Amplitud vs tiempo", fontsize=20)
plt.xlabel("Tiempo (s)", fontsize=15)
plt.xlim(0.0,max(time_array))
plt.ylim(-0.25,0.25)
plt.ylabel("Amplitud", fontsize=15)
plt.savefig("mi_voz.png")
