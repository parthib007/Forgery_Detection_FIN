import cv2
import numpy as np

# Load the heat map image
heatmap = cv2.imread('d:/Parthib Das/Desktop/detect/heatmap3.png')

if heatmap is None:
    print("Error: Image not found or cannot be loaded.")
    exit()

# Convert the heat map to grayscale
gray = cv2.cvtColor(heatmap, cv2.COLOR_BGR2GRAY)

# Threshold the grayscale image to create a binary mask (detect high-value regions)
# Adjust the threshold value as needed (e.g., 200)
_, thresh = cv2.threshold(gray, 25 , 255, cv2.THRESH_BINARY)

# Find contours of the high-value regions
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw red bounding boxes around the contours
for contour in contours:
    # Get the bounding box for each contour
    x, y, w, h = cv2.boundingRect(contour)
    # Draw the red rectangle (BGR: (0, 0, 255) for red)
    cv2.rectangle(heatmap, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Display the result
cv2.imshow('Forged Areas Detected', heatmap)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the output if needed
cv2.imwrite('heatmap_with_boxes.png', heatmap)