# server.py

from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import cv2
import mediapipe as mp
import base64
import numpy as np

app = Flask(__name__)
socketio = SocketIO(app)

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

@app.route('/')
def index():
    return "Backend Server is running!"

@socketio.on('image')
def process_frame(image_data):
    try:
        # Convert base64 image data to numpy array
        image_np = np.frombuffer(base64.b64decode(image_data), dtype=np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

        # Perform hand detection using MediaPipe
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Extract hand landmarks
        landmarks = []
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                landmarks.append(hand_landmarks.landmark)

        # Send processed data back to React
        emit('processed_data', {'landmarks': landmarks})
    except Exception as e:
        print(f"Error processing frame: {str(e)}")

if __name__ == '__main__':
    socketio.run(app, debug=True)
