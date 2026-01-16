import cv2
from ultralytics import YOLO

# Load the model (change path if needed)
model = YOLO(r"runs\optuna_trial_1\weights\best.onnx")

# Load an image with OpenCV
img_path = r"safety-helmet-1\test\images\download-6-_jpeg.rf.ed509408e743c666385b9b1d83d12033.jpg"  # ← Replace with your image path
image = cv2.imread(img_path)

# Run inference
results = model(image)

# Annotate the image with bounding boxes and labels
annotated_frame = results[0].plot()

# Show result using OpenCV
cv2.imshow("YOLOv8 Inference", annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
