import cv2
import time
import glob
from emailing import send_email
import os

video = cv2.VideoCapture(0) #0 for main camera and 1 if using a secondary camera like usb or phone camera connected with laptop

# check1, frame1 = video.read()
# time.sleep(1)

# check2, frame2 = video.read()
# time.sleep(1)

# check3, frame3 = video.read()

# print(frame3)

# cv2.imwrite('app8-email-webcam-detection/image.png',frame3)

# Video capturing
time.sleep(1)
first_frame = None
status_list = []
count = 1

def clean_folder():
  images = glob.glob("app8-email-webcam-detection/images/*.png")
  for image in images:
    os.remove(image)

while True:
  status = 0
  check, frame = video.read()
  gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  gray_frame_gau = cv2.GaussianBlur(gray_frame,(21,21),0)

  if first_frame is None:
    first_frame = gray_frame_gau

  delta_frame = cv2.absdiff(first_frame,gray_frame_gau) #gives difference between 1st and current frame

  thresh_frame = cv2.threshold(delta_frame, 40, 255, cv2.THRESH_BINARY)[1]  #this is for converting all the color whose bgr is above/equal 30 to 255,so that we can get absolute black and white color

  dil_frame = cv2.dilate(thresh_frame,None,iterations=2)
  # cv2.imshow("My video",dil_frame)

  contours, check = cv2.findContours(dil_frame,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  for contour in contours:
    if cv2.contourArea(contour) < 5000:
      continue
    x,y,w,h = cv2.boundingRect(contour)
    rectangle =cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)

    if rectangle.any():
      status = 1
      cv2.imwrite(f"app8-email-webcam-detection/images/{count}.png", frame)
      count+=1
      all_images = glob.glob("app8-email-webcam-detection/images/*.png")
      index = int(len(all_images)/2)
      image_with_obj = all_images[index]

  status_list.append(status)
  status_list = status_list[-2:]

  if status_list[0] == 1 and status_list[1] == 0:
    send_email(image_with_obj)
    clean_folder()
  
  cv2.imshow("Video", frame)

  key = cv2.waitKey(1) #0 waits infinitely(freezes the vdo), 1 means 1ms wait for key press dring capturing each frame.
  if key == ord("q"):  #ord gives ascii of 'q'
    break

video.release()


# Training is a method which is used when we want to run a function but still don't want to interrupt the whole process. Like here, when we take the object out of frame, it stops the camera momentarily, like it resets the camera momentarily. We use training, and in that we send email to the camera so that it doesn't freeze for sending email .