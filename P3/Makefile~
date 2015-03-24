all: mi_voz.png mivoz_fft.png prueba.wav

mi_voz.png: prueba.wav grafica_mi_voz.py
	python grafica_mi_voz.py

mivoz_fft.png: prueba.wav fft_de_mi_voz.py
	python fft_de_mi_voz.py

prueba.wav: a.out
	./a.out

a.out: grabar_mi_nombre.c
	cc grabar_mi_nombre.c

clean:
	rm -f *png prueba.wav *.out