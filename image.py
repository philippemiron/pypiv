import random, os

# fake image generator
pixel_x = 1280
pixel_y = 800
bits = 12
file1 = "B00001.dat"
file2 = "B00002.dat"
ppp = 0.03 # particle per pixels
N = int(ppp*pixel_x*pixel_y)
rp = 2 # particle radius in pixel
dx = 15 #pixel displacement x
dy = 5 #pixel displacement y

# all black image
im = [[0 for i in range(pixel_y)] for j in range(pixel_x)]
im2 = [[0 for i in range(pixel_y)] for j in range(pixel_x)]

# initial seed
random.seed(os.urandom(1))

# gen particles
for i in range(0, N):
	px = int(pixel_x*random.random())
	py = int(pixel_y*random.random())
	intensity = int(2**bits*random.random())
	if intensity < 500:	
		intensity = 500

	for j in range(-rp, rp+1):
		for k in range(-rp, rp+1):
			pxj = px + j
			pyj = py + k
			if (pxj > 0 and pxj < pixel_x and pyj > 0 and pyj < pixel_y):
				im[pxj][pyj] = intensity
				pxj += dx
				pyj += dy
				if (pxj > 0 and pxj < pixel_x and pyj > 0 and pyj < pixel_y):
					im2[pxj][pyj] = intensity

file = open(file1, "w")		
file.write('TITLE = "image"\n')
file.write('VARIABLES = "x", "y", "intensity"\n')
file.write('ZONE T="Frame 1" I=')
file.write(str(pixel_x) + ', J=' + str(pixel_y) + ', F=POINT\n')
for j in range(0, pixel_y):
	for i in range(0, pixel_x):
		file.write(str(i) + " " + str(j) + " " + str(im[i][j]) + "\n")
file.close()

file = open(file2, "w")		
file.write('TITLE = "image"\n')
file.write('VARIABLES = "x", "y", "intensity"\n')
file.write('ZONE T="Frame 1" I=')
file.write(str(pixel_x) + ', J=' + str(pixel_y) + ', F=POINT\n')
for j in range(0, pixel_y):
	for i in range(0, pixel_x):
		file.write(str(i) + " " + str(j) + " " + str(im2[i][j]) + "\n")
file.close()
