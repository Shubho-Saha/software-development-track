import cv2
import time

cam = cv2.VideoCapture(0)

start = time.time()

while True:
    ret, frame = cam.read()

    if not ret:
        break
    
    cv2.imshow("my cam", frame)

    if time.time() - start > 10:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
     
cam.release()
cv2.destroyAllWindows()