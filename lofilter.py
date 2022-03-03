import cv2
import numpy as np

def imagefilter(imgb):
    #######Hamming Filter#####################
    r=50
    ham=np.hamming(600)[:,None]
    hammat=np.sqrt(np.dot(ham,ham.T))**r
    ###########################################
    fft=cv2.dft(imgb.astype(np.float32),flags=cv2.DFT_COMPLEX_OUTPUT)
    ffts=np.fft.fftshift(fft)
    com=ffts[:,:,0]*1j+ffts[:,:,1]
    #comi=np.abs(com)
    fil=com*hammat
    ############################################
    ffil=np.fft.fftshift(fil)
    invf=np.fft.ifft2(ffil)
    invabs=np.abs(invf)
    invabs=20*np.log(invabs)
    invabs=255*invabs/invabs.max()
    invabs=invabs.astype(np.uint8)
    return invabs
img=cv2.imread("C:\\Users\\anand\\Pictures\\Liberty.jpg")
imgb=img[0:600,0:600,0]
imgg=img[0:600,0:600,1]
imgr=img[0:600,0:600,2]
imgfb=imagefilter(imgb)
imgfg=imagefilter(imgg)
imgfr=imagefilter(imgr)
imgf=cv2.merge([imgfb,imgfg,imgfr])
cv2.imshow("",imgf)
cv2.waitKey(0)
cv2.destroyAllWindows()
