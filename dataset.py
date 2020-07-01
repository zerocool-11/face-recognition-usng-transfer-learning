import cv2
import numpy as np

# Initialize Webcam
cap = cv2.VideoCapture(0)
count = 0

# Collect 100 samples of your face from webcam input
while True:

    ret, frame = cap.read()
    count += 1
    # Save file in specified directory with unique name
    file_name_path = 'C://Users//hp//Desktop//mlops-ws//16May2020//face_data//n0//image' + str(count) + '.jpg'
    cv2.imwrite(file_name_path, frame)

    # Put count on images and display live count
    cv2.putText(frame, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    cv2.imshow('Capturing face', frame)

    if cv2.waitKey(1) == 13 or count == 200: #13 is the Enter Key
        break
        
cap.release()
cv2.destroyAllWindows()      
print("Collecting Samples Complete")
