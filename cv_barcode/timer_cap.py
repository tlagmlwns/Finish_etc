import cv2
import time
import datetime

# 화면을 띄우는 함수
def show_screen_for_seconds(seconds):
    cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)
    start_time = time.time()

    while True:
        ret, frame = cap.read()

        elapsed_time = time.time() - start_time
        str_et = str(int(seconds - elapsed_time)+1)
        
        text_size, _ = cv2.getTextSize(str_et, cv2.FONT_HERSHEY_PLAIN, 4, 4)
        tx = (frame.shape[1] - text_size[0]) // 2
        ty = (frame.shape[0] + text_size[1]) // 2
        cv2.putText(frame, str_et, (tx, ty), cv2.FONT_ITALIC, 3, (0, 255, 0), 5)
        cv2.imshow("Screen", frame)

        if elapsed_time >= seconds: break
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()

# s초 동안 화면 표시
s = int(input("타이머 입력하시오 : "))
show_screen_for_seconds(s)

# 화면 캡처
cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)  # 웹캠을 사용하는 경우 0을 사용, 기타 입력 소스를 사용하려면 변경
ret, frame = cap.read()

cur_time = datetime.datetime.now()
CTN = cur_time.strftime("%y%m%d%S") 
file_path = "cp"+CTN+".jpg" #현재시간으로 이름 저장

cv2.imwrite(file_path, frame)
# 리소스 해제
cap.release()
cv2.destroyAllWindows()
