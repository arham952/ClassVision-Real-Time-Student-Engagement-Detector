
from keras.models import load_model
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on the default camera of your computer
camera = cv2.VideoCapture(0)

# Initialize behavior counts
behavior_counts = {class_name[2:]: 0 for class_name in class_names}

while True:

    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the model's input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predict the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Update behavior counts
    behavior_counts[class_name[2:]] += 1

    # Print prediction and confidence score
    print("Press ESC to stop!!")
    print("Confidence Score:", confidence_score)
    print("Class:", class_name[2:])


    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()

# Extract behavior names and counts
behaviors = list(behavior_counts.keys())
counts = list(behavior_counts.values())

# Plot the bar chart
plt.bar(behaviors, counts)
plt.xlabel("Behavior")
plt.ylabel("Count")
plt.title("Behavior Distribution")
plt.show()
