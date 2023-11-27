import cv2
import mediapipe
import pyautogui
capture_hands=mediapipe.solutions.hands.Hands()
drawing_option = mediapipe.solutions.drawing_utils
screen_width , screen_height = pyautogui.size() #to move the finger on screen get screen width and height
camera=cv2.VideoCapture(0)  #to connect camera
x1 = y1 = x2 = y2 =0 # varaibles for storing x and  y values
while True:
    _,image=camera.read() #_:this varaible is not required,only one varaible is required"image"
    #capture image height to convert landmark points which is in decimal
    image_height,image_width,_ =image.shape
    #flip the image-because when righ hand is raised it looks like left hand
    image=cv2.flip(image,1)#1-represents y-axis
    #convert the image to rgb
    rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output_hands =capture_hands.process(rgb_image)
    all_hands=output_hands.multi_hand_landmarks
    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(image,hand)
            one_hand_landmarks=hand.landmark
            for id,lm in enumerate(one_hand_landmarks):
                x=int(lm.x * image_width)
                y=int(lm.y * image_height)
                #identify x & y
                #print(lm.x,lm.y)
                #print(x,y)

                #get id for identifying specific fingers
                if id==8: #forefinger
                    mouse_x = int(screen_width / image_width * x)
                    mouse_y = int(screen_height / image_height *y)
                    cv2.circle(image,(x,y),10,(0,255,255)) #radius=10 , color=0,255,255(yellow)
                    #mouse should to the location
                    pyautogui.moveTo(mouse_x , mouse_y)
                    x1 = x
                    y1 = y
                if id==4: #thumbfinger
                    x2 = x
                    y2 = y
                    cv2.circle(image,(x,y),10,(0,255,255))

        dist = y2 - y1 # identify vertical distance
        print(dist)
        if(dist<40):
            pyautogui.click()
            print("clicked")


    cv2.imshow("Hand movement video capture",image)
    #once the image is captured, we have to wait for milli seconds
    key=cv2.waitKey(100) #while waiting , if any key is captured - stored in the varaible called "key" , else it returns to previous statement
    #check whether the key is escape key(value for escape key=27)
    if key==27:
        break
camera.release()
cv2.destroyAllWindows()
