# import necessary packages
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
import time 
import os

from serial import Serial
from cvlib.object_detection import draw_bbox # 웹캠 온

import serial
import sys
import time
import threading
import queue



ser = serial.Serial('COM5', 9600) #아두이노 포트 할당
# CAM_ID = 0
# cam = cv2.VideoCapture(CAM_ID) #카메라 생성
# if cam.isOpened() == False: #카메라 생성 확인
#     print ('Can\'t open the CAM(%d)') % (CAM_ID)
#     exit()

#윈도우 생성 및 사이즈 변경
cv2.namedWindow('CAM_Window')

prevTime = 0 #이전 시간을 저장할 변수

def opencamera(): 
    webcam = cv2.VideoCapture('http://192.168.0.136:8091/?action=stream')

    count = 0
    if not webcam.isOpened():
        print("카메라를 열 수 없습니다.")
        exit()

    person_risk =0
    car_risk =0
    mortorcycle_risk=0

    while webcam.isOpened():

        status, frame = webcam.read()
        frame = cv2.flip(frame,1)  
        
        #line = ser.readline().decode("utf-8")
        #print(line)
        
        if not status:
            break
        
        # apply object detection (물체 검출)
        
        bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov3-tiny')

        # draw bounding box over detected objects (검출된 물체 가장자리에 바운딩 박스 그리기)
        out = draw_bbox(frame, bbox, label, conf, write_conf=True)
        # 사람수 카운트
        cv2.imshow("Real-time object detection", out)
        if label.count('person') >=3 :
            print('감지된 사람수'+str(label.count('person')))
            print('위험')
            person_risk = 5
        
        
            if person_risk == 5:
                m ='1'
                m = [m.encode('utf-8')]
                ser.writelines(m)
                
            if(car_risk ==5 or mortorcycle_risk==10):
                m ='5'
                m = [m.encode('utf-8')]
                ser.writelines(m)


        elif label.count('car') >=3 :
            print('감지된 차량수'+str(label.count('car')))
            print('위험')
            car_risk = 5
            if car_risk == 5:
                m ='2'
                m = [m.encode('utf-8')]
                ser.writelines(m)
                
            if(person_risk ==5 or mortorcycle_risk==10):
                m ='6'
                m = [m.encode('utf-8')]
                ser.writelines(m)

        elif label.count('motorcycle') >= 1 :
            print('감지된 오토바이수'+str(label.count('motorcycle')))
            print('위험')
            mortorcycle_risk = 10
            if mortorcycle_risk == 10:
                m ='4'
                m = [m.encode('utf-8')]
                ser.writelines(m)

            if(person_risk ==5 or car_risk==10):
                m ='8'
                m = [m.encode('utf-8')]
                ser.writelines(m)

        elif label.count('motorcycle') ==0 and label.count('car') ==0 and label.count('person') ==0 :
            print('아무것도 없습니다.'+str( label.count('motorcycle') ==0 and label.count('car') ==0 and label.count('poerson') ==0))
            m ='3'
            m = [m.encode('utf-8')]
            ser.writelines(m)

            if(person_risk ==5 or car_risk==10 or mortorcycle_risk):
                m ='7'
                m = [m.encode('utf-8')]
                ser.writelines(m)  
        
        
     
      
        count+=1
        print(count)
        if count >=150:
            webcam.release()
            cv2.destroyAllWindows() 
            opencamera()
           
        # press "esc" to stop
        if cv2.waitKey(5) == 27:
            break
        if cv2.waitKey(5) == 24:
            os.system("speed_check.py")
        
        
    # release resources
    webcam.release()
    cv2.destroyAllWindows()   

opencamera()