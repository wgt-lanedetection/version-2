from picamera import PiCamera
from time import sleep


camera = PiCamera()
# Größe des Bildes einstellen
camera.resolution = (320, 192)
camera.start_preview()

for i in range(20):
    sleep(2)    #Bilder im Abstand von 2 Mintuen erstellen
    camera.capture('/home/pi/lane/calibration/calibration%s.jpg' % i) # Hier den Pfad eingeben
camera.stop_preview()
