# ClassVision-Real-Time-Student-Engagement-Detector

**ClassVision** is an AI-powered real-time student engagement detector that uses **Computer Vision (CV) and Deep Learning** to analyze student attentiveness during online classes. It captures live webcam images, classifies student behavior using a trained deep learning model, and visualizes engagement patterns.

## 🚀 Features  
✅ **Real-time face analysis** using OpenCV  
✅ **Deep learning model (`keras_model.h5`) for behavior classification**  
✅ **Confidence score display** for predictions  
✅ **Live data visualization** with Matplotlib  

-----------------------------------------------------------

## **🛠 Technologies Used**

| Technology        | Purpose |
|------------------|---------|
| **Python**       | Backend scripting |
| **Keras**        | Loading deep learning model (`keras_model.h5`) |
| **TensorFlow**   | Underlying deep learning framework |
| **OpenCV**       | Webcam input and image processing |
| **NumPy**        | Data handling and normalization |
| **Matplotlib**   | Visualization of student behavior |

------------------------------------------------------------

## **📥 Installation & Usage**
### **1️⃣ Clone the Repository**

git clone https://github.com/arham952/ClassVision-Real-Time-Student-Engagement-Detector.git
cd ClassVision-Real-Time-Student-Engagement-Detector
2️⃣ Install Dependencies
Ensure you have Python installed, then install required libraries:

pip install tensorflow keras opencv-python numpy matplotlib

3️⃣ Run the Application

Run the script to start real-time engagement detection:
python main.py
4️⃣ Exit the Program
Press ESC to stop the application.

📊 How It Works

1️⃣ Captures webcam frames using OpenCV 
2️⃣ Preprocesses image: Resizes to 224x224, normalizes pixel values
3️⃣ Loads pre-trained Keras model (keras_model.h5)
4️⃣ Predicts student behavior & confidence score
5️⃣ Visualizes behavior distribution using Matplotlib

🎯 Model Output Example

Press ESC to stop!!
Confidence Score: 0.92
Class: Present

⚠ Troubleshooting
If you get "No module named keras", install dependencies using:

pip install keras tensorflow
If the webcam doesn’t open, check your camera permissions.

👨‍💻 Contributing
Pull requests are welcome! Fork the repo and submit improvements.

📩 Contact
👤 Muhammad Arham
📧 Email: m.arham1264@gmail.com
🔗 LinkedIn: linkedin.com/in/muhammad-arham-95b8331a4
