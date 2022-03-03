import numpy
from PIL import Image
import cv2

img=numpy.zeros((512,512,3),numpy.uint8)
img=cv2.line(img,(0,0),(511,511),(255,0,0),5)
img=cv2.rectangle(img,(0,0),(511,511),(0,255,255),3)
img=cv2.circle(img,(255,255),255,(0,255,0),6)
cv2.imshow("Hello",img)
cv2.waitKey(0)
cv2.destroyAllWindows()