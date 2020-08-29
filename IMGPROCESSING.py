#Program used to take a screenshot and then to display a black and white video.

import cv2,time
video=cv2.VideoCapture(0) #This code to capture a photo
check,frame=video.read()
print(check)
print(frame)##frame represents the first image being captured.

time.sleep(3)
cv2.imshow('Capturing',frame)
cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()




video=cv2.VideoCapture(0) #To capture a video
a=1
first_frame=None
while True:
    a=a+1
    check,frame=video.read()
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Capturing',gray)
    if first_frame is None:
        first_frame=frame
        cv2.imshow('Capturing',frame)
        continue
    key=cv2.waitKey(1)
    if(key==ord('q')): #IF user presses 'q' then quits,ord to convert to ascii value
        
        break
print(a)
    

#cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()


