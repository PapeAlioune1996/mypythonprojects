from ultralytics import YOLO
import cv2
import math
import numpy as np

model = YOLO('DetectHuman.pt')

cap = cv2.VideoCapture(0)
PeopleStayed = 0

while True:
    s, img = cap.read()
    if not s:
        break

    result = model(img)

    for r in result:
        boxes = r[:, :4]
        conf = r[:, 4]

        for box, c in zip(boxes, conf):
            conf = math.ceil((c * 100)) / 100
            x1, y1, x2, y2 = box
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.putText(img, str(conf), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    k = cv2.waitKey(1)
    if k == 27:  # Press 'ESC' to exit the loop
        break

cap.release()
cv2.destroyAllWindows()
