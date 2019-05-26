# version-2
## Advanced Lane detection

![](Beispiel.png)


In diesem Projekt wurden Computer Vision Techniken verwendet, um Fahrspurbegrenzungen zu identifizieren.

Um dies zu erreichen, werden die folgenden Schritte durchgeführt:
- Berechnen der Kamerakalibriermatrix und der Verzerrungskoeffizienten der verwendeten Kamera anhand einer Reihe von Schachbrettbildern, die von derselben Kamera aufgenommen wurden.
- Entzerren der einzelen Frames anhand der zurvor errechneten Matrizen
- Umwandeln des Originalsbildes in den HLS-Farbraum und anwendung des Sobel-Algorithmus um:
- - Isolieren der Gelben Farbe: Gelbe Fahrbahnmarkierung
- - Isolieren der Weißen Farbe: Weiße Fahrbahnmarkierung
- Bitweise ODER gelbe und weiße Masken, um eine gemeinsame Maske zu erhalten.
- Perspektivische Transformation, um eine "Vogelperspektive" des Bildes zu erhalten
- - src (sorce) und- dst (destination) Parameter um die Transformierten Bereiche zu definieren.
- Bestimmen andhand des Binärbild die am besten geeignete Kurve für jede Spur durch Polynomische Anpassung. Dazu wird für jede Fahrspur ein Polynom zweiter Ordnung bestimmt.
1. Es wird ein Histogramm berechnet, um die Position der Fahrspur an der x-Achse zu bestimmen.
2. Das Bild wird in 9 horizontale Schichten aufgeteilt
3. Plazieren eines Fensters um den Mittelpunkt der Spur
4. Plazieren weiterer Fenster um den Mittelpunklt der übrigen 8 Fenster. Diese Methode Folgt der "Spur" bis zum oberen Rand des Binärbildes und beschleunigt die Verarbeitung indem es nur nach aktiven Pixeln über einen kleinen Teil des Bildes sucht.
5. Pixel, die zu jeder Spurlinie gehören, werden identifiziert und die Numpy polyfit()-Methode wird Polynom zweiter Ordnung errchnet
- Projizieren Sie die Fahrspurbegrenzungen wieder auf das unverzerrte Bild der ursprünglichen Ansicht. 
- Ausgabe einer visuellen Anzeige der Fahrspurbegrenzungen und anderer verwandter Informationen 

## Anforderungen/Requirements 
- numpy
- opencv
- python3 
- picamera

*1. James Madison
*2. James Monroe
*3. John Quincy Adams

## Wichtige Links

- Video Anleitung für OpenCV für den Raspberry pi
- - https://www.youtube.com/watch?v=ZuhPzP5lt9U&list=LL0DRCOCzI5IYxkaMweeubRA&index=13&t=1832s
