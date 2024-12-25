import numpy as np
import tensorflow as tf

# Load the model
model = tf.keras.models.load_model("D:/pyconda/crack_mobilenetv3.h5")

# Prepare the test image and label
test_img = tf.keras.utils.load_img("D:/pyconda/crack-floor-scaled.jpeg", target_size=(150, 150, 3))  # Resize to model's input size
test_img_array = np.array(test_img) / 255.0  # Normalize to [0, 1]
test_img_array = np.expand_dims(test_img_array, axis=0)  # Add batch dimension

# Mock label for testing (replace with real labels for batch evaluation)
test_label = ["nocrack", "crack"]
# np.array([[1]])  # Assuming "1" represents "crack"

# Evaluate the model on the test sample
loss, accuracy = model.evaluate(test_img_array, test_label, verbose=0)
print(f"Loss: {loss}, Accuracy: {accuracy}")
# Make a prediction
prediction = model.predict(test_img_array)

# Interpret the prediction
if prediction[0][0] <= 0.5:  # Assuming a sigmoid activation in the output layer
    result = "No Crack"
    confidence = (1 - prediction[0][0]) * 100
else:
    result = "Crack"
    confidence = prediction[0][0] * 100

print(f"Prediction: {result}, Confidence: {confidence:.2f}%")