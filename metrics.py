from math import log10, sqrt
import cv2 as cv
import numpy as np
import os


#func to calculate psnr
def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

#func to calculate compression ratio for colored picture
def compressionRatioColor(img, filename):
	# Get the height , width & number of channels in image data object.
    rows, cols, channels = img.shape
	
    # Compute the uncompressed size or the original size.
    oi = rows * cols * channels # Size in byte
    print("Uncompressed size: ", oi, "bytes")
	
    # Retrieve the compressed size or the physical size.
    info = os.stat(filename)
    print("Compressed size: ", info.st_size, "bytes")
	
	# Compute the compression ratio.
    cr = float(info.st_size)/oi
    print("Compressed ratio: ", cr)
	
    crPercent = cr*100 # Convert ratio to percentage
    print("Compression ratio in percentage: ", crPercent,"%")


# func to calculate compression ratio of grescaled image
def compressionRatioGray(img, filename):
	print("Uncompressed size: ", img.shape, "bytes")
	
	# Retrieve the compressed size or the physical size.
	info = os.stat(filename)
	print("Compressed size: ", info.st_size, "bytes")
	
	# Compute the compression ratio.
	cr = float(info.st_size)/img.size
	print("Compressed ratio: ", cr)
	
	crPercent = cr*100 # Convert ratio to percentage
	print("Compression ratio in percentage: ", crPercent,"%")



# images file name (must be in same python folder or must provide full path/directory)
# read the images in grayscale except the original

#original image
image_original  = "original.jpg"
original = cv.imread(image_original)

#grayscale image
image_grayscale = "grayscale.tiff"
grayscale = cv.imread(image_grayscale,cv.IMREAD_GRAYSCALE)

#sobel images
image_sobel3x3 = "sobel3x3.tiff"
sobel3x3 = cv.imread(image_sobel3x3,cv.IMREAD_GRAYSCALE)

image_sobel5x5 = "sobel5x5.tiff"
sobel5x5=cv.imread(image_sobel5x5,cv.IMREAD_GRAYSCALE)

image_sobel7x7 ="sobel7x7.tiff"
sobel7x7 = cv.imread(image_sobel7x7,cv.IMREAD_GRAYSCALE)

image_sobel9x9 ="sobel9x9.tiff"
sobel9x9 = cv.imread(image_sobel9x9,cv.IMREAD_GRAYSCALE)

image_sobel11x11="sobel11x11.tiff"
sobel11x11 = cv.imread(image_sobel11x11,cv.IMREAD_GRAYSCALE)

#scharr images
image_scharr1 = "scharr1.tiff"
scharr1 = cv.imread(image_scharr1,cv.IMREAD_GRAYSCALE)

#laplacian images
image_laplacian3 = "Laplacian3x3.tiff"
laplacian3 = cv.imread(image_laplacian3,cv.IMREAD_GRAYSCALE)

image_laplacian5 ="Laplacian5x5.tiff"
laplacian5 = cv.imread(image_laplacian5,cv.IMREAD_GRAYSCALE)

image_laplacian7="Laplacian7x7.tiff"
laplacian7 = cv.imread(image_laplacian7,cv.IMREAD_GRAYSCALE)

image_laplacian9="Laplacian9x9.tiff"
laplacian9 = cv.imread(image_laplacian9,cv.IMREAD_GRAYSCALE)

image_laplacian11="Laplacian11x11.tiff"
laplacian11 = cv.imread(image_laplacian11,cv.IMREAD_GRAYSCALE)

#cannyedges images
image_cannyedges20100 = "Canny_Edges20x100.tiff"
cannyedges20100 = cv.imread(image_cannyedges20100,cv.IMREAD_GRAYSCALE)

image_cannyedges20150 ="Canny_Edges20x150.tiff"
cannyedges20150 = cv.imread(image_cannyedges20150,cv.IMREAD_GRAYSCALE)

image_cannyedges50100 ="Canny_Edges50x100.tiff"
cannyedges50100 = cv.imread(image_cannyedges50100,cv.IMREAD_GRAYSCALE)

image_cannyedges50150 ="Canny_Edges50x150.tiff"
cannyedges50150 = cv.imread(image_cannyedges50150,cv.IMREAD_GRAYSCALE)

image_cannyedges150150 ="Canny_Edges150x150.tiff"
cannyedges150150  = cv.imread(image_cannyedges150150,cv.IMREAD_GRAYSCALE)


#compression ratio original image
print('===Compression Ratio of original picture===')
compressionRatioColor(original, image_original)


#compression ratio of grayscale image
print('===Compression Ratio of grayscale picture===')
compressionRatioGray(grayscale, image_grayscale)


