# Import the required modules for the project

import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

#   sets up the video stream to read frames from the webcam as we are going do to use the default webcam use 0 .
video_capture = cv2.VideoCapture(0)

# load known faces , extracts facial features and creates a numerical representation (encoding) of each face.
gaurav_image = face_recognition.load_image_file("faces/student1.jpg")
gaurav_encoding = face_recognition.face_encodings(gaurav_image)[0]



# store the obtained encodings in known_face_encodings list 
known_face_encodings = [gaurav_encoding]
# store the expected student names in the known_face_names list
known_face_names = ["student1" ]


# List of Expected Students which will be used to track the expected students and mark their attendance

students = known_face_names.copy()

face_locations = []
face_encodings = []

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Create a CSV file and name it according to present date
f = open(f"{current_date}.csv", "w+", newline="")
# create the object writer to write data into the csv file
lnwriter = csv.writer(f)



'''This is the main loop that continuously reads frames from the webcam. 
The frame is first resized to a smaller resolution (25% of the original size) to speed up face recognition processing.
 The frame is then converted from BGR to RGB, as face_recognition library works with RGB images.'''
while True:

    

    '''Here, video_capture is the OpenCV VideoCapture object that represents the webcam stream. The read() function is used to read the next frame from the webcam. The read() function returns two values: a boolean value (True if the frame was read successfully, False otherwise) and the actual frame itself.

    In the line, the _ is used as a throwaway variable, meaning we are not interested in storing the boolean value returned by video_capture.read(). Instead, we directly assign the frame to the variable frame.'''
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # RECOGNIZE FACES

    '''The face_recognition library is used to locate faces in the rgb_small_frame. 
    The face_locations list will contain the bounding box coordinates of each detected face. 
    Then, the facial encodings of the detected faces are computed and stored in the face_encodings list.'''

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(
        rgb_small_frame, face_locations)


    '''For each face detected in the frame,  compares the face encoding with the known face encodings to check for a match. 
    The face_recognition.compare_faces function returns a list of boolean values, indicating whether each known face matches the detected face. The face_recognition.face_distance function returns an array of distances between the detected face and the known faces. 
    The np.argmin function finds the index of the smallest distance, indicating the best match. '''
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        '''If there is a match  the detected face is recognized as one of the known faces
        the name of the person is assigned based on the index of the best match. '''
        if (matches[best_match_index]):
            name = known_face_names[best_match_index]

        # Add the text if a person is present
        # If the recognized face belongs to one of the known individuals, their name is written on the frame, indicating that they are present.
        
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name+" Present  ", bottomLeftCornerOfText,
                        font, fontScale, fontColor, thickness, lineType)

            if name in students:
                # remove the name of the student marked present from the list of expected students whose attendace is already marked
                students.remove(name)
                current_time = now.strftime("%H:%M:%S")
                lnwriter.writerow([name, current_time])


    '''The frame with the attendance information is displayed in a window. 
    The loop continues until the user presses the 'q' key, at which point the loop is terminated, and the program  stops.'''
    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Finally, the webcam is  released, the OpenCV windows are closed, and the CSV file is closed.
video_capture.release()
cv2.destroyAllWindows()
f.close()
