import cv2
import numpy as np
import asyncio
from cvzone.FaceMeshModule import FaceMeshDetector


async def main():
    image_path = 'sampleData/images2.jpeg'
    image = cv2.imread(image_path)
    image = cv2.resize(image, (314, 149))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    rgba_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    rgba_image[:, :, 3] = mask

    face_mesh_detector = FaceMeshDetector(maxFaces=2)

    cap = cv2.VideoCapture(0)

    while True:
        success, img = await loop.run_in_executor(None, cap.read)
        img = cv2.flip(img, 1)
        img, faces = face_mesh_detector.findFaceMesh(img, draw=False)

        if faces:
            right_point = faces[0][454]
            left_point = faces[0][234]
            breadth, _ = face_mesh_detector.findDistance(left_point, right_point)
            image_to_impose = cv2.resize(rgba_image, (0, 0), None, (breadth*0.0035802469), (breadth*0.0035802469))

            landmark_point = faces[0][168]

            x = int(landmark_point[0] - image_to_impose.shape[1] / 2) + 4
            y = int(landmark_point[1] - image_to_impose.shape[0] / 2) + 10

            h, w, _ = image_to_impose.shape

            for c in range(0, 3):
                try:
                    img[y:y + h, x:x + w, c] = img[y:y + h, x:x + w, c] * (1 - image_to_impose[:, :, 3] / 400.0) + \
                                            image_to_impose[:, :, c] * (image_to_impose[:, :, 3] / 400.0)
                except:
                    pass

        cv2.imshow("Video", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
