import cv2
vi=cv2.VideoCapture("C:\\Users\\anand\\Videos\\car.mp4")
fb=cv2.createBackgroundSubtractorMOG2()
while(1):
    r,frame=vi.read()
    fram=fb.apply(frame)
    cv2.imshow("",fram)
    k=cv2.waitKey(30)
    if k==ord('q'):
        break
vi.release()
cv2.destroyAllWindows()