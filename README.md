# Face-Sense - Facial Recognition Attendance System
This project is a Facial Recognition Attendance System built using OpenCV, Face Recognition, and Firebase. It captures real-time video from a webcam, identifies students using their facial features, and records attendance automatically. The system leverages advanced facial recognition techniques with a Histogram of Oriented Gradients (HOG) for feature extraction and is integrated with Firebase for storing student data and attendance logs.

**Features**
1. Real-Time Face Recognition: Identifies and matches faces in real time using a webcam.
2. Student Database Integration: Stores and retrieves student information from Firebase Realtime Database.
3. Attendance Logging: Automatically records attendance based on facial recognition.
4. Cloud Storage: Saves student images and attendance records in Firebase Storage.
5. User-Friendly Interface: Displays real-time attendance and student details on a custom UI background.

# WorkFlow Diagram

![image](https://github.com/user-attachments/assets/7005a0ba-7a31-4c58-bb9c-34cc103a499a)

# User Interface

![image](https://github.com/user-attachments/assets/99e323eb-b1fa-403b-ab62-c6e737863e2a)

# Dataset

![image](https://github.com/user-attachments/assets/b3493826-dae4-42b1-8c61-1ae52e003369)


**Technologies Used**
1. OpenCV: For video capture and image processing.
2. Face Recognition Library: For facial feature detection and matching.
3. Firebase: For real-time database and cloud storage.
4. Python: Core programming language used for implementing the system


**Setup and Installation**
1. Clone the repository.
2. Install the required Python libraries from requirements.txt.
3. Set up Firebase and download the serviceAccountKey.json file.
4. Run addDataToDatabase.py to initialize the student database.
5. Execute EncodeGenerator.py to generate facial encodings.
6. Run main.py to start the real-time attendance system.


**Note**
  1. The project is designed for demonstration and educational purposes and may require further improvements for real-world applications.
  2. Ensure proper lighting and a clear view of the faces for better face recognition performance.
  3. Feel free to contribute to this project by creating pull requests or raising issues.



