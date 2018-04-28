import sys
import dlib
from skimage import io
from skimage.draw import polygon_perimeter

# Take the image file name from the command line
file_name = input("Image path: ")
#sys.argv[1]

# Create a HOG face detector using the built-in dlib class
face_detector = dlib.get_frontal_face_detector()

win = dlib.image_window()

# Load the image into an array
image = io.imread(file_name)

num_img_pyramids = int(input("Number of image pyramids: "))
# Run the HOG face detector on the image data.
# The result will be the bounding boxes of the faces in our image.
detected_faces = face_detector(image, num_img_pyramids)

print("Total number of faces detected: {}".format(len(detected_faces)))

'''
#
# Open a window on the desktop showing the image
win.set_image(image)

# Loop through each face we found in the image
for i, face_rect in enumerate(detected_faces):

	# Detected faces are returned as an object with the coordinates 
	# of the top, left, right and bottom edges
	#print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))

	# Draw a box around each face we found
	win.add_overlay(face_rect)
'''
    
for d in detected_faces:
    rr,cc = polygon_perimeter([d.top(), d.top(), d.bottom(), d.bottom()], [d.right(), d.left(), d.left(), d.right()])
    if max(rr)<image.shape[0] and max(cc)<image.shape[1]:
        image[rr, cc] = (255, 0, 0)
    
io.imsave('Detected_images/'+file_name.split('/')[1], image)