#  created by @szymonSadowski
import cv2

# # * load trained data from file
trained_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# # * img part
# img = cv2.imread("bruno.jpg")
# grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # * face detection part
# get_face = trained_data.detectMultiScale(grey_img)

# # * draw Coordinates
# for (x, y, w, h) in get_face:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow("Face Detector", web_cam)
# cv2.waitKey()


# ! Webcam face detector part

web_cam = cv2.VideoCapture(0)

while True:
    ret, frame = web_cam.read()

    grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    get_face = trained_data.detectMultiScale(grey_img)

    for (x, y, w, h) in get_face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0))

    cv2.imshow("Face Detector - video/form", frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break
#  if code is completed
web_cam.release()
msg = "Completed"
print(msg)
