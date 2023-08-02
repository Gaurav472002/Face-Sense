# Face-Sense
This is a Python-based facial recognition attendance system created  using the OpenCV library in Python, that detects the attendance of users through facial recognition and stores the result in a .csv file. It eliminates the need for manual attendance tracking, ensuring accuracy and saving valuable time for both students and instructors.

**How to Use**
  1. Download or clone my Repository to your device
  2. type **pip install -r requirements.txt** in the command prompt(this will install the required packages for the project)
  3. open main.py and  change all the paths according to your system
  4. Run the **main.py** file

**Project Flow & Explanation**
 1. The project uses the default webcam (0) as the video stream source. Change this to 1 if you are using a secondary webcam.
 2. The known faces (students) are provided by adding their images to the faces directory. The face_encodings are computed and stored in the known_face_encodings list, and the names of the students are stored in the known_face_names list.
 3. The script continuously captures frames from the webcam and processes them for face recognition.
 4. Each frame is resized and converted to RGB format for compatibility with the face_recognition library.
 5. The faces in the frame are located and their facial encodings are computed.
 6. The facial encodings are compared with the known_face_encodings to recognize the known individuals.
 7. If a recognized face matches one of the known faces, the attendance for that student is marked and their name is displayed on the frame.
 8. The script also logs the name of the recognized student and the timestamp in a CSV file named according to the current date.
