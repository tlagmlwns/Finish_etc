from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from pyzbar.pyzbar import decode
import os
import cv2
import numpy as np

app = Flask(__name__)

# 업로드된 이미지를 저장할 디렉토리 설정
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# HTML 템플릿을 렌더링하는 라우트
@app.route('/', methods=['POST'])
def home():
    return render_template('index_test.html')

# 이미지 업로드 및 작업 선택
@app.route('/detect', methods=['POST'])
def detect_code():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if request.method == 'POST' and request.is_json:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image_path)
        
        data = request.get_json()
        action = data.get('action')

        if action == 'detect_qr_code':
            qr_code_data = QRcode_detection(image_path)
            return jsonify(result=qr_code_data)
        elif action == 'detect_bar_code':
            barcode_data = Barcode_detection(image_path)
            return jsonify(result=barcode_data)
        elif action == 'detect_etc_code':
            # 다른 작업을 수행하는 함수 호출
            # 여기에 다른 작업을 처리하는 코드를 추가하세요.
            pass

    return jsonify(result="No code data found.")

# QR 코드 검출 함수
def QRcode_detection(image_path):
    qr_code_image = cv2.imread(image_path)
    decoded_objects = decode(qr_code_image)

    if decoded_objects:
        for obj in decoded_objects:
            points = obj.polygon
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                points = hull
            points = np.array(points, dtype=np.int32)
            cv2.polylines(qr_code_image, [points], isClosed=True, color=(0, 0, 255), thickness=20)

            qr_code_data = obj.data.decode('utf-8')
            return qr_code_data

        rs_img = cv2.resize(qr_code_image, (400, 400))
        cv2.imshow("QRcode result Image", rs_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        return "QR code not found."

# 바코드 검출 함수
def Barcode_detection(image_path):
    image = cv2.imread(image_path)
    decoded_objects = decode(image)

    if decoded_objects:
        for obj in decoded_objects:
            points = obj.polygon
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                points = hull
            points = np.array(points, dtype=np.int32)
            cv2.polylines(image, [points], isClosed=True, color=(0, 0, 255), thickness=20)

            barcode_data = obj.data.decode('utf-8')
            barcode_type = obj.type
            print("Barcode detected...")
            print(f"-Barcode Type: {barcode_type}, -Barcode Data: {barcode_data}")
            search_item(barcode_data)

        rs_img = cv2.resize(image, (400, 300))
        cv2.imshow("Barcode result Image", rs_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return barcode_data
    else:
        return "Barcode not found."

# 상품 정보 검색 함수 (Web scraping)
def search_item(barcode_data):
    barcode_Num = barcode_data
    url = 'https://www.google.com/search?q={}'.format(barcode_Num)
    #print("-Product Info: " + url)
    return url

if __name__ == '__main__':
    app.run(debug=True)
