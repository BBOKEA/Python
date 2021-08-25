# import necessary packages
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
import time # time 라이브러리
# open webcam (웹캠 열기)

from cvlib.object_detection import draw_bbox

CAM_ID = 0

cam = cv2.VideoCapture(CAM_ID) #카메라 생성
if cam.isOpened() == False: #카메라 생성 확인
    print ('Can\'t open the CAM(%d)') % (CAM_ID)
    exit()

#윈도우 생성 및 사이즈 변경
cv2.namedWindow('CAM_Window')

########### 추가 ##################
prevTime = 0 #이전 시간을 저장할 변수
###################################
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()
    

# loop through frames

while webcam.isOpened():


    # read frame from webcam 
    status, frame = webcam.read()
    frame = cv2.flip(frame,1)
    if not status:
        break

    # apply object detection (물체 검출)
    bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov4-tiny')

    # draw bounding box over detected objects (검출된 물체 가장자리에 바운딩 박스 그리기)
    out = draw_bbox(frame, bbox, label, conf, write_conf=True)
     # 사람수 카운트

    if label.count('person') >=3 :
        print('감지된 사람수'+str(label.count('person')))
        print('위험')
        person_risk = 5
    
    elif label.count('car') >=3 :
        print('감지된 차량수'+str(label.count('car')))
        print('위험')
        car_risk = 5

    elif label.count('motorcycle') >= 1 :
        print('감지된 오토바이수'+str(label.count('motorcycle')))
        print('위험')
        mortorcycle_risk = 10



    # display output
    cv2.imshow("Real-time object detection", out)

    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# release resources
webcam.release()
cv2.destroyAllWindows()   