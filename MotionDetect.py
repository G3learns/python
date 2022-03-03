import cv2
import numpy as np
img1=cv2.imread("C:\\Users\\anand\\Videos\\Captures\\lip45.jpg")
img2=cv2.imread("C:\\Users\\anand\\Videos\\Captures\\lip46.jpg")
r,c=200,200
i1r=img1[0:200,200:400,2]
i2r=img2[0:200,200:400,2]
i1df=cv2.dft(i1r.astype(np.float32),flags=cv2.DFT_COMPLEX_OUTPUT)
i2df=cv2.dft(i2r.astype(np.float32),flags=cv2.DFT_COMPLEX_OUTPUT)
i1ffs=np.fft.fftshift(i1df)
i2ffs=np.fft.fftshift(i2df)
i1c=i1ffs[:,:,0]+1j*i1ffs[:,:,1]
i2c=i2ffs[:,:,0]+1j*i2ffs[:,:,1]
i1a=np.abs(i1c)
i2a=np.abs(i2c)
totalabs=i1a*i2a
print(totalabs)
#i_r=((i1c.real*i2c.real)+(i1c.imag*i2c.imag))/totalabs
#i_i=((i1c.imag*i2c.real)+(i1c.real*i2c.imag))/totalabs
i_r=((np.real(i1c)*np.real(i2c))+(np.imag(i1c)*np.imag(i2c)))/totalabs
i_i=((np.imag(i1c)*np.real(i2c))+(np.real(i1c)*np.imag(i2c)))/totalabs
i_c=i_r+1j*i_i
iif=np.fft.ifft2(i_c)
iif=np.abs(iif)
max_id=[0,0]
max_val=0
for j in range(0,c):
    for i in range(0,r):
        if iif[i,j] > max_val:
            max_val=iif[i,j]
            max_id=[i,j]
shiftx=r-max_id[0]
shifty=c-max_id[1]
print(shiftx,shifty)
cv2.rectangle(img1,(0,0),(r-shiftx,c-shifty),(0,255,0),10)
cv2.rectangle(img2,(0,0),(r-shiftx,c-shifty),(0,255,0),10)
ih=cv2.hconcat([img1,img2])
cv2.imshow("",ih)
cv2.waitKey(0)
cv2.destroyAllWindows()