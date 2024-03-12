import math
import cv2
import cv2.aruco as aruco
import numpy as np
from cvzone.FaceMeshModule import FaceMeshDetector


def findArucoMarkers(img, markerSize=6, totalMarkers=250, draw=True):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    arucoDict = aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    arucoParam = aruco.DetectorParameters()
    bboxs, ids, rejected = cv2.aruco.detectMarkers(imgGray, arucoDict, parameters=arucoParam)

    if draw:
        cv2.aruco.drawDetectedMarkers(img, bboxs, ids)

    # Print ArUco IDs
    # print("Detected ArUco Marker IDs:", ids)

    return [bboxs, ids]


def augmentAruco(bbox, id, dst, imgAug, drawId=False):
    tl = bbox[0][0][0], bbox[0][0][1]
    tr = bbox[0][1][0], bbox[0][1][1]
    br = bbox[0][2][0], bbox[0][2][1]
    bl = bbox[0][3][0], bbox[0][3][1]

    h, w, c = imgAug.shape

    pts1 = np.array([tl, tr, br, bl])
    pts2 = np.float32([[0, 0], [w, 0], [w, h], [0, h]])

    matrix, _ = cv2.findHomography(pts2, pts1)

    imgOut = cv2.warpPerspective(imgAug, matrix, (dst.shape[1], dst.shape[0]))
    cv2.fillConvexPoly(dst, pts1.astype(int), (0, 0, 0))

    imgOut = dst + imgOut
    imgOut = cv2.addWeighted(dst, 1, imgOut, 0.5, 0)

    return imgOut


def load_markers():
    marker0 = cv2.imread('marker/marker0.png')
    marker1 = cv2.imread('marker/marker1.png')
    return cv2.resize(marker0, (150, 150), interpolation=cv2.INTER_AREA), cv2.resize(marker1, (150, 150),
                                                                                     interpolation=cv2.INTER_AREA)


def initialize_ema():
    return None, 0.2  # Initial value for EMA and smoothing factor


def resize_and_rotate_frame(capture, width, height):
    frame = cv2.rotate(cv2.resize(capture.read()[1], (width, height)), cv2.ROTATE_90_CLOCKWISE)
    return frame


def calculate_ema(ema_d, alpha, d):
    if ema_d is None:
        ema_d = d
    else:
        ema_d = alpha * d + (1 - alpha) * ema_d
    return ema_d


def overlay_background(img2, bg, marker):
    center_x = (bg.shape[1] - marker.shape[1]) // 2
    center_y = (bg.shape[0] - marker.shape[0]) // 2
    bg[center_y:center_y + marker.shape[0], center_x:center_x + marker.shape[1]] = marker

    diff1 = cv2.subtract(img2, bg)
    diff2 = cv2.subtract(bg, img2)

    diff = diff1 + diff2

    gray = cv2.cvtColor(diff.astype(np.uint8), cv2.COLOR_BGR2GRAY)
    gray[np.abs(gray) < 10] = 0

    fgmask = gray.astype(np.uint8)

    fgmask[fgmask > 0] = 255

    fgmask_inv = cv2.bitwise_not(fgmask)

    fgimg = cv2.bitwise_and(img2, img2, mask=fgmask_inv)
    bgimg = cv2.bitwise_and(bg, bg, mask=fgmask)

    dst = cv2.add(bgimg, fgimg)

    return dst


def main():
    marker0, marker1 = load_markers()

    imgAug1 = cv2.imread('sampleData/watchFront1.jpg')
    # imgAug1 = cv2.resize(imgAug1, (150, 150), interpolation=cv2.INTER_AREA)

    # cap = cv2.VideoCapture('http://10.222.145.179:8080/video')
    video = cv2.VideoCapture('http://10.222.145.179:8080/video')

    # detector = FaceMeshDetector(maxFaces=1)

    ema_d, alpha = initialize_ema()

    while True:
        # img = resize_and_rotate_frame(cap, 600, 350)
        # img = cv2.flip(img, 1)
        img2 = resize_and_rotate_frame(video, 600, 350)

        # img, faces = detector.findFaceMesh(img, draw=False)

        bg = img2
        dst = img2

        # if faces:
        #     face = faces[0]
        #     pointLeft = face[145]
        #     pointRight = face[374]
        #     cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
        #     cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
        #
        #     w, _ = detector.findDistance(pointLeft, pointRight)
        #     W = 6.3
        #     f = 457
        #     d = (W * f) / w
        #
        #     ema_d = calculate_ema(ema_d, alpha, d)
        #
        #     midPointOfEyes = face[168]
        #     cv2.circle(img, midPointOfEyes, 5, (255, 0, 255), cv2.FILLED)
        #     topPoint = face[10]
        #     cv2.circle(img, topPoint, 5, (255, 0, 255), cv2.FILLED)
        #     Distance, _ = detector.findDistance(topPoint, midPointOfEyes)
        #
        #     if Distance > 0:
        #         angle_rad = math.atan(ema_d / Distance)
        #         angle_deg = math.degrees(angle_rad)
        #
        #         if (20 <= d <= 40 and 70 <= Distance <= 90 and 10 <= angle_deg <= 30) or (
        #                 45 <= d <= 60 and 37 <= Distance <= 42 and 47 <= angle_deg <= 56) or (
        #                 61 <= d <= 92 and 31 <= Distance <= 36 and 61 <= angle_deg <= 72):
        marker = marker0

        imgAug = imgAug1
        dst = overlay_background(img2, bg, marker)
        arucoFound = findArucoMarkers(dst)

        if len(arucoFound[0]) != 0:
            for bbox, id in zip(arucoFound[0], arucoFound[1]):
                dst = augmentAruco(bbox, id, dst, imgAug)

        # cv2.imshow("Image", img)
        cv2.imshow('Background overlay', dst)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # cap.release()
    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
