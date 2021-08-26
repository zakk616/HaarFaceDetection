import cv2
from PIL import Image

# video_capture = cv2.VideoCapture(0)               #for webCam
# video_capture = cv2.VideoCapture("rtsp://admin:Junaid_Sadia@169.254.93.5:554/Streaming/Channels/102")
video_capture = cv2.VideoCapture("rtsp://192.168.1.10:554/live/ch00_0")

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:
        width, height = Image.fromarray(frame).size
        imS = cv2.resize(frame, (width//1, height//1))
        cv2.imshow('Video', imS)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