#compression ratio of sobel images
print('===Compression Ratio of sobel 3x3 picture===')
compressionRatioGray(sobel3x3, image_sobel3x3)
print('===Compression Ratio of sobel 5x5 picture===')
compressionRatioGray(sobel5x5, image_sobel5x5)
print('===Compression Ratio of sobel 7x7 picture===')
compressionRatioGray(sobel7x7, image_sobel7x7)
print('===Compression Ratio of sobel 9x9 picture===')
compressionRatioGray(sobel9x9, image_sobel9x9)
print('===Compression Ratio of sobel 11x11 picture===')
compressionRatioGray(sobel11x11, image_sobel11x11)


#compression ratio of schar image
print('===Compression Ratio of scharr dx, dy = 1 picture===')
compressionRatioGray(scharr1, image_scharr1)

#compression ratio of laplacian images
print('===Compression Ratio of laplacian 3x3 picture===')
compressionRatioGray(laplacian3, image_laplacian3)
print('===Compression Ratio of laplacian 5x5 picture===')
compressionRatioGray(laplacian5, image_laplacian5)
print('===Compression Ratio of laplacian 7x7 picture===')
compressionRatioGray(laplacian7, image_laplacian7)
print('===Compression Ratio of laplacian 9x9 picture===')
compressionRatioGray(laplacian9, image_laplacian9)
print('===Compression Ratio of laplacian 11x11 picture===')
compressionRatioGray(laplacian11, image_laplacian11)

#compression ratio of canny edges images
#canny with combination of max and mind thresholds of max-min; 50-150, 50-100, 150-150, 20-150, 20-100
print('===Compression Ratio of canny edges 50-150 (min-max threshold)  picture===')
compressionRatioGray(cannyedges50150, image_cannyedges50150)
print('===Compression Ratio of canny edges 50-100 (min-max threshold)  picture===')
compressionRatioGray(cannyedges50100, image_cannyedges50100)
print('===Compression Ratio of canny edges 150-150 (min-max threshold)  picture===')
compressionRatioGray(cannyedges150150, image_cannyedges150150)
print('===Compression Ratio of canny edges 20-150 (min-max threshold)  picture===')
compressionRatioGray(cannyedges20150, image_cannyedges20150)
print('===Compression Ratio of canny edges 20-100 (min-max threshold)  picture===')
compressionRatioGray(cannyedges20100, image_cannyedges20100)

# PSNR value of the ground truth image and the filtered images 
print(f"PSNR value of original grayscale and sobel filter in 3 by 3 image is {PSNR(grayscale, sobel3x3)} dB")
print(f"PSNR value of original grayscale and sobel filter in 5 by 5 image is {PSNR(grayscale, sobel5x5)} dB")
print(f"PSNR value of original grayscale and sobel filter in 7 by 7 image is {PSNR(grayscale, sobel7x7)} dB")
print(f"PSNR value of original grayscale and sobel filter in 9 by 9 image is {PSNR(grayscale, sobel9x9)} dB")
print(f"PSNR value of original grayscale and sobel filter in 11 by 11 image is {PSNR(grayscale, sobel11x11)} dB")
print(f"PSNR value of original grayscale and scharr filter in dx & dy = 1 image is {PSNR(grayscale, scharr1)} dB")
print(f"PSNR value of original grayscale and laplacian filter in 3 by 3 image is {PSNR(grayscale, laplacian3)} dB")
print(f"PSNR value of original grayscale and laplacian filter in 5 by 5 image is {PSNR(grayscale, laplacian5)} dB")
print(f"PSNR value of original grayscale and laplacian filter in 7 by 7 image is {PSNR(grayscale, laplacian7)} dB")
print(f"PSNR value of original grayscale and laplacian filter in 9 by 9 image is {PSNR(grayscale, laplacian9)} dB")
print(f"PSNR value of original grayscale and laplacian filter in 11 by 11 image is {PSNR(grayscale, laplacian11)} dB")
print(f"PSNR value of original grayscale and canny edges filter of max 50 and  mix 150 threshold image is {PSNR(grayscale, cannyedges50150)} dB")
print(f"PSNR value of original grayscale and canny edges filter of max 50 and  mix 100 threshold image is {PSNR(grayscale, cannyedges50100)} dB")
print(f"PSNR value of original grayscale and canny edges filter of max 150 and  mix 150 threshold image is {PSNR(grayscale, cannyedges150150)} dB")
print(f"PSNR value of original grayscale and canny edges filter of max 20 and  mix 150 threshold image is {PSNR(grayscale, cannyedges20150)} dB")
print(f"PSNR value of original grayscale and canny edges filter of max 20 and  mix 100 threshold image is {PSNR(grayscale, cannyedges20100)} dB")


