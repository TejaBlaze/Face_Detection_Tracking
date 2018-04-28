import sys
import dlib
from skimage import io
from skimage.draw import polygon_perimeter
import cv2
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Create a HOG face detector using the built-in dlib class
    face_detector = dlib.get_frontal_face_detector()
    win = dlib.image_window()
    image = frame#cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detected_faces = face_detector(image, 1)
    #print("Total number of faces detected: {}".format(len(detected_faces)))   
    for d in detected_faces:
        rr,cc = polygon_perimeter([d.top(), d.top(), d.bottom(), d.bottom()], [d.right(), d.left(), d.left(), d.right()])
        if max(rr)<image.shape[0] and max(cc)<image.shape[1]:
            image[rr, cc] = (255, 0, 0)
    
    # Display the resulting frame
    cv2.imshow('Detected_frame',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()