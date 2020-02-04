## Video frame extraction
from glob import glob
import cv2
import sys

import time
import matplotlib.pyplot as plt

VIDS = glob("/home/thalo/Videos/*")
print(VIDS)
SAVE_PATH = '/home/thalo/Pictures/video_frames/'

"""Tune these three values to fit your dataset.
They will make the program collect more or fewer frames
based on blurriness and delta from the last captured frame.
The BLUR_THRESH determines what is automatically
filtered out. If it is too low, the program will consider
too many images to be blurry.
The SMUDGE_AMT determines how much smudge is applied
to an image while preprocessing it to find its
delta from the previously captured frame. This step
is necessary so that not every single pixel change
is considered significant when calculating the delta.
If this amount is too high, it will smudge an image
into a meaningless blob.
The DIFF_THRESH is the actual threshold of how different
the last saved frame has to be from [this] frame in order to
save [this] frame.
"""
BLUR_THRESH = 90
SMUDGE_AMT = 25
DIFF_THRESH = 25

if "win" in sys.platform:
    path_delimiter = "\\"
    VIDS = list(map(lambda vid: vid.replace("/", "\\"), VIDS))
else:
    path_delimiter = "/"

for vid in VIDS:
    count = 0
    sum_ = 0
    all_blur_metrics = []
    vidcap = cv2.VideoCapture(vid)
    success,image = vidcap.read()
    gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.GaussianBlur(gray1, (SMUDGE_AMT, SMUDGE_AMT), 0)
    # print(type(image))
    while success:
        blur_metric = cv2.Laplacian(image, cv2.CV_64F).var()
        all_blur_metrics.append(blur_metric)
    #     plt.imshow(image)
        sum_ += blur_metric
        if blur_metric > BLUR_THRESH:
            gray2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.GaussianBlur(gray2, (SMUDGE_AMT, SMUDGE_AMT), 0)
            delta = cv2.absdiff(gray1, gray2)
            thresh = cv2.threshold(delta, DIFF_THRESH, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None)

            ## Just looking...
            # print(thresh.sum())
            # plt.imshow(thresh)
            # plt.show()
            # time.sleep(1)
            if thresh.sum() > 0:
                gray1 = gray2
                vidname = vid[vid.rfind(path_delimiter):vid.rfind('.')-1]
                cv2.imwrite(SAVE_PATH + vidname + "frame{}.jpg".format(count), image) # save frame as JPG file
        else:
            print(blur_metric)
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1
    print(sum_ / count)
