# https://pythonprogramming.net/loading-video-python-opencv-tutorial/?completed=/loading-images-python-opencv-tutorial/

import cv2
import numpy as np

# 0 will be the first camera, 1 will be the second camera.
cap = cv2.VideoCapture(0)

# fourcc means four character codec & use XVID codec to write the video.
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Therefore out file video writes to output.avi with codec of 20 fps at resolution 640x480.
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while True:
# So while there is a return captured picture frame,
# the while true loop will continue to read the picture frame.
    ret, frame = cap.read()

    # cvt means convert color in the frame from Blue Green Red to Gray.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # And then writes the frame.
    out.write(frame)

    #cv2.imshow('frame_cam0', frame)
    cv2.imshow('frame', gray)
# Since this is a infinite loop as the camera will always truly return a frame,
# will therefore require the user to enter a CTRL-C or q to break the loop.
# But if user press & hold the spacebar key, then the image will continue to refresh
# frame by frame.
    if cv2.waitKey(0) & 0xFF == ord('q'):    # this line requires user to press q to quit.
    #if cv2.waitKey(0):    # this line requires user to press any key to quit.
        break

# Below tells the camera capturing to release.
cap.release()
# Below tells the saving of the file to stop and release.
out.release()
# And then need to let tell cv2 to close the window frames.
cv2.destroyAllWindows()

# Note that the above code code though could save the video file,
# but macos & windows 10 could not play the movie file. Not sure why.
