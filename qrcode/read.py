import cv2

def read_qr_code():

    cap = cv2.VideoCapture(0)

    while True:

        _, frame = cap.read()

        # Display the video stream with the detected faces and recognized names
        cv2.imshow('Frame', frame)

        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(frame)

        if len(value) > 0:
            return value 
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

value = read_qr_code()
print(value)