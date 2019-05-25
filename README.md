# version-2
## Advanced Lane detection

In diesem Projekt wurden Computer Vision Techniken verwendet, um Fahrspurbegrenzungen zu identifizieren.

Um dies zu erreichen, werden die folgenden Schritte durchgeführt:
- Berechnen der Kamerakalibriermatrix und der Verzerrungskoeffizienten der verwendeten Kamera anhand einer Reihe von Schachbrettbildern, die von derselben Kamera aufgenommen wurden.
- Entzerren der einzelen Frames anhand der zurvor errechneten Matrizen
- Umwandeln des Originalsbildes in den HLS-Farbraum und anwendung des Sobel-Algorithmus um:
- - Isolieren der Gelben Farbe: Gelbe Fahrbahnmarkierung
- - Isolieren der Weißen Farbe: Weiße Fahrbahnmarkierung
- Bitweise ODER gelbe und weiße Masken, um eine gemeinsame Maske zu erhalten.
- Perspektivische Transformation, um eine "Vogelperspektive" des Bildes zu erhalten
- - src (sorce) und- dst(destination) Parameter um die Transformierten Bereiche zu definieren.
- Bestimmen andhand des Binärbild die am besten geeignete Kurve für jede Spur durch Polynomische Anpassung / polinominal fit. Dazu wird für jede Fahrspur ein Polynom zweiter Ordnung bestimmt
-- Bild wird in 9 horizontale Schichten aufgeteilt und 
- Projizieren Sie die Fahrspurbegrenzungen wieder auf das unverzerrte Bild der ursprünglichen Ansicht. 
- Ausgabe einer visuellen Anzeige der Fahrspurbegrenzungen und anderer verwandter Informationen 

## Anforderungen/Requirements 
- numpy
- opencv
- python3 
- picamera

## Wichtige Links

- Video Anleitung für OpenCV für den Raspberry pi
- - https://www.youtube.com/watch?v=ZuhPzP5lt9U&list=LL0DRCOCzI5IYxkaMweeubRA&index=13&t=1832s
