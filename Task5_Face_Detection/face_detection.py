import cv2

# Load Haar Cascade Classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Start webcam
cap = cv2.VideoCapture(0)

print("Press 'Q' to quit")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Failed to access webcam")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Face Count
    face_count = len(faces)

    # Draw rectangle around each face
    for i, (x, y, w, h) in enumerate(faces):

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            f"Face {i+1}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )

    # Display total faces detected
    cv2.putText(
        frame,
        f"Faces Detected: {face_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.imshow("Face Detection System", frame)

    key = cv2.waitKey(1)

    if key == ord('q') or key == ord('Q'):
        break

cap.release()
cv2.destroyAllWindows()