import cv2
import numpy as np
img=cv2.imread("C:\\Users\\anand\\Pictures\\Liberty.jpg",0)
r,c=img.shape
print(r,c)
row=int(r/2)
col=int(c/2)
imff=cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
ims=np.fft.fftshift(imff)
mask=np.zeros((r,c,2),np.uint8)
mask[row-200:row+200,col-400:col+400]=1
#mask[:,:,:]=1
imss=ims*mask
print(imss.shape)
iffs=np.fft.ifftshift(imss)
ifm=np.fft.ifft2(iffs)
ima=cv2.magnitude(ifm[:,:,0],ifm[:,:,1])
#ima=20*np.log(np.abs(ifm))
#ima=255*ima/np.max(ima)
#ima=ima.astype(np.uint8)

#cv2.imshow("",ima)
#cv2.waitKey(0)
#cv2.destroyAllWindows()