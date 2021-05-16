import cv2
import glob
import os

# gives you list of all files with given extension 
sample_images = glob.glob('*.jpg')

for sample in sample_images:
    img = cv2.imread(sample, 0)
    resized_img = cv2.resize(img, (50, 50))
    cv2.imshow(sample , resized_img)
    cv2.waitKey(300)
    cv2.destroyAllWindows()
    cv2.imwrite("newly_resized_"+sample, resized_img)
    print(sample)