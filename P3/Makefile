all: mi_voz.png mivoz_fft.png alvis.wav

mi_voz.png: alvis.wav grafica_mi_voz.py
	python grafica_mi_voz.py

mivoz_fft.png: alvis.wav fft_de_mi_voz.py
	python fft_de_mi_voz.py

alvis.wav: a.out
	./a.out

a.out: grabar_mi_nombre.c
	cc grabar_mi_nombre.c

clean:
	rm -f *png *.wav *.out
