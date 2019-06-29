import cv2
import numpy as np 
import time

capture_video = cv2.VideoCapture("./video_test_3.mp4")

time.sleep(1)
count = 0
background = 0

for i in range(60):
    return_val, background = capture_video.read()
    
    if return_val == False:
        continue
background = np.flip(background, axis=1) # flipping of the frame

# We are reading from video
while(capture_video.isOpened()):
    return_val, img = capture_video.read()
    if not return_val:
        break
    count = count + 1
    img = np.flip(img, axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # setting the lower and upper range for mask1 
    lower_red = np.array([100, 40, 40])   # RGB     
    upper_red = np.array([100, 255, 255]) 
    mask1 = cv2.inRange(hsv, lower_red, upper_red) 
    # setting the lower and upper range for mask2  
    
    # The cv2.inRange function expects three arguments: 
    # the first is the image  were we are going to perform
    # color detection, the second is the lower  limit of 
    # the color you want to detect, and the third argument
    # is the upper  limit of the color you want to detect.
    lower_red = np.array([155, 40, 40]) 
    upper_red = np.array([180, 255, 255]) 
    mask2 = cv2.inRange(hsv, lower_red, upper_red) 

    mask1 = mask1 + mask2

    # Refining the mask corresponding to the detected red color 
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), # morphologyEx(src, dst, op, kernel)
                                         np.uint8), iterations = 2) 
    mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations = 1) 
    mask2 = cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("INVISIBLE MAN", final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break


