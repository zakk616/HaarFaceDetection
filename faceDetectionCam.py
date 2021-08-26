import cv2

video_capture = cv2.VideoCapture("'rtsp://admin:Junaid_Sadia@169.254.93.5:554/Streaming/Channels/102'")

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
        
    if ret:
        cv2.resize(frame, (224, 224))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow('Video', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    

video_capture.release()
cv2.destroyAllWindows()
cv2.waitKey()
