import cv2

def do_nothing(x):
    pass

#Creating windows with track Bars
#And specifying windows is resizable
cv2.namedWindow('Track Bars', cv2.WINDOW_NORMAL)

#Defining Track Bars for convenient process of choosing colours
#For minimum range
cv2.createTrackbar('min_blue', 'Track Bars', 0, 255, do_nothing)
cv2.createTrackbar('min_green', 'Track Bars', 0, 255, do_nothing)
cv2.createTrackbar('min_red', 'Track Bars', 0, 255, do_nothing)

# For maximum range
cv2.createTrackbar('max_blue', 'Track Bars', 0, 255, do_nothing)
cv2.createTrackbar('max_green', 'Track Bars', 0, 255, do_nothing)
cv2.createTrackbar('max_red', 'Track Bars', 0, 255, do_nothing)

# Reading image with OpenCV library
# In this way image is opened already as numpy array
# WARNING! OpenCV by default reads images in BGR format
image_BGR = cv2.imread('trial.jpg')

# Showing Original Image
# Giving name to the window with Original Image
# And specifying that window is resizable
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.imshow('Original Image', image_BGR)

# Converting Original Image to HSV
image_HSV = cv2.cvtColor(image_BGR, cv2.COLOR_BGR2HSV)
# Defining loop for choosing right Colours for the Mask
while True:

    # Defining variables for saving values of the Track Bars
    # For minimum range
    min_blue = cv2.getTrackbarPos('min_blue', 'Track Bars')
    min_green = cv2.getTrackbarPos('min_green', 'Track Bars')
    min_red = cv2.getTrackbarPos('min_red', 'Track Bars')

    # For maximum range
    max_blue = cv2.getTrackbarPos('max_blue', 'Track Bars')
    max_green = cv2.getTrackbarPos('max_green', 'Track Bars')
    max_red = cv2.getTrackbarPos('max_red', 'Track Bars')

   # Implementing Mask with chosen colours from Track Bars to HSV Image
    # Defining lower bounds and upper bounds for thresholding
    mask = cv2.inRange(image_HSV,
                       (min_blue, min_green, min_red),
                       (max_blue, max_green, max_red))

    # Showing Binary Image with implemented Mask
    # Giving name to the window with Mask
    # And specifying that window is resizable
    cv2.namedWindow('Binary Image with Mask', cv2.WINDOW_NORMAL)
    cv2.imshow('Binary Image with Mask', mask)

    # Breaking the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Printing final chosen Mask numbers
print('min_blue, min_green, min_red = {0}, {1}, {2}'.format(min_blue, min_green,
                                                            min_red))
print('max_blue, max_green, max_red = {0}, {1}, {2}'.format(max_blue, max_green,
                                                            max_red))



cv2.waitKey()
cv2.destroyAllWindows()
