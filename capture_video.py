import cv2, time

# have to pass index of video camera or can pass a video file as well
video = cv2.VideoCapture(0) #0 is the camera index

countFrames = 1

while True:        
    countFrames += 1
    # check is bool [whether video is ON or not]
    # frame is the nparray [frame values captured from camera]
    check, frame = video.read()

    # frame is nothing but just a image we can do everthing thatever we do with images
    # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.rectangle(gray_frame, (10,10), (50,50), (255,0,0), 2)

    cv2.imshow("My Webcam", frame)

    # waitKey(1) returns key that's been pressed
    key = cv2.waitKey(1)

    # print(frame)
    if key == ord('q'):
        break


print(countFrames)
cv2.destroyAllWindows()
video.release()