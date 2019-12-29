## Video frame extraction
from glob import glob
import cv2
import sys

VIDS = glob("C:\\Users\\Thalo\\Videos\\*.mp4")
print(VIDS)
SAVE_PATH = 'C:\\Users\\Thalo\\Development\\machinel_a\\'
BLUR_THRESH = 90

if "win" in sys.platform:
    path_delimiter = "\\"
    VIDS = list(map(lambda vid: vid.replace("/", "\\"), VIDS))
else:
    path_delimiter = "/"

for vid in VIDS:
    count = 0
    sum_ = 0
    vidcap = cv2.VideoCapture(vid)
    success,image = vidcap.read()
    # print(type(image))
    while success:
        blur_metric = cv2.Laplacian(image, cv2.CV_64F).var()
    #     plt.imshow(image)
        sum_ += blur_metric
        if blur_metric > BLUR_THRESH:
            # plt.imshow(image)
            vidname = vid[vid.rfind(path_delimiter):vid.rfind('.')-1]
            cv2.imwrite(SAVE_PATH + vidname + "frame%d.jpg" % count, image) # save frame as JPG file
        else:
            print(blur_metric)
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1
    print(sum_ / count)
