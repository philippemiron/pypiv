from numpy import fft, conj, asarray, unravel_index
import matplotlib.pyplot as plt

class image:
  def __init__(self, filename, x, y, bits):
    self.file = filename
    self.dim_x = x
    self.dim_y = y
    self.bits = bits
    # 2d array [x][y]
    self.data = self.parse_image()

  def parse_image(self):
    im = [[0 for i in range(self.dim_y)] for j in range(self.dim_x)]
    file = open(self.file, "r")
    for i in range(3):
      file.readline()
    # loop y first for tp
    for j in range(self.dim_y):
      for i in range(self.dim_x):
        line = file.readline().split()
        im[i][j] = int(float(line[2]))
    file.close()
    return im
  
  def __str__(self):
    return ""

class windows:
  def __init__(self, im, size, index):
    self.size = size
    self.i = index[0]*size
    self.j = index[1]*size
    self.image = im
    self.signal = self.get_window_signal()

  def get_window_signal(self):
    sig2d = [[0 for i in range(self.size)] for j in range(self.size)]
    for k in range(0, self.size):
      for l in range(0, self.size):
        sig2d[k][l] = self.image.data[int(self.i+k)][int(self.j+l)]
    return sig2d

  def export(self):
    file = open("window-" + self.image.file[5] + ".dat", "w")
    file.write('TITLE = "window"\n')
    file.write('VARIABLES = "x", "y", "intensity"\n')
    file.write('ZONE T="Frame 1" I=')
    file.write(str(self.size) + ', J=' + str(self.size) + ', F=POINT\n')
    for i in range(0, self.size):
      for j in range(0, self.size):
        file.write(str(i) + " " + str(j) + " " + str(self.signal[i][j]) + "\n")
    file.close()

class correlation:
  def __init__(self, w1, w2):
    self.size = w1.size
    self.s1 = asarray(w1.signal)
    self.s2 = asarray(w2.signal)
    self.corr = fft.ifft2((fft.fft2(self.s1) * conj(fft.fft2(self.s2)))).real
    self.corr = fft.ifftshift(self.corr)

  def fix_boundary(self):
    for i in range(0, self.size):
      self.corr[i][0] = 0
      self.corr[i][self.size-1] = 0
    for j in range(0, self.size):
      self.corr[0][j] = 0
      self.corr[self.size-1][j] = 0

  def export(self):
    file = open("correlation.dat", "w")
    file.write('TITLE = "correlation"\n')
    file.write('VARIABLES = "x", "y", "correlation"\n')
    file.write('ZONE T="Frame 1" I=')
    file.write(str(self.size) + ', J=' + str(self.size) + ', F=POINT\n')
    for i in range(0, self.size):
      for j in range(0, self.size):
        file.write(str(i-self.size/2) + " " + str(j-self.size/2) + " " + str(self.corr[i][j]) + "\n")
    file.close()

# parameters
pixel_x = 1280
pixel_y = 800
bits = 12
file1 = "B00001.dat"
file2 = "B00002.dat"

# parsing image file
img1 = image(file1, pixel_x, pixel_y, bits)
img2 = image(file2, pixel_x, pixel_y, bits)

# get one window
# in this example the "velocity" is
# constant across the whole image
a = windows(img1, 64, [1, 1])
b = windows(img2, 64, [1, 1])
a.export()
b.export()

# calculate correlation
c = correlation(b, a)
c.export()

# simple plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
peak = unravel_index(c.corr.argmax(), c.corr.shape)
ax.pcolormesh(c.corr.T)
ax.set_title('Displacement estimated by dx=%d dy=%d.' % (peak[0]-a.size/2, peak[1]-a.size/2))
ax.arrow(a.size/2, a.size/2, peak[0]-a.size/2, peak[1]-a.size/2, color='red', linewidth=2)
plt.show()