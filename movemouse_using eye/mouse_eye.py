import cv2
import mediapipe
import pyautogui
import sys
face_mesh_landmarks = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
cam = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()
if not cam.isOpened():
    print("Error: Could not open camera.")
    sys.exit()

while(True):
    _,image = cam.read()
    image =cv2.flip(image,1)
    if image is None:
        print("Error: Could not read frame from camera.")
        sys.exit()
    window_height,window_width,_ = image.shape # _ : (window_depth-not needed)
    #convert the captured image to rgb format
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    processed_image =  face_mesh_landmarks.process(rgb_image)
    all_face_landmark_points = processed_image.multi_face_landmarks
    #print(all_face_landmark_points)
    if all_face_landmark_points:
        one_face_landmark_points = all_face_landmark_points[0].landmark
        #id - for finding the landmarks to move
        for id,landmark_point in enumerate(one_face_landmark_points[474:478]):
            #convert the captured points to windows face resolution
            x= int(landmark_point.x * window_width)
            y= int(landmark_point.y * window_height)
            #print(landmark_point.x , landmark_point.y)
            #print(x,y)
            if id==1: #face is captured
                mouse_x = int(screen_width/window_width*x)
                mouse_y = int(screen_height/window_height *y)
                #move the mouse to respective positions
                pyautogui.moveTo(mouse_x,mouse_y)

            cv2.circle(image,(x,y),3,(0,0,255)) #radius=3, (0,0,255)-red color
        left_eye = [one_face_landmark_points[145],one_face_landmark_points[159]] #145-upper lmt , 159-lower limit

        for landmark_point in left_eye:
            #convert the captured points to windows face resolution
            x= int(landmark_point.x * window_width)
            y= int(landmark_point.y * window_height)
            #print(landmark_point.x , landmark_point.y)
            print(x,y)
            cv2.circle(image,(x,y),3,(0,255,255)) #radius=3, (0,0,255)-red color

        #find the distance between two points
        if(left_eye[0].y - left_eye[1].y < 0.01): #0-upper limit,1-lower limit
            pyautogui.click()
            pyautogui.sleep(2)
            print("mouse clicked")

        
    cv2.imshow("Eye cotrolled mouse",image)
    key = cv2.waitKey(100)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()