# pypiv

## Simple PIV script

I built this to understand Particle Image Velocimetry (PIV) and how commercial softwares calculate velocity fields from particle images. 

Theses scripts use numpy library to evaluate the correlation using bidimensional fast fourrier transfert. 

Run in this order:
	1. image.py: script to generate double frame of particle images with a analytical velocity fields (set dx, dy)
	2. piv.py: calculate the correlation in a selected window to evaluate displacement (should retrieve dx, dy!)
