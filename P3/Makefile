all: mi_voz.png mivoz_fft.png

mi_voz.png: alvis.wav
	python grafica_mi_voz.py

mivoz_fft.png: alvis.wav
	python fft_de_mi_voz.py

clean:
	rm -f *png