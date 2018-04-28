# Python Implementation of Viola-Jones Face Detection Algorithm and Face Detection in a crowd using HOG method

This project implements the Viola-Jones framework for face detection using python and additionally face detection in a crowd is also implemented using Histogram of Oriented Gradiets method.


### Prerequisites

Language: Python 3.5 
Libraries required: Numpy, Opencv-python


### Installing

Installing Numpy
```
python -m pip install numpy
```
Installing Opencv-python
```
python -m pip install opencv-python
```

## Running the program

Open terminal in Viola-Jones project folder and run test_img.py using

## Place your test image in /ViolaJones_1.0/dist/test_img/Images

```
Running with python
-------------------
python test_img.py [zoom_lvl]

Run distribution(if no python)
------------------------------
cd ViolaJones_1.0/dist/test_img
test_img [zoom_lvl]                     #zoom_lvl in range[0.05, 0.1] represents level of zooming in scanning subwindow
Create new classifier(y/n)? : n         #test already created classifier
```

## To give image input via webcam, run test_webcam.py using
```
Running with python
-------------------
python test_webcam.py [zoom_lvl]

Run distribution(if no python)
------------------------------
cd ViolaJones_1.0/dist/test_webcam
test_webcam [zoom_lvl]                  #zoom_lvl in range[0.05, 0.1] represents level of zooming in scanning subwindow
Create new classifier(y/n)? : n         #test already created classifier
```


## Open terminal in Extra/HOG_Tracking project folder for local images, run DetectFaces.py
```
Running(only with python)
-------------------------
python DetectFaces.py
(Enter image file path)
```

## To give image input via webcam, run DetectFaces_webcam.py using
```
Running(only with python)
-------------------------
python DetectFaces_webcam.py
```


## To track set of faces input via webcam, run tracking_test.py using
```
Running(only with python)
-------------------------
python tracking_test.py [type_tracker]

(type_tracker: Which tracker type to use, preferred: 2 , which indicates 'KCF' method. In range [0,4], see code for details.)
```