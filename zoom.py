import numpy as np
import cv2
import os
from math import floor
from math import ceil
import matplotlib.pyplot as plt

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'rabbit.jpg')

img=cv2.imread(filename , -1)
def img_interp(img, K,piv_x,piv_y ):
	
	rows, cols , colors= img.shape
	
	nrows=int(ceil(rows/K))
	ncols=int(ceil(cols/K))
	
	if piv_x < (0+ceil(cols/(2*K))):
		piv_x=0+ceil(cols/(2*K))
		
	elif piv_x > (cols-floor(cols/(2*K))):
		piv_x=cols-floor(cols/(2*K))
		
	if piv_y < (0+ceil(rows/(2*K))):
		piv_y=0+ceil(rows/(2*K))
		
	elif piv_y > (rows-floor(rows/(2*K))):
		piv_y=rows-floor(rows/(2*K))	
		
	
	Ax,Ay= ceil(piv_x-(ncols/2)), ceil(piv_y-(nrows/2))
	Bx= floor(piv_x+(ncols/2))
	Dy=floor(piv_y+(nrows/2))
	
	new_img = np.ones((nrows, ncols, colors))
	new_img=img[Ay:Dy, Ax:Bx]

	enlarged_img = np.ones((rows, cols, colors))
	
	for i in range(rows-ceil(2*K+1)):
		for j in range(cols-ceil(2*K+1)):
			x_coord = j / K
			y_coord = i / K
			
			xc = int(floor(x_coord+1))
			xf = int(floor(x_coord))
			yc = int(floor(y_coord+1))
			yf = int(floor(y_coord))

			W_xc = xc - x_coord
			W_xf = x_coord - xf
			W_yc = yc - y_coord
			W_yf = y_coord - yf
			
			enlarged_img[i, j, :] =255-  np.around(W_xc * (W_yc * new_img[yf, xf, :] + W_yf * new_img[yc, xf, :]) + W_xf * (W_yc * new_img[yf, xc, :] + W_yf * new_img[yc, xc, :]), 0)
			

	plt.subplot(122),plt.imshow(img),plt.title('input')
	plt.subplot(121),plt.imshow(enlarged_img),plt.title('output')
	plt.show()
	
	return
		
img_interp(img, 10.0, 700,500)