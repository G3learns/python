import cv2
import numpy as np
def colorchange(low,high,imag1):    
    hsv_img=cv2.cvtColor(imag1,cv2.COLOR_BGR2HSV)
    bw_img=cv2.cvtColor(imag1,cv2.COLOR_BGR2GRAY)
    red_mask=cv2.inRange(hsv_img,low,high)
    bw_mask=cv2.bitwise_not(red_mask)
    red_img=cv2.bitwise_and(imag1,imag1,mask=red_mask)
    bw_imag=cv2.bitwise_and(bw_img,bw_img,mask=bw_mask)
    fin=cv2.add(red_img,cv2.cvtColor(bw_imag,cv2.COLOR_GRAY2BGR))
    return fin 
    
vi=cv2.VideoCapture("C:\\Users\\anand\\Videos\\lipstick.mp4")
low=np.array([161, 155, 84])
high=np.array([179, 255, 255])
while True:
    success,frame=vi.read()
    if success==True:
        chg_frame=colorchange(low,high,frame)
        cv2.imshow("Lipstick Video",chg_frame)
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
    else:
        break
vi.release()
cv2.destroyAllWindows()