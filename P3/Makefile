all: mi_voz.png mivoz_fft.png

mi_voz.png: prueba.wav
	python grafica_mi_voz.py

mivoz_fft.png: prueba.wav
	python fft_de_mi_voz.py

prueba.wav: a.out
	./a.out

a.out:
	cc grabar_mi_nombre.c

clean:
	rm -f *png prueba.wav *.out