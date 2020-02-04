# custom_annotation_tool
Simple image labeling tool

## Requirements
* OpenCV-Python
* Matplotlib

## Use

Use <code>video_frame_extraction.py</code> by throwing a bunch of video files into a folder and changing line 9 to match that path. Change line 11 to point to a folder where you would like to save the resulting image files. You may tweak lines 30-32 as you see fit. Changing line 30 to 0 to ignore the blurriness of a video frame and save all frames regardless of blurriness. Line 31 determines how much smudge is applied to an image while preprocessing it to find its delta from the previously captured frame. This step is necessary so that not every single pixel change is considered significant when calculating the delta. If this amount is too high, it will smudge an image into a meaningless blob. Line 32 is the actual threshold of how different
the last saved frame has to be from the next frame in order to save the next frame.

Change <code>predefined_classes.txt</code> to have each of your classes on a separate line (without spaces or special characters other than "_" and "-").

Use <code>custom_annotation_tool.py</code> by changing line 16 to the location of <code>predefined_classes.txt</code>. Then change line 18 to point to a folder where you would like to save the resulting annotations (in the form of a bunch of subfolders). You may make line 19 larger or smaller as you wish. This only affects your annotation process, not the actual sizes of any saved images. Change line 20 to 0 to ignore blurriness during annotation, or tweak it as you see fit. Lines 21-23 must point to where your image files are located (usually matching line 8 in <code>video_frame_extraction.py</code>). If you add or remove file extensions in these lines, then also modify lines 183-185 to reflect these changes.
