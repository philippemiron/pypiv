import random, os
from math import exp, ceil
# fake image generator

# function to calculate intensity
# in function of distance from
# the middle of the particle
def intensity(I0, x, y, x0, y0, dp):
  return I0 * exp( (-(x-x0)**2. - (y-y0)**2.)/(1./8. * dp**2.0) )

# parameters
image_size = [1280, 800] # pixels
bits = 12
file1 = "B00001.dat"
file2 = "B00002.dat"
ppp = 0.05 # particle per pixels
N = int(ppp * image_size[0]*image_size[1]) #number of particles
rp = 1.8 # particle radius in pixel
dx = 20 #pixel displacement x
dy = 5 #pixel displacement y

# all black image
im = [[0 for i in range(image_size[1])] for j in range(image_size[0])]
im2 = [[0 for i in range(image_size[1])] for j in range(image_size[0])]

# initial seed
random.seed(os.urandom(1))

# gen particles
for i in range(0, N):
	px = int(image_size[0]*random.random())
	py = int(image_size[1]*random.random())
	intensity_max = int(2**bits*random.random())
	if intensity_max < 500:	
		intensity_max = 500

	for j in range(-int(ceil(rp)), int(ceil(rp))+1):
		for k in range(-int(ceil(rp)), int(ceil(rp))+1):
			pxj = px + j
			pyj = py + k
			if (pxj > 0 and pxj < image_size[0] and pyj > 0 and pyj < image_size[1]):
				im[pxj][pyj] += intensity(intensity_max, pxj, pyj, px, py, 2.0*rp)
				pxj += dx
				pyj += dy
				if (pxj > 0 and pxj < image_size[0] and pyj > 0 and pyj < image_size[1]):
					im2[pxj][pyj] += intensity(intensity_max, pxj, pyj, px+dx, py+dy, 2.0*rp)

file = open(file1, "w")		
file.write('TITLE = "image"\n')
file.write('VARIABLES = "x", "y", "intensity"\n')
file.write('ZONE T="Frame 1" I=')
file.write(str(image_size[0]) + ', J=' + str(image_size[1]) + ', F=POINT\n')
for j in range(0, image_size[1]):
	for i in range(0, image_size[0]):
		file.write(str(i) + " " + str(j) + " " + str(im[i][j]) + "\n")
file.close()

file = open(file2, "w")		
file.write('TITLE = "image"\n')
file.write('VARIABLES = "x", "y", "intensity"\n')
file.write('ZONE T="Frame 1" I=')
file.write(str(image_size[0]) + ', J=' + str(image_size[1]) + ', F=POINT\n')
for j in range(0, image_size[1]):
	for i in range(0, image_size[0]):
		file.write(str(i) + " " + str(j) + " " + str(im2[i][j]) + "\n")
file.close()
