import cv2 as cv
import numpy as np 

# Load the color image
img_color = cv.imread('original.jpg')
cv.imshow("original image",img_color)
# Convert the color image to grayscale image
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)



# Define the scaling factor: 5 scales for 5 resized images
scale_percent1 = 25  # 25% of the original size
scale_percent2 = 50  # 50% of the original size
scale_percent3 = 75  # 75% of the original size
scale_percent4 = 150  # 150% of the original size
scale_percent5 = 200  # 200% of the original size
scale_percent6 = 100 #100% of the original size

# Calculate the new dimensions: 5 resized dimensions: 25%, 50%, 75% , 150%, 200%
#resize 1
width1 = int(img_gray.shape[1] * scale_percent1 / 100)
height1 = int(img_gray.shape[0] * scale_percent1 / 100)
dim1= (width1, height1)

#resize 2
width2 = int(img_gray.shape[1] * scale_percent2 / 100)
height2 = int(img_gray.shape[0] * scale_percent2 / 100)
dim2= (width2, height2)

#resize 3
width3 = int(img_gray.shape[1] * scale_percent3 / 100)
height3 = int(img_gray.shape[0] * scale_percent3 / 100)
dim3= (width3, height3)

#resize 4
width4 = int(img_gray.shape[1] * scale_percent4 / 100)
height4 = int(img_gray.shape[0] * scale_percent4 / 100)
dim4= (width4, height4)

#resize 5
width5 = int(img_gray.shape[1] * scale_percent5 / 100)
height5 = int(img_gray.shape[0] * scale_percent5 / 100)
dim5= (width5, height5)

#resize 6
width6 = int(img_gray.shape[1] * scale_percent6 / 100)
height6 = int(img_gray.shape[0] * scale_percent6 / 100)
dim6= (width6, height6)

# Resize the image using the new dimensions
resized_img1 = cv.resize(img_gray, dim1, interpolation=cv.INTER_AREA)
resized_img2 = cv.resize(img_gray, dim2, interpolation=cv.INTER_AREA)
resized_img3 = cv.resize(img_gray, dim3, interpolation=cv.INTER_AREA)
resized_img4 = cv.resize(img_gray, dim4, interpolation=cv.INTER_AREA)
resized_img5 = cv.resize(img_gray, dim5, interpolation=cv.INTER_AREA)
resized_greyscale = cv.resize(img_gray, dim6, interpolation=cv.INTER_AREA)


# cv.imshow("resized image 25%",resized_img1)
# cv.imshow("resized image 50%",resized_img2)
# cv.imshow("resized image 75%",resized_img3)
# cv.imshow("resized image 150%",resized_img4)
# cv.imshow("resized image 200%",resized_img5)
cv.imshow("resized image 100%",resized_greyscale)

#Save the processed image to tagged image file format (TIFF)
cv.imwrite('grayscale.tiff', resized_greyscale)


used_image = cv.imread('original.jpg',cv.IMREAD_GRAYSCALE)


#sobel 3-5-7-9-11

#3
# Apply the Sobel filter to the image
sobelx3 = cv.Sobel(used_image, cv.CV_8U, 1, 0, ksize=3)
sobely3= cv.Sobel(used_image, cv.CV_8U, 0, 1, ksize=3)
sobel3 = cv.bitwise_or(sobelx3, sobely3)


# cv.imshow('Sobel X 3', sobelx3)
# cv.imshow('Sobel Y 3', sobely3)
cv.imshow('Sobel 3x3 Combined', sobel3)

# Save as TIFF file
cv.imwrite('sobel3x3.tiff', sobel3)

# Save as TIFF file
# cv.imwrite('sobel3x3.tiff', sobel3, [cv.IMWRITE_TIFF_COMPRESSION, 2])

#5
# Apply the Sobel filter to the image
sobelx5 = cv.Sobel(resized_greyscale, cv.CV_8U, 1, 0, ksize=5)
sobely5= cv.Sobel(resized_greyscale, cv.CV_8U, 0, 1, ksize=5)
sobel5 = cv.bitwise_or(sobelx5, sobely5)


# cv.imshow('Sobel X 5', sobelx)
# cv.imshow('Sobel Y 5', sobely)
cv.imshow('Sobel 5x5 Combined', sobel5)

# Save as TIFF file
cv.imwrite('sobel5x5.tiff', sobel5)

#7
# Apply the Sobel filter to the image
sobelx7 = cv.Sobel(resized_greyscale, cv.CV_8U, 1, 0, ksize=7)
sobely7= cv.Sobel(resized_greyscale, cv.CV_8U, 0, 1, ksize=7)
sobel7 = cv.bitwise_or(sobelx7, sobely7)


# cv.imshow('Sobel X 7', sobelx7)
# cv.imshow('Sobel Y 7', sobely7)
cv.imshow('Sobel 7x7 Combined', sobel7)

# Save as TIFF file
cv.imwrite('sobel7x7.tiff', sobel7)

#9

