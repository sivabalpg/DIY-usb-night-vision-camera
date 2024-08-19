import cv2 as cv
cap = cv.VideoCapture('D:/DATA/DATA D/Opencv/ImageTransforms/WIN_20240224_21_40_27_Pro.mp4')


while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    im_color= cv.applyColorMap(gray, cv.COLORMAP_JET)
    cv.imshow('frame', im_color)
    if cv.waitKey(100) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()