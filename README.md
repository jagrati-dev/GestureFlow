# GestureFlow – AI Based Hand Gesture Control System

GestureFlow is an AI-based hand gesture control application that allows users to interact with their computer using real-time hand gestures through a webcam.

The system uses Computer Vision and MediaPipe to detect hand landmarks and recognize gestures, enabling touchless computer interaction.

## 🚀 Features

- Real-time hand detection using a webcam.
- Hand landmark tracking using MediaPipe.
- AI-based hand gesture recognition.
- Touchless computer control.
- Gesture-based system actions.
- Login and Signup using Firebase Authentication.
- Google Sign-In integration.
- User dashboard for application navigation.

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- CustomTkinter
- Firebase Authentication
- Google OAuth
- PyAutoGUI

## 📁 Project Structure

```text
GestureFlow/
│
├── main.py
├── auth_app.py
├── auth_service.py
├── home_dashboard.py
├── gesture_logic.py
├── finger_detection.py
├── hand_detection.py
├── hand_landmarker.task
├── models/
│   └── hand_detection.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/jagrati-dev/GestureFlow.git
```

### 2. Open the project folder

```bash
cd GestureFlow
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Authentication

Configure Firebase Authentication and Google Sign-In using your own Firebase project credentials and OAuth configuration.

Keep private credentials outside the public repository.

### 7. Run the application

```bash
python auth_app.py
```

## 💻 System Requirements

- Windows operating system
- Python 3.x
- Webcam
- Internet connection for authentication
- VS Code or any Python IDE

## 🎯 Project Objective

The main objective of GestureFlow is to provide a touchless and user-friendly computer interaction system using hand gestures, Computer Vision and AI-based technologies.

## 🔮 Future Scope

- Support for additional hand gestures.
- Improved gesture recognition accuracy.
- Integration with smart home and IoT devices.
- Enhanced real-time interaction.

## 👩‍💻 Developer

**Jagrati Patel**

GitHub: https://github.com/jagrati-dev

---

⭐ If you find this project interesting, feel free to explore the repository!
