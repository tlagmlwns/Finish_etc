from pyzbar.pyzbar import decode #바코드 디코딩 라이브러리
from PIL import Image
import cv2, qrcode
import numpy as np
import normal_cap, timer_cap

def QRcode_detection(image_path): #QR_code test
    qr_code_image = cv2.imread(image_path)
    decoded_objects = decode(qr_code_image)
    
    if decoded_objects:
        for obj in decoded_objects:
            points = obj.polygon
            if len(points) > 4: #QR코드 읽는 부분 표시
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                points = hull
            points = np.array(points, dtype=np.int32)
            cv2.polylines(qr_code_image, [points], isClosed=True, color=(0, 0, 255), thickness=15)
            
            qr_code_data = obj.data.decode('utf-8') #QR코드 정보
            print("QR코드 추출중...")
            print(f"- QR 코드 데이터 : {qr_code_data}")

        rs_img = cv2.resize(qr_code_image, (400, 400)) #이미지 크기 조절
        cv2.imshow("QRcode result Image", rs_img) #이미지를 화면에 표시
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    else:
        print("QR 코드를 찾을 수 없습니다.")
        
def Barcode_detection(image_path): #Bar_code test
    image = cv2.imread(image_path) #이미지 불러오기
    decoded_objects = decode(image) #이미지에서 바코드 검출
    
    if decoded_objects:
        for obj in decoded_objects:
            points = obj.polygon
            if len(points) > 4: #바코드 읽는 부분 표시
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                points = hull
            points = np.array(points, dtype=np.int32)
            cv2.polylines(image, [points], isClosed=True, color=(0, 0, 255), thickness=15)
            
            barcode_data = obj.data.decode('utf-8') #바코드 타입
            barcode_type = obj.type #바코드 번호
            print("바코드 추출중...")
            print(f"-바코드 타입: {barcode_type}, -바코드 번호: {barcode_data}")
            search_item(barcode_data)
            
        rs_img = cv2.resize(image, (400, 300)) #크기를 (400, 300)으로 설정   
        cv2.imshow("Barcode result Image", rs_img) #이미지를 화면에 표시
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    else:
        print("바코드를 찾을 수 없습니다.") #되면 다른것도 추가예정

def search_item(barcode_data): #Web scraping
    barcode_Num = barcode_data
    url = 'https://www.google.com/search?q={}'.format(barcode_Num)
    print("-물건 정보 : " + url)
    
def main(): #test_main
    image_path=""
    while True:
        print("-코드 경로 테스트 입니다.\n")
        print("-모드 설정: 1. 사진캡쳐 | 2. 사진업로드 | 3. 종료 ")
        print("-선택 >> ",end="")
        q1 = str(input())
        if q1 == '1':
            print("-타이머 설정: 1.O | 2.X >> ", end="")
            q2 = int(input())
            if q2 == 1:
                timer_cap.timer_main()
            else:
                normal_cap.nor_main()
        if q1 == '3':
            print("-종료합니다.")
            break
        print("-바코드 설정: 1. Barcode | 2. QRcode | 3. 종료 ")
        print("-선택 >> ",end="")
        choice = str(input())
        if choice == '1':
            image_path = input("-사진이름을 입력하시오 : ")
            Barcode_detection(image_path)
            break
        elif choice == '2':
            image_path = input("-사진이름을 입력하시오 : ")
            QRcode_detection(image_path)
            break
        elif choice == 'q' or choice == 'Q':
            print("-종료합니다.")
            break
        else:
            print("-해당되는 번호가 없습니다.\n다시 입력하시오.")
            continue