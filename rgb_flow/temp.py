import cv2
import numpy as np
import imageio
cap = cv2.VideoCapture("test.gif")

ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
images = []

# out = cv2.VideoWriter('output.avi', -1, 20.0, (224,224))

while(1):
    ret, frame2 = cap.read()
    if (ret == False):
        break
    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    
    flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

    cv2.imshow('frame2',rgb)
    images.append(rgb)
    # out.write(frame2)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    # elif k == ord('s'):
    #     cv2.imwrite('opticalfb.png',frame2)
    #     cv2.imwrite('opticalhsv.png',rgb)
    prvs = next
cap.release()
imageio.mimsave('output.gif', images)
cv2.destroyAllWindows() 