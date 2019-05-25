# version-2
## Advanced Lane detection

In diesem Projekt wurden Computer Vision Techniken verwendet, um Fahrspurbegrenzungen zu identifizieren.

Um dies zu erreichen, werden die folgenden Schritte durchgeführt:
- Berechnen der Kamerakalibriermatrix und der Verzerrungskoeffizienten des verwendeten Kameraobjektivs anhand einer Reihe von Schachbrettbildern, die von derselben Kamera aufgenommen wurden.
- Verwendung der vorgenannten Matrix und des Koeffizienten zur Korrektur der Verzerrungen, die durch die Rohdatenausgabe der Kamera entstehen.
- Verwenden Sie Farbtransformationen und Sobel-Algorithmus, um ein Binärbild zu erstellen, das aus unnötigen Informationen über das Bild herausgefiltert wurde. 
- Wenden Sie die perspektivische Transformation an, um eine "Vogelperspektive" des Bildes zu sehen, als ob Sie vom Himmel blicken würden. 
- Wenden Sie die Maskierung an, um den gewünschten Bereich zu erhalten, erkennen Sie Fahrbahnpixel, 
- Bestimmen Sie die am besten geeignete Kurve für jede Spur die Krümmung der Spuren.
- Projizieren Sie die Fahrspurbegrenzungen wieder auf das unverzerrte Bild der ursprünglichen Ansicht. 
- Ausgabe einer visuellen Anzeige der Fahrspurbegrenzungen und anderer verwandter Informationen 

### Requirements 
- numpy
- opencv
- python3 
- picamera

### HOW TO USE
- You need to setup dependencies to run a Jupyter Notebook on your computer and setup a handful of packages such as `opencv`
```
import matplotlib.pyplot as plt
%matplotlib inline
import cv2 
import numpy as np
import pickle
from scipy.misc import imread

from moviepy.editor import VideoFileClip
from IPython.display import HTML
```
### Wichtige Links

- Video Anleitung für OpenCV für den Raspberry pi
- - https://www.youtube.com/watch?v=ZuhPzP5lt9U&list=LL0DRCOCzI5IYxkaMweeubRA&index=13&t=1832s
