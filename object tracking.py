import cv2

v1=cv2.VideoCapture("C:/Users/anand/Videos/car.mp4")
trac=cv2.TrackerMOSSE_create()
s,img=v1.read()
bbx=cv2.selectROI("Track",img,False)
trac.init(img,bbx)
while True:
    timer=cv2.getTickCount()
    suc,img1=v1.read()
    txt=cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img1,str(int(txt)),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    if suc==True:
        cv2.imshow("Hello",img1)
    key=cv2.waitKey(1)
    if key==ord('q'):
        cv2.destroyAllWindows()
        break

    