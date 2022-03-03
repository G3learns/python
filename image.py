import cv2
from matplotlib import pyplot as plt

im=cv2.imread('C:\\Users\\anand\\Pictures\\images.jfif',0)
cv2.namedWindow("Taj Mahal",cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("Taj Mahal",im)
cv2.imwrite('C:\\Users\\anand\\Pictures\\taj.jpg',im)
cv2.waitKey(0)
cv2.destroyAllWindows()