'''
    openCV stands for Open Source Computer Vision.
    Available in different programming languages as well.

'''

import cv2
# import numpy

# imread(path, how do you want to read image ?)
# as it is then pass 1(rgb) 3 bands
# black and white 0(greyscale) 2 bands
# -1 (transparency)
img = cv2.imread("galaxy.jpeg", 0)

# python stores images as numpy array let's check
print(type(img)) #<class 'numpy.ndarray'>

print(img) 

# shape and dimensions of the image depends upon how we have imported the image
print(img.shape) #(411, 616)
print(img.ndim) #2  because we have passed 0 as parameter

# We can resize array according to us python will manipulate the values
# resize() takes to 2 args first one img that we have imported
# second one resized image shape
resized_img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2)) #instaed of tuple can use any other dt by tuple is recommended


# can write image
# it will create and resized image at saves in cwd with given name
cv2.imwrite("galaxy_resized.jpeg", resized_img)

# displays the image
# 1st parameter name of the window that will appear
cv2.imshow("Galaxy", resized_img)
#how to close the window if put 0
#then pressing anykey will closes the window or can pass time in ms
cv2.waitKey(0) 
# what to do after waitKey() method executed
cv2.destroyAllWindows()


