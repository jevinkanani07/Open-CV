import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Frame not recevie")
        break


    cv2.imshow("webcam feed",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("quit the fream")
        break

    cap.release()
    cv2.destroyAllWindows()