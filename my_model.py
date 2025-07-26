import tensorflow as tf

# Load your .h5 model
model = tf.keras.models.load_model("my_model.h5")

# Convert to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the .tflite model
with open("model.tflite", "wb") as f:
    f.write(tflite_model)
