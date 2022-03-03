import cv2
def collage(imag):
    vi=cv2.VideoCapture("C:\\Users\\anand\\Videos\\cheeta.mp4")
    fps=int(vi.get(cv2.CAP_PROP_FPS))
    w=int(vi.get(cv2.CAP_PROP_FRAME_WIDTH))
    h=int(vi.get(cv2.CAP_PROP_FRAME_HEIGHT))
    op=cv2.VideoWriter("C:\\Users\\anand\\Videos\\cheeta.avi",cv2.VideoWriter_fourcc('X','V','I','D'),fps,(w,h))
    while True:
        success,frame=vi.read()
        if success:
            frame[0:270,1180:1280]=imag
            frame=cv2.copyMakeBorder(frame,10,10,10,10,cv2.BORDER_CONSTANT,value=[255,0,0])
            cv2.imshow("Video",frame)
            op.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    vi.release()
    op.release()
    cv2.destroyAllWindows()

liberty=cv2.imread("C:\\Users\\anand\\Pictures\\Liberty.jpg",1)
statue=liberty[50:320,180:280]
collage(statue)