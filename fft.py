import cv2
import numpy as np
img=cv2.imread("C:\\Users\\anand\\Pictures\\Liberty.jpg")
imgb=img[:,:,0]
ff=cv2.dft(np.float32(imgb),flags=cv2.DFT_COMPLEX_OUTPUT)
ff1=np.fft.fftshift(ff)
fftcomplex=ff1[:,:,0]+1j*ff1[:,:,1]
ffabs=np.abs(fftcomplex)+1
ffl=20*np.log(ffabs)
ffn=255*ffl/np.max(ffl)
ffn=ffn.astype(np.uint8)
cv2.imshow("",ffn)
cv2.waitKey(0)
cv2.destroyAllWindows()
