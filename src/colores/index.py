import cv2
from Color import Color 

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    red = Color(frame, [136, 87, 11], [180, 255, 255], (0, 0, 255), "Rojo", 800)
    green = Color(frame, [25, 52, 72], [102, 255, 255], (0, 255, 0), "Verde", 800)
    blue = Color(frame, [94, 80, 2], [120, 255, 255], (255, 0, 0), "Azul", 1000) 
    yellow = Color(frame, [20, 100, 100], [30, 255, 255], (0, 255, 255), "Amarillo", 800)
    
    red.detect()
    green.detect()
    blue.detect()
    yellow.detect()

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()