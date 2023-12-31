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

**CSV File Format**

  1. The attendance data is stored in CSV format in a file named with the current date (e.g., 2023-08-02.csv).
  2. The file has two columns: "Name" and "Time." The "Name" column contains the names of the students whose attendance is marked, and the "Time" column contains the timestamp when the attendance was marked.


**Project Demo**

Whenever a valid student is recognized the student is present message is displayed ensuring that the attendance is marked
![image](https://github.com/Gaurav472002/Face-Sense/assets/97028366/435c6acb-f3da-4949-b3f1-1ac61656effb)

The attendance is stored in the following format

![image](https://github.com/Gaurav472002/Face-Sense/assets/97028366/6d84b16b-a6de-412e-a3e6-2ad1da89bccd)

The .csv file is saved using the present date so that the user can keep track of the attendance for different days accordingly.

![image](https://github.com/Gaurav472002/Face-Sense/assets/97028366/6e94f625-220c-4745-9724-bb7b98fa83b8)


**Note**
  1. The project is designed for demonstration and educational purposes and may require further improvements for real-world applications.
  2. Make sure to have proper lighting and a clear view of the faces for better face recognition performance.
  3. Feel free to contribute to this project by creating pull requests or raising issues.



