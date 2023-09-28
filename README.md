# Pose Detection mit OpenPose - Installations- und Ausführungsdokumentation

Diese Dokumentation führt Sie durch die Installation und Ausführung des Python-Skripts zur Pose Detection, einschließlich der Installation von Python und erforderlichen Bibliotheken.
#
## Schritt 1: Python und erforderliche Bibliotheken installieren

Stellen Sie sicher, dass Sie Python auf Ihrem System installiert haben. Wenn Python nicht installiert ist, können Sie es von der offiziellen Website [https://www.python.org/downloads/](https://www.python.org/downloads/) herunterladen und installieren.

Um sicherzustellen, dass alle erforderlichen Bibliotheken installiert sind, öffnen Sie die Befehlszeile oder das Terminal und führen Sie die folgenden Befehle aus:

Um sicherzustellen, dass alle erforderlichen Bibliotheken installiert sind, öffnen Sie die Befehlszeile oder das Terminal und führen Sie die folgenden Befehle aus:

```bash
pip install opencv-python
pip install mediapipe
pip install python-csv
pip install time
pip install tk
pip install threading
pip install psutil
```

## Schritt 2: Das Skript ausführen
Laden Sie das Skript herunter, in dem die Pose Detection implementiert ist, auf Ihren Computer.

Öffnen Sie eine Befehlszeile oder ein Terminalfenster und navigieren Sie zum Verzeichnis, in dem sich das Skript befindet.

Führen Sie das Skript mit dem folgenden Befehl aus:
```bash
python bear_tracking.py
```

Ersetzen Sie script_name.py durch den tatsächlichen Namen des Skripts, den Sie heruntergeladen haben.

#

## Schritt 3: Verwendung des Pose Detection-Tools
Nachdem das Skript ausgeführt wurde, öffnet sich ein Fenster mit einer Benutzeroberfläche. Hier sind die Hauptfunktionen des Tools:

Start: Klicken Sie auf die "Start"-Schaltfläche, um die Aufnahme von Posen zu starten.

Stop: Klicken Sie auf die "Stop"-Schaltfläche, um die Aufnahme zu beenden.

CPU-Auslastung: Die aktuelle CPU-Auslastung wird in Prozent angezeigt.

Beenden: Sie können das Fenster schließen, um die Anwendung zu beenden.
#
## Hinweise zur Verwendung
Das Tool verwendet die Webcam (Standardkamera), um Posen zu erfassen. Stellen Sie sicher, dass Ihre Kamera ordnungsgemäß funktioniert und eingeschaltet ist.

Während der Aufnahme werden Posen in einer CSV-Datei mit dem Namen "poses.csv" gespeichert. Diese Datei wird im gleichen Verzeichnis wie das Skript erstellt.

Drücken Sie die Taste "q" auf Ihrer Tastatur, um das Fenster zu schließen und die Aufnahme zu beenden.

Die CPU-Auslastung wird in Echtzeit angezeigt und alle 1 Sekunde aktualisiert.

Stellen Sie sicher, dass alle benötigten Bibliotheken korrekt installiert sind, um das Skript ordnungsgemäß auszuführen.
