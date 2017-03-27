import numpy as np
import cv2
import os
from math import floor
from math import ceil
import matplotlib.pyplot as plt


def img_zoom(img, K,piv_x,piv_y ):
	
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

	zoomed_img = np.ones((rows, cols, colors))
	
	for i in range(rows-ceil(2*K+1)):
		for j in range(cols-ceil(2*K+1)):
			x_cord = j / K
			y_cord = i / K
			
			b_x = int(floor(x_cord+1))
			a_x = int(floor(x_cord))
			d_y = int(floor(y_cord+1))
			a_y = int(floor(y_cord))

			L_b_x = b_x - x_cord
			L_a_x = x_cord - a_x
			L_d_y = d_y - y_cord
			L_a_y = y_cord - a_y
			
			zoomed_img[i, j, :] =255-  np.around(L_b_x * (L_d_y * new_img[a_y, a_x, :] + L_a_y * new_img[d_y, a_x, :]) + L_a_x * (L_d_y * new_img[a_y, b_x, :] + L_a_y * new_img[d_y, b_x, :]), 0)
			

	plt.subplot(121),plt.imshow(img),plt.title('input')
	plt.subplot(122),plt.imshow(zoomed_img),plt.title('output')
	plt.show()
	
	cv2.imwrite('zoomed_img',zoomed_img)
	
	return

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'rabbit.jpg')   

img=cv2.imread(filename , -1)	
img_zoom(img, 2.0, 200,200)  # parameters( image, scale, piv_x,piv_y)