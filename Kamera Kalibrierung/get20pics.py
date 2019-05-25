from picamera import PiCamera
from time import sleep


camera = PiCamera()
# set resulution
camera.resolution = (320, 192)
camera.start_preview()

for i in range(20):
    sleep(2)
    camera.capture('/home/pi/lane/calibration/calibration%s.jpg' % i) # Hier den Pfad eingeben
camera.stop_preview()
