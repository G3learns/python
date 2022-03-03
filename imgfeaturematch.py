import cv2
import numpy as np
img1=cv2.imread("C:\\Users\\anand\\Pictures\\box.png")
imgbw1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2=cv2.imread("C:\\Users\\anand\\Pictures\\boxinimage.png")
imgbw2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#Feature point and Feature descriptor SIFT
sf1=cv2.xfeatures2d.SIFT_create()
sf2=cv2.xfeatures2d.SIFT_create()
kp1,desc1=sf1.detectAndCompute(imgbw1,None)
kp2,desc2=sf2.detectAndCompute(imgbw2,None)
# =============================================================================
# #feature point and descriptor identification ORB
# orb1=cv2.ORB_create()
# kp1,desc1=orb1.detectAndCompute(imgbw1,None)
# orb2=cv2.ORB_create()
# kp2,desc2=orb2.detectAndCompute(imgbw2,None)
# # =============================================================================
# =============================================================================
# #feature match using Brute force
# bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
# matches=bf.match(desc1,desc2)
# matches=sorted(matches,key=lambda x:x.distance)
# img3=cv2.drawMatches(img1,kp1,img2,kp2,matches[:50],img3,flags=2)
# =============================================================================
# =============================================================================
# #Feature Matching using BFMatcher and KNNMatch
# bf=cv2.BFMatcher()
# matches=bf.knnMatch(desc1,desc2,k=2)
# good=[]
# for m,n in matches:
#     if m.distance<0.75*n.distance:
#         good.append(m)
# img3=cv2.drawMatches(img1,kp1,img2,kp2,good,img3,flags=2)
# 
# =============================================================================
#Feature Matching using FLANN MATCHER
# =============================================================================
# FLANN_MATCH_KDTREE=0
# index_param=dict(algorithm=FLANN_MATCH_KDTREE,trees=5)
# search_param=dict(checks=50)
# fl=cv2.FlannBasedMatcher(index_param,search_param)
# matches=fl.knnMatch(desc1,desc2,k=2)
# matchmask=[[0,0] for x in range(len(matches))]
# for i,(m,n) in enumerate(matches):
#     if m.distance<0.7*n.distance:
#         matchmask[i]=[1,0]
# img3=cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,img3,(255,0,0),(0,255,0),matchmask,flags=0)
# =============================================================================
FLANN_MATCH_KDTREE=0
index_param=dict(algorithm=FLANN_MATCH_KDTREE,trees=5)
search_param=dict(checks=50)
fl=cv2.FlannBasedMatcher(index_param,search_param)
matches=fl.knnMatch(desc1,desc2,k=2)
good=[]
for m,n in matches:
    if m.distance<0.7*n.distance:
        good.append(m)
if len(good)>10:
    src_pt=np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dst_pt=np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    M,mask=cv2.findHomography(src_pt,dst_pt,cv2.RANSAC,5.0)
    matchmask=mask.ravel().tolist()
        
#cv2.imshow("",img3)
#cv2.waitKey(0)
#cv2.destroyAllWindows()