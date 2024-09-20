import cv2
import mediapipe as mp
import numpy as np
import math

def calculate_angle(a, b, c):
    a = np.array([a.x, a.y])   # First point
    b = np.array([b.x, b.y])   # Middle point
    c = np.array([c.x, c.y])   # End point

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle

# Initialize variables
counter = 0
stage = None

cap = cv2.VideoCapture(0)
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Recolor image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    # Make detection
    results = pose.process(image)

    # Recolor back to BGR
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Extract landmarks
    try:
        landmarks = results.pose_landmarks.landmark

        # Get coordinates
        left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
        left_knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE]
        left_ankle = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE]

        # Calculate angle
        angle = calculate_angle(left_hip, left_knee, left_ankle)

        # Visualize angle
        cv2.putText(image, str(int(angle)),
                    (int(left_knee.x * image.shape[1]), int(left_knee.y * image.shape[0])),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Squat logic
        if angle > 160:
            stage = 'up'
        if angle < 90 and stage == 'up':
            stage = 'down'
            counter += 1
            print(f"Squat count: {counter}")

    except Exception as e:
        pass

    # Render squat count
    cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)
    cv2.putText(image, 'REPS', (15, 12),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(image, str(counter),
                (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    # Display image
    cv2.imshow('Knee Exercise', image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
