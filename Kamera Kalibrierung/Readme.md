# Kamera Kalibrierung

Mit dem Skript `get20pics.py` können 20 Bilder vom vorliegenden Schachbrettmuster `chessboard.png` aus verschieden Positionen und Winkel aufgenommen werden.
Diese Bilder können dann durch die Datei `calibration.py` verarbeitet werden um die Kamermatrix: `mtx` und die Entzerrungsmatrix `dst` zu gewinnen.
Beie Matrizen müssten dann händisch im Hauptskript `lane-detect-pi.py` eingetragen werden. 

#### To do:
- [ ] Kameramatrix und Entzerrrungsmatrix über eine Datei automatisch einlesen und einschreiben - Dies kann z.B. über Pythons Library Pickle realisiert werden
