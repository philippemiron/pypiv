#pypiv

###Simple PIV script

I built this to understand Particle Image Velocimetry (PIV) and how commercial softwares calculate velocity fields from particle images. 

Theses scripts use numpy library to evaluate the correlation using bidimensional fast fourrier transfert. 

- image.py: script to generate double frame of particles images with a analytical velocity fields
- piv.py: calculate the correlation in a fixed size window of the images to evaluate displacement


