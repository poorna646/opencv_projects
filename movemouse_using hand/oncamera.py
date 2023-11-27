import cv2
import mediapipe
import pyautogui

camera=cv2.VideoCapture(0)  #to connect camera
while True:
    _,image=camera.read() #_:this varaible is not required,only one varaible is required"image"
    cv2.imshow("Hand movement video capture",image)
    #once the image is captured, we have to wait for milli seconds
    key=cv2.waitKey(100) #while waiting , if any key is captured - stored in the varaible called "key" , else it returns to previous statement
    #check whether the key is escape key(value for escape key=27)
    if key==27:
        break
camera.release()
cv2.destroyAllWindows()
