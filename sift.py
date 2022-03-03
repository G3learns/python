import cv2
img=cv2.imread("C:\\Users\\anand\\Pictures\\chessboard.jpg")
imgbw=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# =============================================================================
# SIFT Scale Invariant Feature Transform
# sf=cv2.xfeatures2d.SIFT_create()
# kp,desc=sf.detectAndCompute(imgbw,None)
# =============================================================================
# =============================================================================
# SURF Speeded Up Robust Feature
# surf=cv2.xfeatures2d.SURF_create()
# kp,desc=surf.detectAndCompute(imgbw,None)
# =============================================================================
# =============================================================================
## FAST Feature from Accelerated Segment Test
#fs=cv2.FastFeatureDetector_create()
#fs.setNonmaxSuppression(False)
#kp=fs.detect(imgbw,None)
# =============================================================================
# =============================================================================
# #BRIEF fetaure Detector
# kp=cv2.xfeatures2d_StarDetector.detect(imgbw,None)
# kp,dsc=cv2.xfeatures2d_BriefDescriptorExtractor.compute(imgbw,kp)
# =============================================================================
#ORB feature detector
orb=cv2.ORB_create()
kp=orb.detect(imgbw,None)
kp,desc=orb.compute(imgbw,kp)
cv2.drawKeypoints(img,kp,img)
cv2.imshow("",img)
cv2.waitKey(0)
cv2.destroyAllWindows()