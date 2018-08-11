import cv2
import numpy as np

# 0 will be the first camera, 1 will be the second camera.
cap = cv2.VideoCapture(0)

while True:
# So while there is a return captured picture frame,
# the while true loop will continue to read the picture frame.
    ret, frame = cap.read()

    # cvt means convert color in the frame from Blue Green Red to Gray.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame_cam0', frame)
    cv2.imshow('frame_gray', gray)
# Since this is a infinite loop as the camera will always truly return a frame,
# will therefore require the user to enter a CTRL-C or q to break the loop.
# But if user press & hold the spacebar key, then the image will continue to refresh
# frame by frame.
    #if cv2.waitKey(0) & 0xFF == ord('q'):    # this line requires user to press q to quit.
    if cv2.waitKey(0):    # this line requires user to press any key to quit.
        break
# Below tells the camera capturing to release.
# And then need to let tell cv2 to close the window frames.
cap.release()
cv2.destroyAllWindows()
