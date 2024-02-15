import sys # to access the system
import cv2
img = cv2.imread("models.jpg", cv2.IMREAD_ANYCOLOR)
 
while True:
    cv2.imshow("Happy Father's Day!", img)
    cv2.waitKey(0)
    sys.exit() # to exit from all the processes
 
cv2.destroyAllWindows() # destroy all windowscd 