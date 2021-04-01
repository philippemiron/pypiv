# pypiv

## Simple PIV script

I built this to understand Particle Image Velocimetry (PIV) and how commercial softwares calculate velocity fields from particle images. Theses scripts use numpy library to evaluate the correlation using bidimensional fast fourrier transfert. 

## How does it work?
 1. image.py: generate double frame images of particles with a analytical velocity fields (set dx, dy)
 2. piv.py: retrieve a window from both images and calculate the correlation (and the its peak) to evaluate the displacement (should retrieve dx, dy!)