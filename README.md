# Image Processing Edge Detection Techniques

## Overview

This project explores various edge detection techniques in image processing. The primary objective is to apply different edge detection filters on an image and observe the results. The techniques implemented in `image_analysis.py` include Sobel, Scharr, Laplacian, and Canny edge detection. Additionally, the project evaluates the quality of the processed images using metrics defined in `metrics.py`, specifically focusing on compression ratio and Peak Signal-to-Noise Ratio (PSNR).

## Edge Detection Techniques

### Sobel Operator
The Sobel operator calculates the gradient of the image intensity, emphasizing edges. It uses convolution kernels to detect horizontal and vertical changes in intensity.

### Scharr Operator
The Scharr operator is a variant of the Sobel operator, designed to provide a more accurate gradient computation. It is particularly effective in detecting fine details and edges in noisy images.

### Laplacian Operator
The Laplacian operator detects edges by computing the second derivative of the image intensity. It highlights regions of rapid intensity change and is sensitive to noise.

### Canny Edge Detection
Canny edge detection is a multi-stage algorithm that detects a wide range of edges in images. It involves noise reduction, gradient calculation, non-maximum suppression, and edge tracking by hysteresis.

## Metrics and Evaluation

### Compression Ratio
The compression ratio measures the efficiency of compressing each filtered image. It is calculated as the ratio of the size of the original image to the size of the compressed image.

### Peak Signal-to-Noise Ratio (PSNR)
PSNR is used to measure the quality of the filtered images compared to the original image. It quantifies the difference between the original and processed images, with higher values indicating better quality.

## Implementation Details

### `image_analysis.py`
This script applies the Sobel, Scharr, Laplacian, and Canny edge detection filters to an input image. It processes the image and saves the results for further analysis.

### `metrics.py`
This script calculates the compression ratio and PSNR for each filtered image. It compares these metrics against the original image to evaluate the performance of each edge detection technique.

## Usage

1. **Image Processing**: Run `image_analysis.py` to apply edge detection filters on your input image.
   ```sh
   python image_analysis.py input_image.jpg
   ```

2. **Metrics Calculation**: Run `metrics.py` to compute the compression ratio and PSNR for the processed images.
   ```sh
   python metrics.py
   ```

## Results
The results include the processed images for each edge detection technique and the corresponding compression ratio and PSNR values. These results help in understanding the effectiveness and quality of each edge detection method.

## Dependencies
- Python 3.x
- OpenCV
- NumPy
