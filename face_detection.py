import cv2

# load the Cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# load the image
# grayscale images gives high accuracy in face detection
# as compared to colorful images
img = cv2.imread('photo.jpg') #colorful image to give the output

# grayscale to detect face
# convert one image to another form
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# less value of scaleFactor the more high accuracy
# scaleFactor tells how much size to decrease in next search
# 1.05 means decrease size by 5%
# 1.5 means decrease size by 50% which is not accurate at all
faces = face_cascade.detectMultiScale(gray_img, 
scaleFactor=1.1,
minNeighbors=5)

# using loop because there could be many faces in the image
for x, y, w, h in faces:
    # rectangle(image in which you wanna draw rect,
    #  ( starting points top-left ), ( ending point bottom-right ),
    #  ( color of rect in rgb ), width of rect ) 
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)

# print(faces)
# print(type(faces))

# can resize if want
# temp = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))

cv2.imshow("sds", img)
cv2.waitKey(0)
