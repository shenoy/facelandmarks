import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("ronaldo.jpg")
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=1)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

frameNum = 0
while True:
    success, img = cap.read()
    frameNum += 1
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if frameNum ==1 and results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_TESSELATION,
                                  drawSpec, drawSpec)
            for id,lm in enumerate(faceLms.landmark):
                ih, iw, ic = img.shape
                x,y = int(lm.x*iw), int(lm.y*ih)
                print(x,y)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)


    def output_coords_to_csv(x_coords, y_coords, csv_filename):
        with open(csv_filename, 'w') as f:
            for i in range(len(x_coords)):
                x = x_coords[i]
                y = y_coords[i]
                f.write(str(x) + ',' + str(y) + '\n')
        print('Coordinates written to CSV file.')
