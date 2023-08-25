import cv2

def detect_people(video_path):
    # Charger le modèle de détection de personnes pré-entraîné
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Ouvrir la vidéo
    video_capture = cv2.VideoCapture(video_path)

    while True:
        ret, frame = video_capture.read()

        if not ret:
            break

        # Effectuer la détection de personnes dans le cadre
        detected, _ = hog.detectMultiScale(frame)

        # Dessiner les rectangles autour des personnes détectées
        for (x, y, w, h) in detected:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Afficher le cadre traité
        cv2.imshow('Video', frame)

        # Presser 'q' pour quitter la boucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libérer les ressources
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = "C:/Users/DELL/Desktop/MyPythonExercises/california-street.mp4"  # Remplacez cela par le chemin de votre vidéo
    detect_people(video_path)
