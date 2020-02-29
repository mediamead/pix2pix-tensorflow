# https://gist.githubusercontent.com/keithweaver/70df4922fec74ea87405b83840b45d57/raw/80e9aef3ab3862a67c8379b947748973cc7eb757/split-video-by-frame.py

'''
Using OpenCV takes a mp4 video and produces a number of images.

Requirements
----
You require OpenCV 3.2 to be installed.

Run
----
Open the main.py and edit the path to the video. Then run:
$ python main.py

Which will produce a folder called data with the images. There will be 2000+ images for example.mp4.
'''
import cv2
import numpy as np
import os
import sys

assert(len(sys.argv) == 3)
video_file = sys.argv[1]
frames_dir = sys.argv[2]

# Playing video from file:
cap = cv2.VideoCapture(video_file)

try:
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)
except OSError:
    print ('Error: Creating %s directory' % frames_dir)

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = "%s\\frame%d.jpg" % (frames_dir, currentFrame)
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()