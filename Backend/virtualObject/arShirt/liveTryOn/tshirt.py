import cv2
import cvzone
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0)
detector = PoseDetector()

image_path = "sampleData/tshirt3.png"

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findPose(img, draw=False)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
    if lmList:
        # center = bboxInfo["center"]
        lm11 = lmList[11][0:2]
        lm12 = lmList[12][0:2]
        lm24 = lmList[24][0:2]

        breadth = detector.findDistance(lm12, lm11)
        length = detector.findDistance(lm12, lm24)

        shift_x = -30
        shift_y = -40

        coord = (lm12[0] + shift_x, lm12[1] + shift_y)

        imgShirt = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        imgShirt = cv2.resize(imgShirt, (0, 0), None, breadth[0]*0.00333333333, length[0]*0.002)
        try:
            img = cvzone.overlayPNG(img, imgShirt, coord)
        except:
            pass
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

