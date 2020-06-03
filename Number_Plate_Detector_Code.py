##Number Plate Detection


import cv2    #Importing package for Computer Vision

########################################################
frameWidth = 640
frameHeight = 480
minArea = 500
nPlateCascade = cv2.CascadeClassifier(r"C:\Users\USER\Desktop\OpenCvPython\venv\Lib\site-packages\cv2\data\haarcascade_russian_plate_number.xml")
color = (255, 0 ,255)
########################################################
cap = cv2.VideoCapture(0)  #Id for default is 0
cap.set(3, frameWidth)            #Id for height is 3
cap.set(4, frameHeight)             #Id for width is 4
cap.set(10,150)            #Id for brightness id 10
count = 0
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
             cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
             cv2.putText(img, "Number Plate", (x, y-5),
                         cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                         color, 2)
             imgRoi = img[y:y+h, x:x+w]
             cv2.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  #Press q to close
        cv2.imwrite("Resources/scanned/No.Plate_"+str(count)+".jpg", imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved", (150,265), cv2.FONT_HERSHEY_DUPLEX,
                    2,(0, 0, 255),2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count +=1