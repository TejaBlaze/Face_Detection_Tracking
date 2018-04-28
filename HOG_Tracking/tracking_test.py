import cv2
import sys
import dlib
from skimage import io
import numpy as np
from skimage.draw import polygon_perimeter
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
if __name__ == '__main__' :
 
    # Set up tracker.
    # Instead of MIL, you can also use
 
    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
    tracker_type = tracker_types[int(sys.argv[1])]
 
    if int(minor_ver) < 3:
        tracker = cv2.Tracker_create(tracker_type)
    else:
        if tracker_type == 'BOOSTING':
            tracker = cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            tracker = cv2.TrackerGOTURN_create()
 
    # Read video
    video = cv2.VideoCapture(0)
 
    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()
 
    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()
    
    face_detector = dlib.get_frontal_face_detector()
    win = dlib.image_window()
    image = np.copy(frame)#cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detected_faces = face_detector(image, 1)
    #print("Total number of faces detected: {}".format(len(detected_faces)))   
    for d in detected_faces:
        rr,cc = polygon_perimeter([d.top(), d.top(), d.bottom(), d.bottom()], [d.right(), d.left(), d.left(), d.right()])
        if max(rr)<image.shape[0] and max(cc)<image.shape[1]:
            image[rr, cc] = (255, 0, 0)
    
    #cv2.imshow('Detected_frame', image)
    # Define an initial bounding box
    bbox = (d.left(), d.top(), d.right(), d.bottom())
 
    # Uncomment the line below to select a different bounding box
    #bbox = cv2.selectROI(image)
    cv2.SetImageROI(frame, bbox)
    #frame = image
    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)
 
    while True:
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break
         
        # Start timer
        timer = cv2.getTickCount()
 
        # Update tracker
        ok, bbox = tracker.update(frame)
 
        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
 
        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        else :
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
 
        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
     
        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
 
        # Display result
        cv2.imshow("Tracking", frame)
 
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break


    # When everything done, release the capture
    video.release()
    cv2.destroyAllWindows()