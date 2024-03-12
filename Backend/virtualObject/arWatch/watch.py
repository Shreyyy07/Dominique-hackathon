import cv2
import mediapipe as mp
import numpy as np
import uuid
import os

# Load the image you want to impose
imposed_image = cv2.imread('sampleData/watch.png')
image = cv2.resize(imposed_image, (170, 170))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
rgba_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
rgba_image[:, :, 3] = mask

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # print(results)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                          )
                hand_landmarks = results.multi_hand_landmarks[num]  # Corrected indexing

                # Calculate the pixel coordinates of landmark[0] in the frame
                x_pixel = int(hand_landmarks.landmark[0].x * frame.shape[1])
                y_pixel = int(hand_landmarks.landmark[0].y * frame.shape[0])
                image_to_impose = cv2.resize(rgba_image, (140, 140))

                x, y = x_pixel, y_pixel
                x -= 100
                y -= 80

                # Resize imposed image to fit within bounding box around landmark[0]
                h, w, _ = image_to_impose.shape

                for c in range(0, 3):
                    try:
                        frame[y:y + h, x:x + w, c] = frame[y:y + h, x:x + w, c] * (1 - image_to_impose[:, :, 3] / 255.0) + \
                                                   image_to_impose[:, :, c] * (image_to_impose[:, :, 3] / 255.0)
                    except:
                        pass
        cv2.imshow('watch', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
