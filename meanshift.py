import cv2
import numpy as np
#get the mouse location
refpoint=[]
drawing=False
def draw_rec(event,x,y,flags,param):
    global refpoint,drawing
    if event==cv2.EVENT_LBUTTONDOWN:
        #refpoint.clear()
        refpoint.append((x,y))
    elif event==cv2.EVENT_LBUTTONUP:
        refpoint.append((x,y))
        print(refpoint[0],refpoint[1])
        cv2.rectangle(frame,refpoint[0],refpoint[1],(0,255,0),2)
vi=cv2.VideoCapture("C:\\Users\\anand\\Videos\\cone.mp4")
suc,frame=vi.read()
cv2.namedWindow("Read pointer")
cv2.setMouseCallback("Read pointer",draw_rec)
cv2.imshow("Read pointer",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
c=min((refpoint[0][0],refpoint[1][0]))
w=max((refpoint[0][0],refpoint[1][0]))-c
r=min((refpoint[0][1],refpoint[1][1]))
h=max((refpoint[0][1],refpoint[1][1]))-r

#c,r,w,h=10,240,180,100
print(c,r,w,h)
topframe=(c,r,w,h)
roi=frame[r:r+h,c:c+w]
rhsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
#hsv=cv2.inRange(rhsv,np.array((5., 40., 90.)),np.array((40., 255., 255.)))
hsv=cv2.inRange(rhsv,np.array((0., 60.,32.)), np.array((180.,255.,255.)))
hist=cv2.calcHist([roi],[0],hsv,[180],[0,180])
cv2.normalize(hist,hist,0,255,cv2.NORM_MINMAX)
term_crit=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,1)
while(1):
    suc,frame=vi.read()
    if suc==0:
        break
    ihsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    bp=cv2.calcBackProject([ihsv],[0],hist,[0,180],1)
# =============================================================================
# #Mean shift
#     sat,topframe=cv2.meanShift(bp,topframe,term_crit)
#     c,r,w,h=topframe
#     img2=cv2.rectangle(frame,(c,r),(c+w,r+h),255,2)
# =============================================================================
#CAM Continous Adaptive Meanshift
    sat,topframe=cv2.CamShift(bp,top    frame,term_crit)
    pts=cv2.boxPoints(sat)
    pts=np.int0(pts)
    img2=cv2.polylines(frame,[pts],True,255,2)
    cv2.imshow("",img2)
    k = cv2.waitKey(60) & 0xff
    if k == 27:
        break
#print(hsv[50,100])
#cv2.imwrite("C:\\Users\\anand\\Videos\\rhsv.jpeg",rhsv)

#cv2.imshow("",norm)
cv2.waitKey(0)
cv2.destroyAllWindows()