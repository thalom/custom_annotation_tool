#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import matplotlib.pyplot as plt
import cv2
import os
import sys
import shutil
from collections import OrderedDict
from glob import glob

print(os.path.abspath(os.path.curdir))
# Define these classes in a separate config file:
CLASSES_FILE = "C:\\Users\\Thalo\\Development\\VenvMl\\predefined_classes.txt"
KEYS = "q w e r t y u i o p a s d f g h j k l z x c v b n m"
BASE_PATH = "C:\\Users\\Thalo\\Development\\machinel_a"
IMG_SIZE = (500, 500)
BLUR_THRESH = 100
JPG_PATH = "../machinel_a/*.jpg"
JPEG_PATH = "../machinel_a/*.jpeg"
PNG_PATH = "../machinel_a/*.png"
BLUR_DIR_NAME = "blurry"

with open(CLASSES_FILE) as classes_file:
    classes_list = classes_file.read().split()
print(classes_list)
keys = KEYS.split()
print(keys)
map_ = OrderedDict(zip(keys, classes_list))
print("\n", map_, len(map_), sep="\n")

def press(event):
    while True:
        if event.key == (keys[0]):  # if key 'q' is pressed
            ans = keys[0]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[1]):
            ans = keys[1]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[2]):
            ans = keys[2]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[3]):
            ans = keys[3]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[4]):
            ans = keys[4]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[5]):
            ans = keys[5]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[6]):
            ans = keys[6]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[7]):
            ans = keys[7]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[8]):
            ans = keys[8]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[9]):
            ans = keys[9]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[10]):
            ans = keys[10]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[11]):
            ans = keys[11]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[12]):
            ans = keys[12]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[13]):
            ans = keys[13]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[14]):
            ans = keys[14]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[15]):
            ans = keys[15]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[16]):
            ans = keys[16]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[17]):
            ans = keys[17]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[18]):
            ans = keys[18]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[19]):
            ans = keys[19]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[20]):
            ans = keys[20]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[21]):
            ans = keys[21]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[22]):
            ans = keys[22]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[23]):
            ans = keys[23]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[24]):
            ans = keys[24]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == (keys[25]):
            ans = keys[25]
            cmd.append(ans)
            plt.close()
            break
        elif event.key == "backspace":
            cmd.append("back")
            plt.close()
            break
        elif event.key == "escape":
            cmd.append("skip")
            plt.close()
            break
        else:
            # print(event.key)
            continue

## Main Part

base_path = BASE_PATH
img_size = IMG_SIZE
blur_threshold = BLUR_THRESH
paths = glob(JPG_PATH)
paths.extend(glob(JPEG_PATH))
paths.extend(glob(PNG_PATH))
print(len(paths), "remaining images...")
if "win" in sys.platform:
    path_delimiter = "\\"
    paths = list(map(lambda path: path.replace("/", "\\"), paths))
else:
    path_delimiter = "/"

i = -1
went_back = False
while i < len(paths):
    if not went_back:
        i += 1
    else:
        i -= 1
        went_back = False
    img = cv2.resize(cv2.imread(paths[i]), img_size, interpolation=cv2.INTER_AREA)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray_img, cv2.CV_64F).var()
    if laplacian < blur_threshold:
        destination = base_path + path_delimiter + BLUR_DIR_NAME + paths[i][paths[i].rfind(path_delimiter):]
    #     print(paths[i], destination)
        if not os.path.exists(destination[: destination.rfind(path_delimiter)]):
            os.mkdir(base_path + path_delimiter + BLUR_DIR_NAME)

        # os.system('{} {} {}'.format(command, paths[i], destination))
        try:
            shutil.move(paths[i], destination)
            print("{} had a Laplacian variance of {:.3}".format(paths[i], laplacian))
            print("moved from {} to {}".format(paths[i], destination))
        except Exception as e:
            print(e)
        continue
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    fig = plt.figure(figsize=(10, 6))
    plt.imshow(img, origin="upper")
    plt.title(paths[i])
    left, width = img_size[0], .5
    bottom, height = .25, img_size[1] / len(map_)
    right = left + width
    top = bottom + height
    for j in range(len(map_)):
        text = "Press '{}' for {}".format(keys[j], map_[keys[j]])
        plt.text(right, bottom + (height * j), text,
                horizontalalignment='left',
                verticalalignment='top')

    cmd = []
    fig.canvas.mpl_connect('key_press_event', press)
    plt.show()

    if cmd[-1] != "skip" and cmd[-1] != "back":
        destination = base_path + path_delimiter + map_[cmd[-1]] + paths[i][paths[i].rfind(path_delimiter):]
    #     print(paths[i], destination)
        if not os.path.exists(destination[: destination.rfind(path_delimiter)]):
            os.mkdir(base_path + path_delimiter + map_[cmd[-1]])

        try:
            shutil.move(paths[i], destination)
            print("moved from {} to {}".format(paths[i], destination))
            paths[i] = destination
        except Exception as e:
            print(e)
    elif cmd[-1] == "back":
        went_back = True
    plt.close()
