import cv2
import numpy as np

from models.image_processing_task import ImageModification

# Split an image into multiple equal parts horizontally
def split_image(image_filepath, divisions):
    
    # Load image using OpenCV
    img = cv2.imread(image_filepath)
    # Extract image width and height
    img_height, img_width = img.shape[:2]

    # Calculate width of each image slice based on number of divisions
    slice_width = img_width // divisions

    # Create an empty list to store image slices
    slices = []
    for index in range(divisions):
        # Calculate starting and ending coordinates for slicing
        x_start = index * slice_width
        x_end = x_start + slice_width

        # Slice image and add to list
        img_slice = img[:, x_start:x_end]
        slices.append(img_slice)

    # Convert list of slices to a numpy array
    slices_array = np.stack(slices)

    return slices_array

# Image transformations and filters

# Apply Canny edge detection to an image slice
def detect_edges(slice):
    # Parameters set for Canny algorithm
    return cv2.Canny(slice, 100, 200)

# Apply Gaussian blur to an image slice
def blur(slice):
    # Blur with a 5x5 kernel
    return cv2.GaussianBlur(slice, (5, 5), 0)

# Increase the brightness of an image slice
def enhance_brightness(slice, intensity=3):
    # Create an array with the brightness increase value
    brightness_incr = np.full(slice.shape, intensity, dtype=np.uint8)
    enhanced_slice = cv2.add(slice, brightness_incr)
    return enhanced_slice

# Apply image filter based on modification type
def modify_image(modification_type: ImageModification, segment):
    if modification_type == ImageModification.BLUR:
        # Inversion achieved through blurring as a placeholder
        return blur(segment)
    elif modification_type == ImageModification.EDGE_DETECTION:
        # Apply edge detection to segment
        return detect_edges(segment)
    elif modification_type == ImageModification.ENHANCE_BRIGHTNESS:
        # Brighten the segment with a small intensity increase
        return enhance_brightness(segment)
    
    # If no operation is matched, return original segment
    return segment
