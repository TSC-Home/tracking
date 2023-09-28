import cv2
import mediapipe as mp
import csv
import time
import tkinter as tk
from tkinter import messagebox
import threading
import psutil

# Initialisierung der OpenPose-Bibliothek
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Initialisierung der Kamera
cap = cv2.VideoCapture(0)

# Pose-Erfassungsmodell laden
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

    # Variablen für die Aufnahme
    recording = False
    csv_file = None
    csv_writer = None

    def start_recording():
        global recording, csv_file, csv_writer
        if not recording:
            # CSV-Datei für die Posen erstellen
            csv_file = open('poses.csv', 'w', newline='')
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Timestamp', 'Pose'])
            recording = True
            start_button.config(state='disabled')
            stop_button.config(state='normal')
            messagebox.showinfo('Information', 'Die Aufnahme wurde gestartet.')

    def stop_recording():
        global recording, csv_file, csv_writer
        if recording:
            # CSV-Datei schließen
            csv_file.close()
            recording = False
            start_button.config(state='normal')
            stop_button.config(state='disabled')
            messagebox.showinfo('Information', 'Die Aufnahme wurde gestoppt.')

    def process_frame(frame):
        # Frame in RGB umwandeln
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Pose-Erfassung auf dem Frame durchführen
        results = pose.process(frame_rgb)

        # Posen in CSV-Datei schreiben
        timestamp = time.time()
        pose_list = []

        if results.pose_landmarks is not None:
            for landmark in results.pose_landmarks.landmark:
                pose_list.append([landmark.x, landmark.y, landmark.z])

        csv_writer.writerow([timestamp, pose_list])

        # Knochen zeichnen
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                              mp_drawing.DrawingSpec(
                                  color=(0, 0, 255), thickness=2, circle_radius=2),
                              mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2))

        # Frame anzeigen
        cv2.imshow('Pose Detection', frame)

    def process_video():
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            # Posen verarbeiten, wenn die Aufnahme aktiv ist
            if recording:
                process_frame(frame)

            # Überprüfen, ob das Fenster geschlossen wurde
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Funktion zur Aktualisierung der CPU-Auslastung
    def update_cpu_label():
        cpu_usage = psutil.cpu_percent()
        cpu_label.config(text=f'CPU: {cpu_usage}%')
        root.after(1000, update_cpu_label)

    # Tkinter-Interface erstellen
    root = tk.Tk()
    root.title('Pose Detection')
    start_button = tk.Button(root, text='Start', command=start_recording)
    start_button.pack()
    stop_button = tk.Button(root, text='Stop', command=stop_recording, state='disabled')
    stop_button.pack()
    cpu_label = tk.Label(root, text='', font=('Arial', 12))
    cpu_label.pack()

    # Videoverarbeitung in einem separaten Thread starten
    video_thread = threading.Thread(target=process_video)
    video_thread.start()

    # CPU-Auslastung in einem separaten Thread aktualisieren
    cpu_thread = threading.Thread(target=update_cpu_label)
    cpu_thread.start()

    # Tkinter-Hauptloop starten
    root.mainloop()

    # Kamera freigeben
    cap.release()

    # Fenster schließen
    cv2.destroyAllWindows()
