# 🚗 AI Drowsiness Detection System
### Version 1.0.0

A real-time AI-based driver monitoring system that detects drowsiness using computer vision and deep learning techniques.  
Designed with a professional fullscreen UI, alert system, and installer-ready Windows distribution.

---

## 📌 Overview

Driver fatigue is one of the leading causes of road accidents worldwide.  
This project uses real-time face and eye detection to monitor driver alertness and trigger warnings when signs of drowsiness are detected.

The system is built using:

- OpenCV
- Haarcascade classifiers
- Deep Learning model (.h5)
- Python
- Custom Professional UI
- Windows EXE Packaging with Installer

---

## 🎯 Key Features

✔ Real-time face detection  
✔ Eye closure monitoring  
✔ Drowsiness time tracking  
✔ Blinking alert warning system  
✔ Professional fullscreen camera UI  
✔ Glow border + Live indicator  
✔ FPS counter  
✔ Loading animation screen  
✔ Custom application icon  
✔ Versioned executable (1.0.0)  
✔ Windows Setup Installer  

---

## 🖥️ User Interface Highlights

- Cinematic intro screen  
- Fade transition effect  
- Loading progress animation  
- Live camera monitoring interface  
- Status panel with alert detection  
- Blinking warning message  
- Border glow effect  
- Clean and professional layout  

---

## 🧠 AI Detection Logic

The system detects:

1. Face using Haarcascade frontal face classifier
2. Eyes using Haarcascade eye classifier
3. Eye closure duration tracking
4. Alert trigger if eyes remain closed beyond threshold time

Optional model-based prediction using trained `.h5` deep learning model.

---

## 📂 Project Structure

AI_Drowsiness_Detection/
│
├── assets/
│   ├── icon.ico
│   └── logo.png
│
├── model/
│   └── drowsiness_model.h5
│
├── haarcascade_frontalface_default.xml
├── haarcascade_eye.xml
│
├── main.py
├── version.txt
├── README.md

---

## ⚙️ Installation (Windows Users)

### Option 1 – Direct EXE Download

1. Go to **Releases** section of this repository
2. Download the latest version (v1.0.0)
3. Run `AI_Drowsiness.exe`
4. Click **START**
5. Press **Q** to exit

No Python installation required.

---

### Option 2 – Setup Installer

1. Download the Setup Installer from Releases
2. Run installer
3. Choose install location
4. Launch from Desktop shortcut

---

## 🛠️ Technologies Used

- Python 3.10
- OpenCV 4.x
- NumPy
- TensorFlow / Keras (for .h5 model)
- PyInstaller (EXE packaging)
- Inno Setup (Installer creation)

---

## 🔔 Alert System

The system triggers alert when:

- Eye closure exceeds defined threshold time
- No face detected beyond safety duration

Warning displayed with:
- Blinking red alert text
- Audio beep alarm
- Visual border glow effect

---

## 📊 Performance

- Real-time video processing
- FPS counter displayed on UI
- Optimized for smooth execution

---

## 🚀 Future Improvements

- Eye Aspect Ratio (EAR) based detection
- MediaPipe facial landmark integration
- TensorFlow Lite mobile version
- Event logging system
- Multi-level alert system
- Cloud analytics dashboard

---

## 👨‍💻 Developer

Developed by:  
**[Dharnesh Priyan J]**

Project Type:  
Final Year / AI Computer Vision Project

---

## 📜 License

This project is developed for academic and educational purposes.

---

## ⭐ Support

If you found this project useful:

- Star the repository
- Share with your team
- Provide feedback

---

## 📌 Disclaimer

This system is intended as a driver assistance tool.  
It does not replace responsible driving behavior.
