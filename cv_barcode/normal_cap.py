import cv2
import datetime
import time

cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)
if cap.isOpened() == False:
    print("Camera load Failed")
    exit()
    
ret, frame = cap.read()
cur_time = datetime.datetime.now()
CTN = cur_time.strftime("%y%m%d%S") 
file_path = "cp"+CTN+".jpg" #현재시간으로 이름 저장

cv2.imwrite(file_path, frame)

cap.release()

cv2.destroyAllWindows()

print("사진이 저장되었습니다:", file_path)
