# import cv2
# import pyzbar.pyzbar as pyzbar



# def apply_thresholding(image, threshold_method=cv2.THRESH_BINARY, block_size=5, constant=7):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#     _, thresholded = cv2.threshold(blurred, 0, 255, threshold_method + cv2.THRESH_OTSU)

#     return thresholded

# def apply_denoising(image, denoising_strength=10):
#     denoised = cv2.fastNlMeansDenoisingColored(image, None, denoising_strength, denoising_strength, 7, 21)
#     return denoised

# def apply_image_filter(image, d=9, sigmaColor=75, sigmaSpace=75):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     filtered = cv2.adaptiveBilateralFilter(gray, (d, d), sigmaColor, sigmaSpace)
#     return filtered


# def upscale_image_opencv(image, scale_factor):
#     # Get the original image dimensions
#     height, width = image.shape[:2]

#     # Calculate the new dimensions after upscaling
#     new_height = int(height * scale_factor)
#     new_width = int(width * scale_factor)

#     # Use the resize function to upscale the image
#     upscaled_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

#     return upscaled_image

# def scan_qr_code_from_image(image_path, scale_factor=2):
#     # Read the image using OpenCV
#     image = cv2.imread(image_path)

#     threshold_method = cv2.THRESH_BINARY
#     block_size = 5
#     constant = 5
#     denoising_strength = 20
#     d = 15
#     sigmaColor = 100
#     sigmaSpace = 100


#     # Apply pre-processing techniques with custom parameters
#     preprocessed_image = apply_thresholding(image, threshold_method, block_size, constant)
#     cv2.imshow("result",preprocessed_image)
#     cv2.waitKey(0)
#     # preprocessed_image = apply_denoising(preprocessed_image, denoising_strength)
#     # preprocessed_image = apply_image_filter(preprocessed_image, d, sigmaColor, sigmaSpace)

#     # Upscale the image
#     upscaled_image = upscale_image_opencv(preprocessed_image, scale_factor)

#     # Find and decode QR codes in the upscaled image
#     qr_codes = pyzbar.decode(upscaled_image)

#     # If a QR code is detected, print the decoded information
#     if qr_codes:
#         for qr_code in qr_codes:
#             decoded_info = qr_code.data.decode('utf-8')
#             print("QR Code Detected!")
#             print("Decoded Info:", decoded_info)
#     else:
#         print("No QR Code Detected.")

# if __name__ == "__main__":
#     # Replace 'patOh/to/your/image.jpg' with the actual path to your image file
#     image_path = 'Output2.png'
#     scan_qr_code_from_image(image_path, scale_factor=2)
import cv2
import pyzbar.pyzbar as pyzbar

def apply_thresholding(image, threshold_method=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, block_size=7, constant=5):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresholded = cv2.adaptiveThreshold(gray, 255, threshold_method, cv2.THRESH_BINARY, block_size, constant)

    return thresholded

def apply_denoising(image, denoising_strength=10):
    # Convert the image to three channels
    three_channel_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # Apply non-local means denoising
    denoised = cv2.fastNlMeansDenoisingColored(three_channel_image, None, denoising_strength, denoising_strength, 7, 21)

    return denoised

def apply_image_filter(image, d=9, sigmaColor=75, sigmaSpace=75):
    # Apply bilateral filter for denoising and smoothing
    filtered = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
    return filtered


def upscale_image_opencv(image, scale_factor):
    # Get the original image dimensions
    height, width = image.shape[:2]

    # Calculate the new dimensions after upscaling
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)

    # Use the resize function to upscale the image
    upscaled_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

    return upscaled_image

def find_qr_codes_in_roi(roi):
    qr_codes = pyzbar.decode(roi)
    return qr_codes

if __name__ == "__main__":
    image_path = 'printtest.jpeg'
    
    # Experiment with different parameter values for pre-processing
    threshold_method = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    block_size = 7
    constant = 5
    denoising_strength = 20
    d = 15
    sigmaColor = 100
    sigmaSpace = 100

    # Read the image using OpenCV
    image = cv2.imread(image_path)


    # Apply pre-processing techniques with custom parameters
    preprocessed_image = apply_thresholding(image, threshold_method, block_size, constant)
    cv2.imshow("Result",preprocessed_image)
    cv2.waitKey(0)
    preprocessed_image = apply_denoising(preprocessed_image, denoising_strength)
    cv2.imshow("Result",preprocessed_image)
    cv2.waitKey(0)
    preprocessed_image = apply_image_filter(preprocessed_image, d, sigmaColor, sigmaSpace)
    cv2.imshow("Result",preprocessed_image)
    cv2.waitKey(0)

    # Convert the preprocessed image to grayscale for contour detection
    preprocessed_image_gray = cv2.cvtColor(preprocessed_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Result",preprocessed_image)
    cv2.waitKey(0)

    # Find contours in the pre-processed image
    contours, _ = cv2.findContours(preprocessed_image_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through each contour and extract the QR codes
    qr_codes = []
    for contour in contours:
        # Filter out small contours (to avoid noise)
        if cv2.contourArea(contour) > 100:
            x, y, w, h = cv2.boundingRect(contour)
            roi = preprocessed_image[y:y+h, x:x+w]
            qr_codes += find_qr_codes_in_roi(roi)

    # If QR codes are detected, print the decoded information
    if qr_codes:
        for qr_code in qr_codes:
            decoded_info = qr_code.data.decode('utf-8')
            print("QR Code Detected!")
            print("Decoded Info:", decoded_info)
    else:
        print("No QR Code Detected.")
