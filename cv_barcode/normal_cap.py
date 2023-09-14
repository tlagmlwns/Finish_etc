import cv2
import time

def nor_main():
    cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)
    if cap.isOpened() == False:
        print("-Camera load Failed")
        exit()
        
    ret, frame = cap.read()
    print("-저장할 이미지 이름을 작성 >> ", end="")
    Name = str(input())
    file_path = Name+".jpg"

    cv2.imwrite(file_path, frame)

    cap.release()

    cv2.destroyAllWindows()

    print("-사진이 저장되었습니다:", file_path)
