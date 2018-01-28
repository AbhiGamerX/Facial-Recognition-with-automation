import sys
import time import sleep
import Rpi.GPIO as GPIO
import face_recognition
import cv2
video_capture = cv2.VideoCapture(0)
abhi_image = face_recognition.load_image_file("abhi.jpg")
abhi_face_encoding = face_recognition.face_encodings(abhi_image)[0]
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding
]
known_face_names = [
    "Abhijit"
]
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Abhijit"
		DIR=20
	STEP=21
	CW=1
	CCW=0
	SPR=12 #90/7.5
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(DIR,GPIO.OUT)
	GPIO.setup(STEP,GPIO.OUT)
	GPIO.output(DIR,CW)
	step_count=SPR
	delay=0.833 #1/12
	for x in range(step_count):
		GPIO.output(STEP,GPIO.HIGH)
		sleep(delay)
		GPIO.output(STEP,GPIO.LOW)
		sleep(delay)
	sleep(5)
	GPIO.outdoor(DIR,CCW)
	for x in range(step_down)
		GPIO.output(STEP,GPIO.HIGH)
		sleep(delay)
		GPIO.output(STEP,GPIO.LOW)
		sleep(delay)
	GPIO.cleanup()
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