# Apply the Sobel filter to the image
sobelx9 = cv.Sobel(resized_greyscale, cv.CV_8U, 1, 0, ksize=9)
sobely9= cv.Sobel(resized_greyscale, cv.CV_8U, 0, 1, ksize=9)
sobel9 = cv.bitwise_or(sobelx9, sobely9)


# cv.imshow('Sobel X 3', sobelx9)
# cv.imshow('Sobel Y 3', sobely9)
cv.imshow('Sobel 9x9 Combined', sobel9)

# Save as TIFF file
cv.imwrite('sobel9x9.tiff', sobel9)

#11

# Apply the Sobel filter to the image
sobelx11 = cv.Sobel(resized_greyscale, cv.CV_8U, 1, 0, ksize=11)
sobely11= cv.Sobel(resized_greyscale, cv.CV_8U, 0, 1, ksize=11)
sobel11 = cv.bitwise_or(sobelx11, sobely11)


# cv.imshow('Sobel X 11', sobelx11)
# cv.imshow('Sobel Y 11', sobely11)
cv.imshow('Sobel 11x11 Combined', sobel11)

# Save as TIFF file
cv.imwrite('sobel11x11.tiff', sobel11)


#scharr dx dy 1 , it is advisable to change to laplacian filter if you want to raise the derivative values to more than 1. 
# Apply Scharr edge detection

#1

scharrx1 = cv.Scharr(resized_greyscale, cv.CV_8U, 1, 0)
scharry1 = cv.Scharr(resized_greyscale, cv.CV_8U, 0, 1)

# Combine the x and y gradient images
scharr_combined1 = cv.bitwise_or(scharrx1, scharry1)

# Display the original and Scharr images
# cv.imshow('Scharr X 1', scharrx)
# cv.imshow('Scharr Y 1', scharry)
cv.imshow('Scharr 1 Combined', scharr_combined1)

cv.imwrite('scharr1.tiff', scharr_combined1)


#laplacian ksizes; 3-5-7-9-11
#3

laplacian3 = cv.Laplacian(resized_greyscale, cv.CV_8U, ksize=3)

# Display the original and Laplacian images
cv.imshow('Laplacian 3x3', laplacian3)
cv.imwrite('Laplacian3x3.tiff', laplacian3)
#5

laplacian5 = cv.Laplacian(resized_greyscale, cv.CV_8U, ksize=5)

# Display the original and Laplacian images
# cv.imshow('Laplacian 5x5', laplacian5)
cv.imwrite('Laplacian5x5.tiff', laplacian5)

#7
laplacian7 = cv.Laplacian(resized_greyscale, cv.CV_8U, ksize=7)

# Display the original and Laplacian images
# cv.imshow('Laplacian 7x7', laplacian7)
cv.imwrite('Laplacian7x7.tiff', laplacian7)

#9
laplacian9 = cv.Laplacian(resized_greyscale, cv.CV_8U, ksize=9)

# Display the original and Laplacian images
# cv.imshow('Laplacian 5x5', laplacian5)
cv.imwrite('Laplacian9x9.tiff', laplacian9)

#11

laplacian11 = cv.Laplacian(resized_greyscale, cv.CV_8U, ksize=11)

# Display the original and Laplacian images
cv.imshow('Laplacian 5x5', laplacian5)
cv.imwrite('Laplacian11x11.tiff', laplacian11)

#canny with combination of max and mind thresholds of max-min; 50-150, 50-100, 150-150, 20-150, 20-100

# Apply Canny edge detection with threshold values of 50 and 150
edges50150 = cv.Canny(resized_greyscale, 50, 150)

# Display the original and Canny edge images
cv.imshow('Canny Edges 50x150', edges50150)
cv.imwrite('Canny_Edges50x150.tiff', edges50150)

# 50-100
# Apply Canny edge detection with threshold values of 50 and 100
edges50100 = cv.Canny(resized_greyscale, 50, 100)

# Display the original and Canny edge images
# cv.imshow('Canny Edges 50x100', edges50100)
cv.imwrite('Canny_Edges50x100.tiff', edges50100)

#150-150
# Apply Canny edge detection with threshold values of 150 and 150
edges150150 = cv.Canny(resized_greyscale, 150, 150)

# Display the original and Canny edge images
# cv.imshow('Canny Edges 150x150', edges150150)
cv.imwrite('Canny_Edges150x150.tiff', edges150150)

#20-150
# Apply Canny edge detection with threshold values of 20 and 150
edges20150 = cv.Canny(resized_greyscale, 20, 150)

# Display the original and Canny edge images
# cv.imshow('Canny Edges 20x150', edges20150)
cv.imwrite('Canny_Edges20x150.tiff', edges20150)

#20-100
# Apply Canny edge detection with threshold values of 20 and 100
edges20100 = cv.Canny(resized_greyscale, 20, 100)

# Display the original and Canny edge images
# cv.imshow('Canny Edges 20x100', edges20100)
cv.imwrite('Canny_Edges20x100.tiff', edges20100)

cv.waitKey(0)
cv.destroyAllWindows()